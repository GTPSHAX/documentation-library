---
title: std::isinf
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isinf
---

cpp/numeric/math/unary_is|isinf
|description= Determines if the given floating-point number `num` is a positive or negative infinity.
|condition=is infinite
|note=
[https://gcc.gnu.org/wiki/FloatingPointMath GCC] and [https://clang.llvm.org/docs/UsersManual.html#controlling-floating-point-behavior Clang] support a `-ffinite-math` option (additionally implied by `-ffast-math`), which allows the respective compiler to assume the nonexistence of special IEEE-754 floating point values such as NaN, infinity, or negative zero. In other words, `std::isinf` is assumed to always return `false` under this option.

## Example


### Example

```cpp
#include <cfloat>
#include <cmath>
#include <iostream>
#include <limits>

int main()
{
    const double max = std::numeric_limits<double>::max();
    const double inf = std::numeric_limits<double>::infinity();

    std::cout << std::boolalpha
              << "isinf(NaN) = " << std::isinf(NAN) << '\n'
              << "isinf(Inf) = " << std::isinf(INFINITY) << '\n'
              << "isinf(max) = " << std::isinf(max) << '\n'
              << "isinf(inf) = " << std::isinf(inf) << '\n'
              << "isinf(0.0) = " << std::isinf(0.0) << '\n'
              << "isinf(exp(800)) = " << std::isinf(std::exp(800)) << '\n'
              << "isinf(DBL_MIN/2.0) = " << std::isinf(DBL_MIN / 2.0) << '\n';
}
```


**Output:**
```
isinf(NaN) = false
isinf(Inf) = true
isinf(max) = false
isinf(inf) = true
isinf(0.0) = false
isinf(exp(800)) = true
isinf(DBL_MIN/2.0) = false
```


## See also


| cpp/numeric/math/dsc fpclassify | (see dedicated page) |
| cpp/numeric/math/dsc isfinite | (see dedicated page) |
| cpp/numeric/math/dsc isnan | (see dedicated page) |
| cpp/numeric/math/dsc isnormal | (see dedicated page) |

