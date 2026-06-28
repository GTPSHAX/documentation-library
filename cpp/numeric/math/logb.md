---
title: std::logb
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/logb
---

cpp/numeric/math/declarations
|family=logb
|param1=num
|constexpr_since=23
|desc=Extracts the value of the unbiased radix-independent exponent from the floating-point argument `num`, and returns it as a floating-point value.
Formally, the unbiased exponent is the signed integral part of $log (returned by this function as a floating-point value), for non-zero `num`, where `r` is `std::numeric_limits<T>::radix` and `T` is the floating-point type of `num`. If `num` is subnormal, it is treated as though it was normalized.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the unbiased exponent of `num` is returned as a signed floating-point value.
If a domain error occurs, an implementation-defined value is returned.
If a pole error occurs, `HUGE_VAL|-HUGE_VAL`, `-HUGE_VALF`, or `-HUGE_VALL` is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain or range error may occur if `num` is zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If `num` is ±0, -∞ is returned and `FE_DIVBYZERO` is raised.
* If `num` is ±∞, +∞ is returned.
* If `num` is NaN, NaN is returned.
* In all other cases, the result is exact (`FE_INEXACT` is never raised) and the current rounding mode is ignored.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/logb.html POSIX requires] that a pole error occurs if `num` is ±0.
The value of the exponent returned by `std::logb` is always 1 less than the exponent returned by `std::frexp` because of the different normalization requirements: for the exponent `e` returned by `std::logb`, $ is between `1` and `r` (typically between `1` and `2`), but for the exponent `e` returned by `std::frexp`, $ is between `0.5` and `1`.

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

    std::cout << "logb(0) = " << std::logb(0) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,
modf() makes 123 + 0.45
frexp() makes 0.964453 * 2^7
logb()/ilogb() make 1.92891 * 2^6
logb(0) = -Inf
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc frexp | (see dedicated page) |
| cpp/numeric/math/dsc ilogb | (see dedicated page) |
| cpp/numeric/math/dsc scalbn | (see dedicated page) |

