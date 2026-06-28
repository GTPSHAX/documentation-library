---
title: std::tanh(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/tanh
---


# tanhsmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> tanh( const valarray<T>& va );
For each element in `va` computes hyperbolic tangent of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing hyperbolic tangent of the values in `va`.

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
    const std::valarray<double> sinh = std::sinh(x);
    const std::valarray<double> cosh = std::cosh(x);
    const std::valarray<double> tanh = std::tanh(x);
    const std::valarray<double> tanh_by_def = sinh / cosh;
    const std::valarray<double> tanh_2x = std::tanh(2.0 * x);
    const std::valarray<double> tanh_2x_by_def = 
        (2.0 * tanh) / (1.0 + std::pow(tanh, 2.0));

    show("x              ", x);
    show("tanh(x)        ", tanh);
    show("tanh(x) (def)  ", tanh_by_def);
    show("tanh(2*x)      ", tanh_2x);
    show("tanh(2*x) (def)", tanh_2x_by_def);
}
```


**Output:**
```
x               :  0.000000  0.100000  0.200000  0.300000
tanh(x)         :  0.000000  0.099668  0.197375  0.291313
tanh(x) (def)   :  0.000000  0.099668  0.197375  0.291313
tanh(2*x)       :  0.000000  0.197375  0.379949  0.537050
tanh(2*x) (def) :  0.000000  0.197375  0.379949  0.537050
```


## See also


| cpp/numeric/valarray/dsc sinh | (see dedicated page) |
| cpp/numeric/valarray/dsc cosh | (see dedicated page) |
| cpp/numeric/math/dsc tanh | (see dedicated page) |
| cpp/numeric/complex/dsc tanh | (see dedicated page) |

