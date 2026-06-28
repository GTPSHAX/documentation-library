---
title: std::pow
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/pow
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|dcl1=
float       pow ( float base, float exp );
double      pow ( double base, double exp );
long double pow ( long double base, long double exp );
|since2=c++23|dcl2=
/* floating-point-type */
pow ( /* floating-point-type */ base,
/* floating-point-type */ exp )
|notes2=<sup>(constexpr C++26)</sup>
dcl|num=2|until=c++11|
float       pow ( float base, int exp );
double      pow ( double base, int exp );
long double pow ( long double base, int exp );
|
float       powf( float base, float exp );
|
long double powl( long double base, long double exp );
**Header:** `<`cmath`>`
|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
pow ( Arithmetic1 base, Arithmetic2 exp );
```

@1-4@ Computes the value of `base` raised to the power `exp`.<sup>(since C++23)</sup>  The library provides overloads of `std::pow` for all cv-unqualified floating-point types as the type of the parameters `base` and `exp`.
rrev|since=c++11|
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `base` - base as a floating-point or integer value
- `exp` - exponent as a floating-point or integer value

## Return value

If no errors occur, `base` raised to the power of `exp` ($base), is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a pole error or a range error due to overflow occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If `base` is finite and negative and `exp` is finite and non-integer, a domain error occurs and a range error may occur.
If `base` is zero and `exp` is zero, a domain error may occur.
If `base` is zero and `exp` is negative, a domain error or a pole error may occur.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* `pow(+0, exp)`, where `exp` is a negative odd integer, returns +∞ and raises `FE_DIVBYZERO`.
* `pow(-0, exp)`, where `exp` is a negative odd integer, returns -∞ and raises `FE_DIVBYZERO`.
* `pow(±0, exp)`, where `exp` is negative, finite, and is an even integer or a non-integer, returns +∞ and raises `FE_DIVBYZERO`.
* `pow(±0, -∞)` returns +∞ and may raise `FE_DIVBYZERO`.
* `pow(+0, exp)`, where `exp` is a positive odd integer, returns +0.
* `pow(-0, exp)`, where `exp` is a positive odd integer, returns -0.
* `pow(±0, exp)`, where `exp` is positive non-integer or a positive even integer, returns +0.
* `pow(-1, ±∞)` returns 1.
* `pow(+1, exp)` returns 1 for any `exp`, even when `exp` is NaN.
* `pow(base, ±0)` returns 1 for any `base`, even when `base` is NaN.
* `pow(base, exp)` returns NaN and raises `FE_INVALID` if `base` is finite and negative and `exp` is finite and non-integer.
* `pow(base, -∞)` returns +∞ for any `.
* `pow(base, -∞)` returns +0 for any `.
* `pow(base, +∞)` returns +0 for any `.
* `pow(base, +∞)` returns +∞ for any `.
* `pow(-∞, exp)` returns -0 if `exp` is a negative odd integer.
* `pow(-∞, exp)` returns +0 if `exp` is a negative non-integer or negative even integer.
* `pow(-∞, exp)` returns -∞ if `exp` is a positive odd integer.
* `pow(-∞, exp)` returns +∞ if `exp` is a positive non-integer or positive even integer.
* `pow(+∞, exp)` returns +0 for any negative `exp`.
* `pow(+∞, exp)` returns +∞ for any positive `exp`.
* except where specified above, if any argument is NaN, NaN is returned.

## Notes

C++98 added overloads where `exp` has type `int` on top of C , and the return type of `std::pow(float, int)` was `float`. However, the additional overloads introduced in C++11 specify that `std::pow(float, int)` should return `double`.  was raised to target this conflict, and the resolution is to removed the extra `int` `exp` overloads.
Although `std::pow` cannot be used to obtain a root of a negative number, `std::cbrt` is provided for the common case where `exp` is 1/3.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <cstring>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    // typical usage
    std::cout << "pow(2, 10) = " << std::pow(2, 10) << '\n'
              << "pow(2, 0.5) = " << std::pow(2, 0.5) << '\n'
              << "pow(-2, -3) = " << std::pow(-2, -3) << '\n';

    // special values
    std::cout << "pow(-1, NAN) = " << std::pow(-1, NAN) << '\n'
              << "pow(+1, NAN) = " << std::pow(+1, NAN) << '\n'
              << "pow(INFINITY, 2) = " << std::pow(INFINITY, 2) << '\n'
              << "pow(INFINITY, -1) = " << std::pow(INFINITY, -1) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "pow(-1, 1/3) = " << std::pow(-1, 1.0 / 3) << '\n';
    if (errno == EDOM)
        std::cout << "    errno == EDOM " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";

    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "pow(-0, -3) = " << std::pow(-0.0, -3) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
pow(2, 10) = 1024
pow(2, 0.5) = 1.41421
pow(-2, -3) = -0.125
pow(-1, NAN) = nan
pow(+1, NAN) = 1
pow(INFINITY, 2) = inf
pow(INFINITY, -1) = 0
pow(-1, 1/3) = -nan
    errno == EDOM Numerical argument out of domain
    FE_INVALID raised
pow(-0, -3) = -inf
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc sqrt | (see dedicated page) |
| cpp/numeric/math/dsc cbrt | (see dedicated page) |
| cpp/numeric/math/dsc hypot | (see dedicated page) |
| cpp/numeric/complex/dsc pow | (see dedicated page) |
| cpp/numeric/valarray/dsc pow | (see dedicated page) |

