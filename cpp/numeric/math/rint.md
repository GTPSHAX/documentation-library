---
title: std::llrint
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/rint
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++11|dcl1=
float       rint ( float num );
double      rint ( double num );
long double rint ( long double num );
|since2=c++23|dcl2=
/* floating-point-type */ rint( /* floating-point-type */ num );
dcl|num=2|since=c++11|
float       rintf( float num );
dcl|num=3|since=c++11|
long double rintl( long double num );
dcl rev multi|num=4|since1=c++11|dcl1=
long lrint ( float num );
long lrint ( double num );
long lrint ( long double num );
|since2=c++23|dcl2=
long lrint ( /* floating-point-type */ num );
dcl|num=5|since=c++11|
long lrintf( float num );
dcl|num=6|since=c++11|
long lrintl( long double num );
dcl rev multi|num=7|since1=c++11|dcl1=
long long llrint ( float num );
long long llrint ( double num );
long long llrint ( long double num );
|since2=c++23|dcl2=
long long llrint ( /* floating-point-type */ num );
dcl|num=8|since=c++11|
long long llrintf( float num );
dcl|num=9|since=c++11|
long long llrintl( long double num );
**Header:** `<`cmath`>`
dcl|num=A|since=c++11|
template< class Integer >
double rint( Integer num );
dcl|num=B|since=c++11|
template< class Integer >
long lrint( Integer num );
dcl|num=C|since=c++11|
template< class Integer >
long long llrint( Integer num );
```

@1-3@ Rounds the floating-point argument `num` to an integer value (in floating-point format), using the current rounding mode.<sup>(since C++23)</sup>  The library provides overloads of `std::rint` for all cv-unqualified floating-point types as the type of the parameter `num`.
@4-9@ Rounds the floating-point argument `num` to an integer value, using the current rounding mode.<sup>(since C++23)</sup>  The library provides overloads of `std::lrint` and `std::llrint` for all cv-unqualified floating-point types as the type of the parameter `num`.
@A-C@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the nearest integer value to `num`, according to the current rounding mode, is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the result of `std::lrint` or `std::llrint` is outside the range representable by the return type, a domain error or a range error may occur.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
: For the `std::rint` function:
* If `num` is ±∞, it is returned, unmodified.
* If `num` is ±0, it is returned, unmodified.
* If `num` is NaN, NaN is returned.
: For `std::lrint` and `std::llrint` functions:
* If `num` is ±∞, `FE_INVALID` is raised and an implementation-defined value is returned.
* If the result of the rounding is outside the range of the return type, `FE_INVALID` is raised and an implementation-defined value is returned.
* If `num` is NaN, `FE_INVALID` is raised and an implementation-defined value is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/lrint.html POSIX specifies] that all cases where `std::lrint` or `std::llrint` raise `FE_INEXACT` are domain errors.
As specified in `math_errhandling`, `FE_INEXACT` may be (but isn't required to be on non-IEEE floating-point platforms) raised by `std::rint` when rounding a non-integer finite value.
The only difference between `std::rint` and `std::nearbyint` is that `std::nearbyint` never raises `FE_INEXACT`.
The largest representable floating-point values are exact integers in all standard floating-point formats, so `std::rint` never overflows on its own; however the result may overflow any integer type (including `std::intmax_t`), when stored in an integer variable.
If the current rounding mode is:
* `FE_DOWNWARD`, then `std::rint` is equivalent to `std::floor`.
* `FE_UPWARD`, then `std::rint` is equivalent to `std::ceil`.
* `FE_TOWARDZERO`, then `std::rint` is equivalent to `std::trunc`.
* `FE_TONEAREST`, then `std::rint` differs from `std::round` in that halfway cases are rounded to even rather than away from zero.

## Example


### Example

```cpp
#include <cfenv>
#include <climits>
#include <cmath>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    std::fesetround(FE_TONEAREST);
    std::cout << "Rounding to nearest (halfway cases to even):\n"
              << "  rint(+2.3) = " << std::rint(2.3) << '\n'
              << "  rint(+2.5) = " << std::rint(2.5) << '\n'
              << "  rint(+3.5) = " << std::rint(3.5) << '\n'
              << "  rint(-2.3) = " << std::rint(-2.3) << '\n'
              << "  rint(-2.5) = " << std::rint(-2.5) << '\n'
              << "  rint(-3.5) = " << std::rint(-3.5) << '\n';

    std::fesetround(FE_DOWNWARD);
    std::cout << "Rounding down:\n"
              << "  rint(+2.3) = " << std::rint(2.3) << '\n'
              << "  rint(+2.5) = " << std::rint(2.5) << '\n'
              << "  rint(+3.5) = " << std::rint(3.5) << '\n'
              << "  rint(-2.3) = " << std::rint(-2.3) << '\n'
              << "  rint(-2.5) = " << std::rint(-2.5) << '\n'
              << "  rint(-3.5) = " << std::rint(-3.5) << '\n'
              << "Rounding down with lrint:\n"
              << "  lrint(+2.3) = " << std::lrint(2.3) << '\n'
              << "  lrint(+2.5) = " << std::lrint(2.5) << '\n'
              << "  lrint(+3.5) = " << std::lrint(3.5) << '\n'
              << "  lrint(-2.3) = " << std::lrint(-2.3) << '\n'
              << "  lrint(-2.5) = " << std::lrint(-2.5) << '\n'
              << "  lrint(-3.5) = " << std::lrint(-3.5) << '\n'
              << "Special values:\n"
              << "  lrint(-0.0) = " << std::lrint(-0.0) << '\n'
              << std::hex << std::showbase
              << "  lrint(-Inf) = " << std::lrint(-INFINITY) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "std::rint(0.1) = " << std::rint(.1) << '\n';
    if (std::fetestexcept(FE_INEXACT))
        std::cout << "  FE_INEXACT was raised\n";

    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "std::lrint(LONG_MIN-2048.0) = "
              << std::lrint(LONG_MIN - 2048.0) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "  FE_INVALID was raised\n";
}
```


**Output:**
```
Rounding to nearest (halfway cases to even):
  rint(+2.3) = 2
  rint(+2.5) = 2
  rint(+3.5) = 4
  rint(-2.3) = -2
  rint(-2.5) = -2
  rint(-3.5) = -4
Rounding down:
  rint(+2.3) = 2
  rint(+2.5) = 2
  rint(+3.5) = 4
  rint(-2.3) = -2
  rint(-2.5) = -2
  rint(-3.5) = -4
Rounding down with lrint:
  lrint(+2.3) = 2
  lrint(+2.5) = 2
  lrint(+3.5) = 3
  lrint(-2.3) = -3
  lrint(-2.5) = -3
  lrint(-3.5) = -4
Special values:
  lrint(-0.0) = 0
  lrint(-Inf) = 0x8000000000000000
std::rint(0.1) = 0
std::lrint(LONG_MIN-2048.0) = 0x8000000000000000
  FE_INVALID was raised
```


## See also


| cpp/numeric/math/dsc trunc | (see dedicated page) |
| cpp/numeric/math/dsc nearbyint | (see dedicated page) |
| cpp/numeric/fenv/dsc feround | (see dedicated page) |

