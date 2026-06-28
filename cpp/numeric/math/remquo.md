---
title: std::remquo
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/remquo
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++11|dcl1=
float       remquo ( float x, float y, int* quo );
double      remquo ( double x, double y, int* quo );
long double remquo ( long double x, long double y, int* quo );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
remquo ( /* floating-point-type */ x,
/* floating-point-type */ y, int* quo );
dcla|anchor=no|num=2|since=c++11|constexpr=c++23|
float       remquof( float x, float y, int* quo );
dcla|anchor=no|num=3|since=c++11|constexpr=c++23|
long double remquol( long double x, long double y, int* quo );
**Header:** `<`cmath`>`
dcla|anchor=no|num=A|since=c++11|constexpr=c++23|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
remquo( Arithmetic1 x, Arithmetic2 y, int* quo );
```

@1-3@ Computes the floating-point remainder of the division operation `x / y` as the `std::remainder()` function does. Additionally, the sign and at least the three of the last bits of `x / y` will be stored in `quo`, sufficient to determine the octant of the result within a period.<sup>(since C++23)</sup>  The library provides overloads of `std::remquo` for all cv-unqualified floating-point types as the type of the parameters `x` and `y`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `x, y` - floating-point or integer values
- `quo` - pointer to `int` to store the sign and some bits of `x / y`

## Return value

If successful, returns the floating-point remainder of the division `x / y` as defined in `std::remainder`, and stores, in `*quo`, the sign and at least three of the least significant bits of `x / y` (formally, stores a value whose sign is the sign of `x / y` and whose magnitude is congruent $modulo 2 to the magnitude of the integral quotient of `x / y`, where `n` is an implementation-defined integer greater than or equal to `3`).
If `y` is zero, the value stored in `*quo` is unspecified.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result is returned if subnormals are supported.
If `y` is zero, but the domain error does not occur, zero is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error may occur if `y` is zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* The current rounding mode has no effect.
* `FE_INEXACT` is never raised.
* If `x` is ±∞ and `y` is not NaN, NaN is returned and `FE_INVALID` is raised.
* If `y` is ±0 and `x` is not NaN, NaN is returned and `FE_INVALID` is raised.
* If either `x` or `y` is NaN, NaN is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/remquo.html POSIX requires] that a domain error occurs if `x` is infinite or `y` is zero.
This function is useful when implementing periodic functions with the period exactly representable as a floating-point value: when calculating $sin(πx)$ for a very large `x`, calling `std::sin` directly may result in a large error, but if the function argument is first reduced with `std::remquo`, the low-order bits of the quotient may be used to determine the sign and the octant of the result within the period, while the remainder may be used to calculate the value with high precision.
On some platforms this operation is supported by hardware (and, for example, on Intel CPUs, `FPREM1` leaves exactly 3 bits of precision in the quotient when complete).

## Example


### Example

```cpp
#include <cfenv>
#include <cmath>
#include <iostream>

#ifndef __GNUC__
#pragma STDC FENV_ACCESS ON
#endif

const double pi = std::acos(-1); // or std::numbers::pi since C++20

double cos_pi_x_naive(double x)
{
    return std::cos(pi * x);
}

// the period is 2, values are (0;0.5) positive, (0.5;1.5) negative, (1.5,2) positive
double cos_pi_x_smart(double x)
{
    int quadrant;
    double rem = std::remquo(x, 1, &quadrant);
    quadrant = static_cast<unsigned>(quadrant) % 2; // The period is 2.
    return quadrant == 0 ?  std::cos(pi * rem)
                         : -std::cos(pi * rem);
}

int main()
{
    std::cout << std::showpos
              << "naive:\n"
              << "  cos(pi * 0.25) = " << cos_pi_x_naive(0.25) << '\n'
              << "  cos(pi * 1.25) = " << cos_pi_x_naive(1.25) << '\n'
              << "  cos(pi * 2.25) = " << cos_pi_x_naive(2.25) << '\n'
              << "smart:\n"
              << "  cos(pi * 0.25) = " << cos_pi_x_smart(0.25) << '\n'
              << "  cos(pi * 1.25) = " << cos_pi_x_smart(1.25) << '\n'
              << "  cos(pi * 2.25) = " << cos_pi_x_smart(2.25) << '\n'
              << "naive:\n"
              << "  cos(pi * 1000000000000.25) = "
              << cos_pi_x_naive(1000000000000.25) << '\n'
              << "  cos(pi * 1000000000001.25) = "
              << cos_pi_x_naive(1000000000001.25) << '\n'
              << "smart:\n"
              << "  cos(pi * 1000000000000.25) = "
              << cos_pi_x_smart(1000000000000.25) << '\n'
              << "  cos(pi * 1000000000001.25) = "
              << cos_pi_x_smart(1000000000001.25) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    int quo;
    std::cout << "remquo(+Inf, 1) = " << std::remquo(INFINITY, 1, &quo) << '\n';
    if (fetestexcept(FE_INVALID))
        std::cout << "  FE_INVALID raised\n";
}
```


**Output:**
```
naive:
  cos(pi * 0.25) = +0.707107
  cos(pi * 1.25) = -0.707107
  cos(pi * 2.25) = +0.707107
smart:
  cos(pi * 0.25) = +0.707107
  cos(pi * 1.25) = -0.707107
  cos(pi * 2.25) = +0.707107
naive:
  cos(pi * 1000000000000.25) = +0.707123
  cos(pi * 1000000000001.25) = -0.707117
smart:
  cos(pi * 1000000000000.25) = +0.707107
  cos(pi * 1000000000001.25) = -0.707107
<!--note: this is exact output from:
 * Intel C++ on Linux, Oracle and GNU C++ on Sparc,
 * IBM and GNU C++ compilers on a Power platform,
 * GNU C++ and Clang C++ on Linux
-->
remquo(+Inf, 1) = -nan
  FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc div | (see dedicated page) |
| cpp/numeric/math/dsc fmod | (see dedicated page) |
| cpp/numeric/math/dsc remainder | (see dedicated page) |

