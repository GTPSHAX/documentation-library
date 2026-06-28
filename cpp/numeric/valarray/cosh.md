---
title: std::cosh(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/cosh
---


# coshsmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> cosh( const valarray<T>& va );
For each element in `va` computes hyperbolic cosine of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing hyperbolic cosine of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>
#include <valarray>

void show(const char* title, const std::valarray<float>& data)
{
    const int w{9};
    std::cout << std::setw(w) << title << " {{!
```

for (float x : data)
std::cout << std::setw(w) << x << " | ";
std::cout << '\n';
}
int main()
{
const std::valarray<float> x{.1, .2, .3, .4};
const auto sinh = std::sinh(x);
const auto cosh = std::cosh(x);
const auto z = (cosh * cosh) - (sinh * sinh);
show("x", x);
show("sinh(x)", sinh);
show("cosh(x)", cosh);
show("z", z);
}
|output=<nowiki/>
x |       0.1 |       0.2 |       0.3 |       0.4 |
sinh(x) |  0.100167 |  0.201336 |   0.30452 |  0.410752 |
cosh(x) |     1.005 |   1.02007 |   1.04534 |   1.08107 |
z |         1 |         1 |         1 |         1 |

## See also


| cpp/numeric/valarray/dsc sinh | (see dedicated page) |
| cpp/numeric/valarray/dsc tanh | (see dedicated page) |
| cpp/numeric/math/dsc cosh | (see dedicated page) |
| cpp/numeric/complex/dsc cosh | (see dedicated page) |

