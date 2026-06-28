---
title: std::tan(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/tan
---


# tansmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> tan( const valarray<T>& va );
For each element in `va` computes tangent of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing tangents of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <valarray>

auto show = [](char const* title, const std::valarray<double>& va)
{
    std::cout << title << " :";
    for (auto x : va)
        std::cout << "  " << std::fixed << x;
    std::cout << '\n';
};

int main()
{
    const std::valarray<double> x = {.0, .1, .2, .3};
    const std::valarray<double> y = std::tan(x);
    const std::valarray<double> z = std::atan(y);

    show("x          ", x);
    show("y = tan(x) ", y);
    show("z = atan(y)", z);
}
```


**Output:**
```
x           :  0.000000  0.100000  0.200000  0.300000
y = tan(x)  :  0.000000  0.100335  0.202710  0.309336
z = atan(y) :  0.000000  0.100000  0.200000  0.300000
```


## See also


| cpp/numeric/valarray/dsc sin | (see dedicated page) |
| cpp/numeric/valarray/dsc cos | (see dedicated page) |
| cpp/numeric/valarray/dsc atan | (see dedicated page) |
| cpp/numeric/math/dsc tan | (see dedicated page) |
| cpp/numeric/complex/dsc tan | (see dedicated page) |

