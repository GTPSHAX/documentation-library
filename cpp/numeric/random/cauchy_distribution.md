---
title: std::cauchy_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/cauchy_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class cauchy_distribution;
Produces random numbers according to a [Cauchy distribution](https://en.wikipedia.org/wiki/Cauchy distribution) (also called Lorentz distribution):
:mathjax-or|1=\({\small f(x;a,b)={(b\pi{[1+{(\frac{x-a}{b})}^{2}]} })}^{-1}\)|2=f(x; a,b) =
`std::cauchy_distribution` satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|cauchy_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|cauchy_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|cauchy_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|cauchy_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|cauchy_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|cauchy_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|cauchy_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|cauchy_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|cauchy_distribution | (see dedicated page) |


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
auto cauchy = [&gen](const float x0, const float 𝛾)
{
std::cauchy_distribution<float> d{x0 /* a */, 𝛾 /* b */};
const int norm = 1'00'00;
const float cutoff = 0.005f;
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
std::cout << "x₀ = " << x0 << ", 𝛾 = " << 𝛾 << ":\n";
draw_vbars<4,3>(bars);
for (int n : indices)
std::cout << std::setw(2) << n << "  ";
std::cout << "\n\n";
};
cauchy(/* x₀ = */ -2.0f, /* 𝛾 = */ 0.50f);
cauchy(/* x₀ = */ +0.0f, /* 𝛾 = */ 1.25f);
}
|p=true
|output=<nowiki/>
x₀ = -2, 𝛾 = 0.5:
███                     ┬ 0.5006
███                     │
▂▂▂ ███ ▁▁▁                 │
▁▁▁ ▁▁▁ ▁▁▁ ▃▃▃ ███ ███ ███ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0076
-7  -6  -5  -4  -3  -2  -1   0   1   2   3
x₀ = 0, 𝛾 = 1.25:
███                                 ┬ 0.2539
▅▅▅ ███ ▃▃▃                             │
▁▁▁ ███ ███ ███ ▁▁▁                         │
▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ▃▃▃ ▅▅▅ ███ ███ ███ ███ ███ ▅▅▅ ▃▃▃ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0058
-8  -7  -6  -5  -4  -3  -2  -1   0   1   2   3   4   5   6   7   9

## External links

