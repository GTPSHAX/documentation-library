---
title: std::numeric_limits::denorm_min
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/denorm_min
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static T denorm_min() throw();
|dcl2=
static constexpr T denorm_min() noexcept;
```

Returns the minimum positive subnormal value of the type `T`, if `1=std::numeric_limits<T>::has_denorm != std::denorm_absent`, otherwise returns `std::numeric_limits<T>::min()` for floating point types and `T()` for all other types. Only meaningful for floating-point types.

## Return value


| dsc | `float`             | `FLT_TRUE_MIN` (} if<br>`std::numeric_limits<float>::is_iec559` is `true`) | |
| dsc | `double`            | `DBL_TRUE_MIN` (} if<br>`std::numeric_limits<double>::is_iec559` is `true`) | |


## Example


### Example

```cpp
#include <cassert>
#include <cstdint>
#include <cstring>
#include <iostream>
#include <limits>

int main()
{
    // the smallest subnormal value has sign bit = 0, exponent = 0
    // and only the least significant bit of the fraction is 1
    std::uint32_t denorm_bits = 0x0001;
    float denorm_float;
    std::memcpy(&denorm_float, &denorm_bits, sizeof(float));

    assert(denorm_float == std::numeric_limits<float>::denorm_min());

    std::cout << "float\tmin()\t\tdenorm_min()\n";
    std::cout << "\t" << std::numeric_limits<float>::min() << '\t';
    std::cout <<         std::numeric_limits<float>::denorm_min() << '\n';

    std::cout << "double\tmin()\t\tdenorm_min()\n";
    std::cout << "\t" << std::numeric_limits<double>::min() << '\t';
    std::cout <<         std::numeric_limits<double>::denorm_min() << '\n';
}
```


**Output:**
```
float	min()		denorm_min()
	1.17549e-38	1.4013e-45
double	min()		denorm_min()
	2.22507e-308	4.94066e-324
```


## See also


| cpp/types/numeric_limits/dsc min | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_denorm | (see dedicated page) |
| cpp/types/numeric_limits/dsc lowest | (see dedicated page) |

