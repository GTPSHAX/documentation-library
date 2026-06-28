---
title: std::extreme_value_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/extreme_value_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class extreme_value_distribution;
Produces random numbers according to the [Generalized extreme value distribution](https://en.wikipedia.org/wiki/Generalized extreme value distribution) (it is also known as Gumbel Type I, log-Weibull, Fisher-Tippett Type I):
:mathjax-or|1=\({\small p(x;a,b) = \frac{1}{b} \exp{(\frac{a-x}{b}-\exp{(\frac{a-x}{b})})} }\)|2=p(x;a,b) =  exp
`std::extreme_value_distribution` satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|extreme_value_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|extreme_value_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|extreme_value_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|extreme_value_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|extreme_value_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|extreme_value_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|extreme_value_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|extreme_value_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|extreme_value_distribution | (see dedicated page) |


## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <random>
#include <vector>

{{cpp/numeric/draw_vbars
```

int main()
{
std::random_device rd{};
std::mt19937 gen{rd()};
std::extreme_value_distribution<> d{-1.618f, 1.618f};
const int norm = 10'000;
const float cutoff = 0.000'3f;
std::map<int, int> hist{};
for (int n = 0; n != norm; ++n)
++hist[std::round(d(gen))];
std::vector<float> bars;
std::vector<int> indices;
for (const auto& [n, p] : hist)
if (const float x = p * (1.0f / norm); x > cutoff)
{
bars.push_back(x);
indices.push_back(n);
}
draw_vbars<8,4>(bars);
for (int n : indices)
std::cout << ' ' << std::setw(2) << n << "  ";
std::cout << '\n';
}
|p=true
|output=<nowiki/>
████ ▅▅▅▅                                                        ┬ 0.2186
████ ████                                                        │
▁▁▁▁ ████ ████ ▇▇▇▇                                                   │
████ ████ ████ ████                                                   │
████ ████ ████ ████ ▆▆▆▆                                              │
████ ████ ████ ████ ████ ▁▁▁▁                                         │
▄▄▄▄ ████ ████ ████ ████ ████ ████ ▃▃▃▃                                    │
▁▁▁▁ ████ ████ ████ ████ ████ ████ ████ ████ ▆▆▆▆ ▃▃▃▃ ▂▂▂▂ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ▁▁▁▁ ┴ 0.0005
-5   -4   -3   -2   -1    0    1    2    3    4    5    6    7    8    9   10

## External links

