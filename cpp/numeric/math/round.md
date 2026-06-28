---
title: std::llround
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/round
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++11|dcl1=
float       round ( float num );
double      round ( double num );
long double round ( long double num );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
round ( /* floating-point-type */ num );
dcla|anchor=no|num=2|since=c++11|constexpr=c++23|
float       roundf( float num );
dcla|anchor=no|num=3|since=c++11|constexpr=c++23|
long double roundl( long double num );
dcl rev multi|num=4|since1=c++11|dcl1=
long lround ( float num );
long lround ( double num );
long lround ( long double num );
|since2=c++23|dcl2=
constexpr long lround( /* floating-point-type */ num );
dcla|anchor=no|num=5|since=c++11|constexpr=c++23|
long lroundf( float num );
dcla|anchor=no|num=6|since=c++11|constexpr=c++23|
long lroundl( long double num );
dcl rev multi|num=7|since1=c++11|dcl1=
long long llround ( float num );
long long llround ( double num );
long long llround ( long double num );
|since2=c++23|dcl2=
constexpr long long llround( /* floating-point-type */ num );
dcla|anchor=no|num=8|since=c++11|constexpr=c++23|
long long llroundf( float num );
dcla|anchor=no|num=9|since=c++11|constexpr=c++23|
long long llroundl( long double num );
**Header:** `<`cmath`>`
dcla|anchor=no|num=A|since=c++11|constexpr=c++23|
template< class Integer >
double round( Integer num );
dcla|anchor=no|num=B|since=c++11|constexpr=c++23|
template< class Integer >
long lround( Integer num );
dcla|anchor=no|num=C|since=c++11|constexpr=c++23|
template< class Integer >
long long llround( Integer num );
```

@1-3@ Computes the nearest integer value to `num` (in floating-point format), rounding halfway cases away from zero, regardless of the current rounding mode.<sup>(since C++23)</sup>  The library provides overloads of `std::round` for all cv-unqualified floating-point types as the type of the parameter `num`.
@4-9@ Computes the nearest integer value to `num` (in integer format), rounding halfway cases away from zero, regardless of the current rounding mode.<sup>(since C++23)</sup>  The library provides overloads of `std::lround` and `std::llround` for all cv-unqualified floating-point types as the type of the parameter `num`.
@A-C@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the nearest integer value to `num`, rounding halfway cases away from zero, is returned.
If a domain error occurs, an implementation-defined value is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the result of `std::lround` or `std::llround` is outside the range representable by the return type, a domain error or a range error may occur.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
: For the `std::round` function:
:* The current rounding mode has no effect.
:* If `num` is ±∞, it is returned, unmodified.
:* If `num` is ±0, it is returned, unmodified.
:* If `num` is NaN, NaN is returned.
: For `std::lround` and `std::llround` functions:
:* `FE_INEXACT` is never raised.
:* The current rounding mode has no effect.
:* If `num` is ±∞, `FE_INVALID` is raised and an implementation-defined value is returned.
:* If the result of the rounding is outside the range of the return type, `FE_INVALID` is raised and an implementation-defined value is returned.
:* If `num` is NaN, `FE_INVALID` is raised and an implementation-defined value is returned.

## Notes

`FE_INEXACT` may be (but is not required to be) raised by `std::round` when rounding a non-integer finite value.
The largest representable floating-point values are exact integers in all standard floating-point formats, so `std::round` never overflows on its own; however the result may overflow any integer type (including `std::intmax_t`), when stored in an integer variable.
[https://pubs.opengroup.org/onlinepubs/9699919799/functions/lround.html POSIX specifies] that all cases where `std::lround` or `std::llround` raise `FE_INEXACT` are domain errors.
The `double` version of `std::round` behaves as if implemented as follows:

```cpp
#include <cfenv>
#include <cmath>

#pragma STDC FENV_ACCESS ON

double round(double x)
{
    const int save_round = std::fegetround();
    std::fesetround(FE_TOWARDZERO);
    const double result = std::rint(std::copysign(0.5 + std::fabs(x), x));
    std::fesetround(save_round);
    return result;
}
```


## Example


### Example

```cpp
#include <cassert>
#include <cfenv>
#include <cfloat>
#include <climits>
#include <cmath>
#include <iostream>

// #pragma STDC FENV_ACCESS ON

double custom_round(double x)
{
    const int save_round = std::fegetround();
    std::fesetround(FE_TOWARDZERO);
    const double result = std::rint(std::copysign(0.5 + std::fabs(x), x));
    std::fesetround(save_round);
    return result;
}

void test_custom_round()
{
    for (const double x :
        {
            0.0, 0.3,
            0.5 - DBL_EPSILON / 2,
            0.5,
            0.5 + DBL_EPSILON / 2,
            0.7, 1.0, 2.3, 2.5, 2.7, 3.0,
            static_cast<double>(INFINITY)
        })
        assert(round(+x) == custom_round(+x) && round(-x) == custom_round(-x));
}

int main()
{
    test_custom_round();

    std::cout << std::showpos;

    // round
    std::cout << "round(+2.3) = " << std::round(2.3)
              << "  round(+2.5) = " << std::round(2.5)
              << "  round(+2.7) = " << std::round(2.7) << '\n'
              << "round(-2.3) = " << std::round(-2.3)
              << "  round(-2.5) = " << std::round(-2.5)
              << "  round(-2.7) = " << std::round(-2.7) << '\n';

    std::cout << "round(-0.0) = " << std::round(-0.0)  << '\n'
              << "round(-Inf) = " << std::round(-INFINITY) << '\n';

    // lround
    std::cout << "lround(+2.3) = " << std::lround(2.3)
              << "  lround(+2.5) = " << std::lround(2.5)
              << "  lround(+2.7) = " << std::lround(2.7) << '\n'
              << "lround(-2.3) = " << std::lround(-2.3)
              << "  lround(-2.5) = " << std::lround(-2.5)
              << "  lround(-2.7) = " << std::lround(-2.7) << '\n';

    std::cout << "lround(-0.0) = " << std::lround(-0.0)  << '\n'
              << "lround(-Inf) = " << std::lround(-INFINITY) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "std::lround(LONG_MAX+1.5) = "
              << std::lround(LONG_MAX + 1.5) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID was raised\n";
}
```


**Output:**
```
round(+2.3) = +2  round(+2.5) = +3  round(+2.7) = +3
round(-2.3) = -2  round(-2.5) = -3  round(-2.7) = -3
round(-0.0) = -0
round(-Inf) = -inf
lround(+2.3) = +2  lround(+2.5) = +3  lround(+2.7) = +3
lround(-2.3) = -2  lround(-2.5) = -3  lround(-2.7) = -3
lround(-0.0) = +0
lround(-Inf) = -9223372036854775808
std::lround(LONG_MAX+1.5) = -9223372036854775808
    FE_INVALID was raised
```


## See also


| cpp/numeric/math/dsc floor | (see dedicated page) |
| cpp/numeric/math/dsc ceil | (see dedicated page) |
| cpp/numeric/math/dsc trunc | (see dedicated page) |

