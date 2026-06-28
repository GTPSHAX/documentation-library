---
title: std::sin(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/sin
---


# sinsmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> sin( const valarray<T>& va );
For each element in `va` computes sine of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing sine of the values in `va`.

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
    std::valarray<double> v1 = {0, 0.25, 0.5, 0.75, 1};
    std::valarray<double> v2 = std::sin(v1 * std::numbers::pi);

    for (double n : v2)
        std::cout << std::fixed << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
0.000000 0.707107 1.000000 0.707107 0.000000
```


## See also


| cpp/numeric/valarray/dsc cos | (see dedicated page) |
| cpp/numeric/valarray/dsc tan | (see dedicated page) |
| cpp/numeric/valarray/dsc asin | (see dedicated page) |
| cpp/numeric/math/dsc sin | (see dedicated page) |
| cpp/numeric/complex/dsc sin | (see dedicated page) |

