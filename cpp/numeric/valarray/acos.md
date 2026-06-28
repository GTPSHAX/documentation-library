---
title: std::acos(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/acos
---


# acossmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> acos( const valarray<T>& va );
For each element in `va` computes arc cosine of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing arc cosines of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>
#include <valarray>

int main()
{
    // take common x-values from unit circle
    const double s32 = std::sqrt(3.0) / 2.0;
    const double s22 = std::sqrt(2.0) / 2.0;
    std::valarray<double> v1 = {-1.0, -s32, -s22, -0.5, 0.0, 0.5, s22, s32, 1.0};
    std::valarray<double> v2 = std::acos(v1) * 180.0 / std::numbers::pi;

    for (double n : v2)
        std::cout << n << "° ";
    std::cout << '\n';
}
```


**Output:**
```
180° 150° 135° 120° 90° 60° 45° 30° 0°
```


## See also


| cpp/numeric/valarray/dsc asin | (see dedicated page) |
| cpp/numeric/valarray/dsc atan | (see dedicated page) |
| cpp/numeric/valarray/dsc atan2 | (see dedicated page) |
| cpp/numeric/valarray/dsc cos | (see dedicated page) |
| cpp/numeric/math/dsc acos | (see dedicated page) |
| cpp/numeric/complex/dsc acos | (see dedicated page) |

