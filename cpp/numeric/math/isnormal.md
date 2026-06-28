---
title: std::isnormal
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isnormal
---

cpp/numeric/math/unary_is|isnormal
|description=Determines if the given floating point number `num` is normal, i.e. is neither zero, subnormal, infinite, nor NaN.
|condition=is normal

## Example


### Example

```cpp
#include <cfloat>
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::boolalpha
              << "isnormal(NaN) = " << std::isnormal(NAN) << '\n'
              << "isnormal(Inf) = " << std::isnormal(INFINITY) << '\n'
              << "isnormal(0.0) = " << std::isnormal(0.0) << '\n'
              << "isnormal(DBL_MIN/2.0) = " << std::isnormal(DBL_MIN / 2.0) << '\n'
              << "isnormal(1.0) = " << std::isnormal(1.0) << '\n';
}
```


**Output:**
```
isnormal(NaN) = false
isnormal(Inf) = false
isnormal(0.0) = false
isnormal(DBL_MIN/2.0) = false
isnormal(1.0) = true
```


## See also


| cpp/numeric/math/dsc fpclassify | (see dedicated page) |
| cpp/numeric/math/dsc isfinite | (see dedicated page) |
| cpp/numeric/math/dsc isinf | (see dedicated page) |
| cpp/numeric/math/dsc isnan | (see dedicated page) |

