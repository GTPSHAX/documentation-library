---
title: std::signbit
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/signbit
---

cpp/numeric/math/unary_is|signbit
|description= Determines if the given floating point number `num` is negative.
|condition=is negative
|note=
This function detects the sign bit of zeroes, infinities, and NaNs. Along with `std::copysign`, `std::signbit` is one of the only two portable ways to examine the sign of a NaN.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::boolalpha
              << "signbit(+0.0) = " << std::signbit(+0.0) << '\n'
              << "signbit(-0.0) = " << std::signbit(-0.0) << '\n'
              << "signbit(+nan) = " << std::signbit(+NAN) << '\n'
              << "signbit(-nan) = " << std::signbit(-NAN) << '\n'
              << "signbit(+inf) = " << std::signbit(+INFINITY) << '\n'
              << "signbit(-inf) = " << std::signbit(-INFINITY) << '\n';
}
```


**Output:**
```
signbit(+0.0) = false
signbit(-0.0) = true
signbit(+nan) = false
signbit(-nan) = true
signbit(+inf) = false
signbit(-inf) = true
```


## See also


| cpp/numeric/math/dsc fabs | (see dedicated page) |
| cpp/numeric/math/dsc copysign | (see dedicated page) |

