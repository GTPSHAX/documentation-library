---
title: std::numeric_limits::min_exponent10
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/min_exponent10
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const int min_exponent10;
|dcl2=
static constexpr int min_exponent10;
```

The value of `std::numeric_limits<T>::min_exponent10` is the lowest negative number `n` such that  is a valid normalized value of the floating-point type `T`.

## Standard specializations


## Example


### Example

```cpp
#include <iostream>
#include <limits>

int main()
{
    std::cout << "min() = " << std::numeric_limits<float>::min() << '\n'
              << "min_exponent10 = " << std::numeric_limits<float>::min_exponent10 << '\n'
              << std::hexfloat << '\n'
              << "min() = " << std::numeric_limits<float>::min() << '\n'
              << "min_exponent = " << std::numeric_limits<float>::min_exponent << '\n';
}
```


**Output:**
```
min() = 1.17549e-38
min_exponent10 = -37

min() = 0x1p-126
min_exponent = -125
```


## See also


| cpp/types/numeric_limits/dsc min_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent10 | (see dedicated page) |

