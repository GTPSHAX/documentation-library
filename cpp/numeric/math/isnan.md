---
title: std::isnan
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isnan
---

cpp/numeric/math/unary is|isnan
|description=Determines if the given floating point number `num` is a not-a-number (NaN) value.
|condition=is a NaN
|note=
There are many different NaN values with different sign bits and payloads, see `std::nan` and `std::numeric_limits::quiet_NaN`.
NaN values never compare equal to themselves or to other NaN values. Copying a NaN is not required, by IEEE-754, to preserve its bit representation (sign and `payload`), though most implementation do.
Another way to test if a floating-point value is NaN is to compare it with itself: }.
[https://gcc.gnu.org/wiki/FloatingPointMath GCC] and [https://clang.llvm.org/docs/UsersManual.html#controlling-floating-point-behavior Clang] support a `-ffinite-math` option (additionally implied by `-ffast-math`), which allows the respective compiler to assume the nonexistence of special IEEE-754 floating point values such as NaN, infinity, or negative zero. In other words, `std::isnan` is assumed to always return `false` under this option.

## Example


### Example

```cpp
#include <cfloat>
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::boolalpha
              << "isnan(NaN) = " << std::isnan(NAN) << '\n'
              << "isnan(Inf) = " << std::isnan(INFINITY) << '\n'
              << "isnan(0.0) = " << std::isnan(0.0) << '\n'
              << "isnan(DBL_MIN/2.0) = " << std::isnan(DBL_MIN / 2.0) << '\n'
              << "isnan(0.0 / 0.0)   = " << std::isnan(0.0 / 0.0) << '\n'
              << "isnan(Inf - Inf)   = " << std::isnan(INFINITY - INFINITY) << '\n';
}
```


**Output:**
```
isnan(NaN) = true
isnan(Inf) = false
isnan(0.0) = false
isnan(DBL_MIN/2.0) = false
isnan(0.0 / 0.0)   = true
isnan(Inf - Inf)   = true
```


## See also


| cpp/numeric/math/dsc fnan | (see dedicated page) |
| cpp/numeric/math/dsc fpclassify | (see dedicated page) |
| cpp/numeric/math/dsc isfinite | (see dedicated page) |
| cpp/numeric/math/dsc isinf | (see dedicated page) |
| cpp/numeric/math/dsc isnormal | (see dedicated page) |
| cpp/numeric/math/dsc isunordered | (see dedicated page) |

