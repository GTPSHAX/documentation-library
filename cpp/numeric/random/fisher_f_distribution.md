---
title: std::fisher_f_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/fisher_f_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class fisher_f_distribution;
Produces random numbers according to the [F-distribution](https://en.wikipedia.org/wiki/F-distribution):
:mathjax-or|1=\(P(x;m,n)=\frac{\Gamma{(\frac{m+n}{2})} }{\Gamma{(\frac{m}{2})}\Gamma{(\frac{n}{2})} }{(\frac{m}{n})}^{\frac{m}{2} }x^{\frac{m}{2}-1}{(1+\frac{m}{n}x)}^{-\frac{m+n}{2} }\)|2=P(x;m,n) =  (m/n) x (1+)
and  are the [degrees of freedom (statistics)|degrees of freedom](https://en.wikipedia.org/wiki/degrees of freedom (statistics)|degrees of freedom).
satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|fisher_f_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|fisher_f_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|fisher_f_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|fisher_f_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|fisher_f_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|fisher_f_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|fisher_f_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|fisher_f_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|fisher_f_distribution | (see dedicated page) |


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
auto fisher = [&gen](const float d1, const float d2)
{
std::fisher_f_distribution<float> d{d1 /* m */, d2 /* n */};
const int norm = 1'00'00;
const float cutoff = 0.002f;
std::map<int, int> hist{};
for (int n = 0; n != norm; ++n)
++hist[std::round(d(gen))];
std::vector<float> bars;
std::vector<int> indices;
for (auto const& [n, p] : hist)
if (float x = p * (1.0 / norm); cutoff < x)
{
bars.push_back(x);
indices.push_back(n);
}
std::cout << "d₁ = " << d1 << ", d₂ = " << d2 << ":\n";
for (draw_vbars<4, 3>(bars); int n : indices)
std::cout << std::setw(2) << n << "  ";
std::cout << "\n\n";
};
fisher(/* d₁ = */ 1.0f, /* d₂ = */ 5.0f);
fisher(/* d₁ = */ 15.0f, /* d₂ = */ 10.f);
fisher(/* d₁ = */ 100.0f, /* d₂ = */ 3.0f);
}
|p=true
|output=<nowiki/>
d₁ = 1, d₂ = 5:
███                                                     ┬ 0.4956
███                                                     │
███ ▇▇▇                                                 │
███ ███ ▇▇▇ ▄▄▄ ▂▂▂ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0021
0   1   2   3   4   5   6   7   8   9  10  11  12  14
d₁ = 15, d₂ = 10:
███                     ┬ 0.6252
███                     │
███ ▂▂▂                 │
▆▆▆ ███ ███ ▃▃▃ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0023
0   1   2   3   4   5   6
d₁ = 100, d₂ = 3:
███                                                             ┬ 0.4589
███                                                             │
▁▁▁ ███ ▅▅▅                                                         │
███ ███ ███ ▆▆▆ ▃▃▃ ▂▂▂ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0021
0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16

## External links

