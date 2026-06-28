---
title: std::ldexp
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/ldexp
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|dcl1=
float       ldexp ( float num, int exp );
double      ldexp ( double num, int exp );
long double ldexp ( long double num, int exp );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
ldexp ( /* floating-point-type */ num, int exp );
|
float       ldexpf( float num, int exp );
|
long double ldexpl( long double num, int exp );
**Header:** `<`cmath`>`
|
template< class Integer >
double      ldexp ( Integer num, int exp );
```

@1-3@ Multiplies a floating point value `num` by the number `2` raised to the `exp` power.<sup>(since C++23)</sup>  The library provides overloads of `std::ldexp` for all cv-unqualified floating-point types as the type of the parameter `num`.
rrev|since=c++11|
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or integer value
- `exp` - integer value

## Return value

If no errors occur, `num` multiplied by 2 to the power of `exp` ($num&times;2) is returned.
If a range error due to overflow occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.
If a range error due to underflow occurs, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* Unless a range error occurs, `FE_INEXACT` is never raised (the result is exact).
* Unless a range error occurs, the current rounding mode is ignored.
* If `num` is ±0, it is returned, unmodified.
* If `num` is ±∞, it is returned, unmodified.
* If `exp` is 0, then `num` is returned, unmodified.
* If `num` is NaN, NaN is returned.

## Notes

On binary systems (where `FLT_RADIX` is `2`), `std::ldexp` is equivalent to `std::scalbn`.
The function `std::ldexp` ("load exponent"), together with its dual, `std::frexp`, can be used to manipulate the representation of a floating-point number without direct bit manipulations.
On many implementations, `std::ldexp` is less efficient than multiplication or division by a power of two using arithmetic operators.
For exponentiation of 2 by a floating point exponent, `std::exp2` can be used.

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
    std::cout
        << "ldexp(5, 3) = 5 * 8 = " << std::ldexp(5, 3) << '\n'
        << "ldexp(7, -4) = 7 / 16 = " << std::ldexp(7, -4) << '\n'
        << "ldexp(1, -1074) = " << std::ldexp(1, -1074)
        << " (minimum positive subnormal float64_t)\n"
        << "ldexp(nextafter(1,0), 1024) = "
        << std::ldexp(std::nextafter(1,0), 1024)
        << " (largest finite float64_t)\n";

    // special values
    std::cout << "ldexp(-0, 10) = " << std::ldexp(-0.0, 10) << '\n'
              << "ldexp(-Inf, -1) = " << std::ldexp(-INFINITY, -1) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    errno = 0;
    const double inf = std::ldexp(1, 1024);
    const bool is_range_error = errno == ERANGE;

    std::cout << "ldexp(1, 1024) = " << inf << '\n';
    if (is_range_error)
        std::cout << "    errno == ERANGE: " << std::strerror(ERANGE) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
ldexp(5, 3) = 5 * 8 = 40
ldexp(7, -4) = 7 / 16 = 0.4375
ldexp(1, -1074) = 4.94066e-324 (minimum positive subnormal float64_t)
ldexp(nextafter(1,0), 1024) = 1.79769e+308 (largest finite float64_t)
ldexp(-0, 10) = -0
ldexp(-Inf, -1) = -inf
ldexp(1, 1024) = inf
    errno == ERANGE: Numerical result out of range
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc frexp | (see dedicated page) |
| cpp/numeric/math/dsc scalbn | (see dedicated page) |
| cpp/numeric/math/dsc exp2 | (see dedicated page) |

