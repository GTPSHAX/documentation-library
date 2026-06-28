---
title: std::chi_squared_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/chi_squared_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class chi_squared_distribution;
The `chi_squared_distribution` produces random numbers  according to the [Chi-squared distribution](https://en.wikipedia.org/wiki/Chi-squared distribution):
:mathjax-or|1=\({\small f(x;n) = }\frac{x^{(n/2)-1}\exp{(-x/2)} }{\Gamma{(n/2)}2^{n/2} }\)|2=f(x;n) =
is the [Gamma function](https://en.wikipedia.org/wiki/Gamma function) (See also `std::tgamma`) and  are the [Degrees_of_freedom_(statistics)|degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)|degrees of freedom) (default 1).
satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|chi_squared_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|chi_squared_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|chi_squared_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/chi_squared_distribution/dsc n | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|chi_squared_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|chi_squared_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|chi_squared_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|chi_squared_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|chi_squared_distribution | (see dedicated page) |


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
auto χ2 = [&gen](const float dof)
{
std::chi_squared_distribution<float> d{dof /* n */};
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
std::cout << "dof = " << dof << ":\n";
for (draw_vbars<4, 3>(bars); int n : indices)
std::cout << std::setw(2) << n << "  ";
std::cout << "\n\n";
};
for (float dof : {1.f, 2.f, 3.f, 4.f, 6.f, 9.f})
χ2(dof);
}
|p=true
|output=<nowiki/>
dof = 1:
███                                 ┬ 0.5271
███                                 │
███ ███                             │
███ ███ ▇▇▇ ▃▃▃ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.003
0   1   2   3   4   5   6   7   8
dof = 2:
███                                     ┬ 0.3169
▆▆▆ ███ ▃▃▃                                 │
███ ███ ███ ▄▄▄                             │
███ ███ ███ ███ ▇▇▇ ▄▄▄ ▃▃▃ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.004
0   1   2   3   4   5   6   7   8   9  10
dof = 3:
███ ▃▃▃                                         ┬ 0.2439
███ ███ ▄▄▄                                     │
▃▃▃ ███ ███ ███ ▇▇▇ ▁▁▁                             │
███ ███ ███ ███ ███ ███ ▆▆▆ ▄▄▄ ▃▃▃ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0033
0   1   2   3   4   5   6   7   8   9  10  11  12
dof = 4:
▂▂▂ ███ ▃▃▃                                                 ┬ 0.1864
███ ███ ███ ███ ▂▂▂                                         │
███ ███ ███ ███ ███ ▅▅▅ ▁▁▁                                 │
▅▅▅ ███ ███ ███ ███ ███ ███ ███ ▆▆▆ ▄▄▄ ▃▃▃ ▂▂▂ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0026
0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
dof = 6:
▅▅▅ ▇▇▇ ███ ▂▂▂                                                 ┬ 0.1351
▅▅▅ ███ ███ ███ ███ ▇▇▇ ▁▁▁                                         │
▁▁▁ ███ ███ ███ ███ ███ ███ ███ ▅▅▅ ▂▂▂                                 │
▁▁▁ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ▅▅▅ ▄▄▄ ▃▃▃ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0031
0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
dof = 9:
▅▅▅ ▇▇▇ ███ ███ ▄▄▄ ▂▂▂                                                 ┬ 0.1044
▃▃▃ ███ ███ ███ ███ ███ ███ ▅▅▅ ▁▁▁                                         │
▄▄▄ ███ ███ ███ ███ ███ ███ ███ ███ ███ ▆▆▆ ▃▃▃                                 │
▄▄▄ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ███ ▆▆▆ ▄▄▄ ▃▃▃ ▂▂▂ ▁▁▁ ▁▁▁ ▁▁▁ ┴ 0.0034
2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22

## External links

