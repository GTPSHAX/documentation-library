---
title: std::sinh(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/sinh
---


# sinhsmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> sinh( const valarray<T>& va );
For each element in `va` computes hyperbolic sine of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing hyperbolic sine of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iomanip>
#include <iostream>
#include <valarray>

template<typename T>
void show(char const* title, const std::valarray<T>& va)
{
    std::cout << title << " : " << std::right;
    for (T x : va)
        std::cout << std::fixed << x << ' ';
    std::cout << '\n';
}

template<typename T>
void sinh_for(std::valarray<T> const& z)
{
    // Hyperbolic sine is sinh(z) = (eᶻ - e⁻ᶻ) / 2.

    const std::valarray<T> sinh_z{std::sinh(z)};
    const std::valarray<T> e_z{std::exp(z)};
    const std::valarray<T> e_neg_z{std::exp(-z)};
    const std::valarray<T> sinh_def{(e_z - e_neg_z) / 2.0f};

    show("n         ", z);
    show("sinh(n)   ", sinh_z);
    show("(eⁿ-e⁻ⁿ)/2", sinh_def);

    std::cout.put('\n');
}

int main()
{
    sinh_for(std::valarray<float>{-.2f, -.1f, 0.f, .1f, .2f, INFINITY});
    sinh_for(std::valarray<std::complex<double>>{<!---->{-.2,-.1}, {.2,.1}<!---->});
}
```


**Output:**
```
n          : -0.200000 -0.100000 0.000000 0.100000 0.200000 inf 
sinh(n)    : -0.201336 -0.100167 0.000000 0.100167 0.201336 inf 
(eⁿ-e⁻ⁿ)/2 : -0.201336 -0.100167 0.000000 0.100167 0.201336 inf 

n          : (-0.200000,-0.100000) (0.200000,0.100000) 
sinh(n)    : (-0.200330,-0.101837) (0.200330,0.101837) 
(eⁿ-e⁻ⁿ)/2 : (-0.200330,-0.101837) (0.200330,0.101837)
```


## See also


| cpp/numeric/valarray/dsc cosh | (see dedicated page) |
| cpp/numeric/valarray/dsc tanh | (see dedicated page) |
| cpp/numeric/math/dsc sinh | (see dedicated page) |
| cpp/numeric/complex/dsc sinh | (see dedicated page) |

