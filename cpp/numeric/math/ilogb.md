---
title: std::ilogb
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/ilogb
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++11|dcl1=
int ilogb ( float num );
int ilogb ( double num );
int ilogb ( long double num );
|since2=c++23|dcl2=
constexpr int ilogb( /* floating-point-type */ num );
|
int ilogbf( float num );
|
int ilogbl( long double num );
dcl|num=4|since=c++11|
#define FP_ILOGB0   /* implementation-defined */
dcl|num=5|since=c++11|
#define FP_ILOGBNAN /* implementation-defined */
**Header:** `<`cmath`>`
|
template< class Integer >
int ilogb ( Integer num );
```

@1-3@ Extracts the value of the unbiased exponent from the floating-point argument `num`, and returns it as a signed integer value.<sup>(since C++23)</sup>  The library provides overloads of `std::ilogb` for all cv-unqualified floating-point types as the type of the parameter `num`.
4. Expands to integer constant expression whose value is either `INT_MIN` or `-INT_MAX`.
5. Expands to integer constant expression whose value is either `INT_MIN` or `+INT_MAX`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.
Formally, the unbiased exponent is the integral part of $log as a signed integral value, for non-zero `num`, where `r` is `std::numeric_limits<T>::radix` and `T` is the floating-point type of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the unbiased exponent of `num` is returned as a signed int value.
If `num` is zero, `FP_ILOGB0` is returned.
If `num` is infinite, `INT_MAX` is returned.
If `num` is a NaN, `FP_ILOGBNAN` is returned.
If the correct result is greater than `INT_MAX` or smaller than `INT_MIN`, the return value is unspecified.

## Error handling

Errors are reported as specified in `math_errhandling`.
A domain error or range error may occur if `num` is zero, infinite, or NaN.
If the correct result is greater than `INT_MAX` or smaller than `INT_MIN`, a domain error or a range error may occur.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the correct result is greater than `INT_MAX` or smaller than `INT_MIN`, `FE_INVALID` is raised.
* If `num` is ±0, ±∞, or NaN, `FE_INVALID` is raised.
* In all other cases, the result is exact (`FE_INEXACT` is never raised) and the current rounding mode is ignored.

## Notes

If `num` is not zero, infinite, or NaN, the value returned is exactly equivalent to `static_cast<int>(std::logb(num))`.
[https://pubs.opengroup.org/onlinepubs/9699919799/functions/ilogb.html POSIX requires] that a domain error occurs if `num` is zero, infinite, NaN, or if the correct result is outside of the range of `int`.
POSIX also requires that, on XSI-conformant systems, the value returned when the correct result is greater than `INT_MAX` is `INT_MAX` and the value returned when the correct result is less than `INT_MIN` is `INT_MIN`.
The correct result can be represented as `int` on all known implementations. For overflow to occur, `INT_MAX` must be less than `LDBL_MAX_EXP * std::log2(FLT_RADIX)` or `INT_MIN` must be greater than `LDBL_MIN_EXP - LDBL_MANT_DIG) * std::log2(FLT_RADIX)`.
The value of the exponent returned by `std::ilogb` is always 1 less than the exponent retuned by `std::frexp` because of the different normalization requirements: for the exponent `e` returned by `std::ilogb`, $ is between `1` and `r` (typically between `1` and `2`), but for the exponent `e` returned by `std::frexp`, $ is between `0.5` and `1`.

## Example


### Example

```cpp
#include <cfenv>
#include <cmath>
#include <iostream>
#include <limits>

// #pragma STDC FENV_ACCESS ON

int main()
{
    double f = 123.45;
    std::cout << "Given the number " << f << " or " << std::hexfloat
              << f << std::defaultfloat << " in hex,\n";

    double f3;
    double f2 = std::modf(f, &f3);
    std::cout << "modf() makes " << f3 << " + " << f2 << '\n';

    int i;
    f2 = std::frexp(f, &i);
    std::cout << "frexp() makes " << f2 << " * 2^" << i << '\n';

    i = std::ilogb(f);
    std::cout << "logb()/ilogb() make " << f / std::scalbn(1.0, i) << " * "
              << std::numeric_limits<double>::radix
              << "^" << std::ilogb(f) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "ilogb(0) = " << std::ilogb(0) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,
modf() makes 123 + 0.45
frexp() makes 0.964453 * 2^7
logb()/ilogb() make 1.92891 * 2^6
ilogb(0) = -2147483648
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc frexp | (see dedicated page) |
| cpp/numeric/math/dsc logb | (see dedicated page) |
| cpp/numeric/math/dsc scalbn | (see dedicated page) |

