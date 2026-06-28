---
title: std::numeric_limits::max_exponent10
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/max_exponent10
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const int max_exponent10;
|dcl2=
static constexpr int max_exponent10;
```

The value of `std::numeric_limits<T>::max_exponent10` is the largest positive number `n` such that  is a representable finite value of the floating-point type `T`.

## Standard specializations


## Example


### Example

```cpp
#include <iostream>
#include <limits>

int main()
{
    std::cout << "max() = " << std::numeric_limits<float>::max() << '\n'
              << "max_exponent10 = " << std::numeric_limits<float>::max_exponent10 << '\n'
              << std::hexfloat << '\n'
              << "max() = " << std::numeric_limits<float>::max() << '\n'
              << "max_exponent = " << std::numeric_limits<float>::max_exponent << '\n';
}
```


**Output:**
```
max() = 3.40282e+38
max_exponent10 = 38

max() = 0x1.fffffep+127
max_exponent = 128
```


## See also


| cpp/types/numeric_limits/dsc max_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent10 | (see dedicated page) |

