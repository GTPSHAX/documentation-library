---
title: std::cos(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/cos
---


# cossmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> cos( const valarray<T>& va );
For each element in `va` computes cosine of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing cosines of the values in `va`.

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
const auto sin = std::sin(x);
const auto cos = std::cos(x);
const auto z = (sin * sin) + (cos * cos);
show("x", x);
show("sin(x)", sin);
show("cos(x)", cos);
show("z", z);
}
|output=<nowiki/>
x |       0.1 |       0.2 |       0.3 |       0.4 |
sin(x) | 0.0998334 |  0.198669 |   0.29552 |  0.389418 |
cos(x) |  0.995004 |  0.980067 |  0.955337 |  0.921061 |
z |         1 |         1 |         1 |         1 |

## See also


| cpp/numeric/valarray/dsc sin | (see dedicated page) |
| cpp/numeric/valarray/dsc tan | (see dedicated page) |
| cpp/numeric/valarray/dsc acos | (see dedicated page) |
| cpp/numeric/math/dsc cos | (see dedicated page) |
| cpp/numeric/complex/dsc cos | (see dedicated page) |

