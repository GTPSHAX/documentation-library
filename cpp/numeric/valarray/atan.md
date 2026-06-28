---
title: std::atan(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/atan
---


# atansmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> atan( const valarray<T>& va );
For each element in `va` computes arc tangent of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing arc tangents of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <valarray>

auto show = [](char const* title, const std::valarray<float>& va)
{
    std::cout << title << " :";
    std::for_each(std::begin(va), std::end(va), 
        [](const float x) { std::cout << "  " << std::fixed << x; });
    std::cout << '\n';
};

int main()
{
    const std::valarray<float> x = {.1f, .3f, .6f, .9f};
    const std::valarray<float> f = std::atan(x);
    const std::valarray<float> g = std::tan(f);

    show("x          ", x);
    show("f = atan(x)", f);
    show("g = tan(f) ", g);
}
```


**Output:**
```
x           :  0.100000  0.300000  0.600000  0.900000
f = atan(x) :  0.099669  0.291457  0.540420  0.732815
g = tan(f)  :  0.100000  0.300000  0.600000  0.900000
```


## See also


| cpp/numeric/valarray/dsc asin | (see dedicated page) |
| cpp/numeric/valarray/dsc acos | (see dedicated page) |
| cpp/numeric/valarray/dsc atan2 | (see dedicated page) |
| cpp/numeric/valarray/dsc tan | (see dedicated page) |
| cpp/numeric/math/dsc atan | (see dedicated page) |
| cpp/numeric/complex/dsc atan | (see dedicated page) |

