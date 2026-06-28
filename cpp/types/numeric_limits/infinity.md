---
title: std::numeric_limits::infinity
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/infinity
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static T infinity() throw();
|dcl2=
static constexpr T infinity() noexcept;
```

Returns the special value "positive infinity", as represented by the floating-point type `T`. Only meaningful if `1=std::numeric_limits<T>::has_infinity == true`. In IEEE 754, the most common binary representation of floating-point numbers, the positive infinity is the value with all bits of the exponent set and all bits of the fraction cleared.

## Return value


## Example


### Example

```cpp
#include <iostream>
#include <limits>

int main()
{
    double max = std::numeric_limits<double>::max();
    double inf = std::numeric_limits<double>::infinity();

    if (inf > max)
        std::cout << inf << " is greater than " << max << '\n';
}
```


**Output:**
```
inf is greater than 1.79769e+308
```


## See also


| cpp/types/numeric_limits/dsc has_infinity | (see dedicated page) |

