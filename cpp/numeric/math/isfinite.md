---
title: std::isfinite
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isfinite
---

cpp/numeric/math/unary_is|isfinite
|description=Determines if the given floating point number `num` has finite value i.e. it is normal, subnormal or zero, but not infinite or NaN.
|condition=has finite value

## Examples


### Example

```cpp
#include <cfloat>
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::boolalpha
              << "isfinite(NaN) = " << std::isfinite(NAN) << '\n'
              << "isfinite(Inf) = " << std::isfinite(INFINITY) << '\n'
              << "isfinite(-Inf) = " << std::isfinite(-INFINITY) << '\n'
              << "isfinite(HUGE_VAL) = " << std::isfinite(HUGE_VAL) << '\n'
              << "isfinite(0.0) = " << std::isfinite(0.0) << '\n'
              << "isfinite(exp(800)) = " << std::isfinite(std::exp(800)) << '\n'
              << "isfinite(DBL_MIN/2.0) = " << std::isfinite(DBL_MIN / 2.0) << '\n';
}
```


**Output:**
```
isfinite(NaN) = false
isfinite(Inf) = false
isfinite(-Inf) = false
isfinite(HUGE_VAL) = false
isfinite(0.0) = true
isfinite(exp(800)) = false
isfinite(DBL_MIN/2.0) = true
```


## See also


| cpp/numeric/math/dsc fpclassify | (see dedicated page) |
| cpp/numeric/math/dsc isinf | (see dedicated page) |
| cpp/numeric/math/dsc isnan | (see dedicated page) |
| cpp/numeric/math/dsc isnormal | (see dedicated page) |

