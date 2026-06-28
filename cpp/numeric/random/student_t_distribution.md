---
title: std::student_t_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/student_t_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class student_t_distribution;
Produces random floating-point values $x$, distributed according to probability density function:
:n) = \frac{1}{\sqrt{n\pi} } \cdot \frac{\Gamma(\frac{n+1}{2})}{\Gamma(\frac{n}{2})} \cdot (1+\frac{x^2}{n})^{-\frac{n+1}{2} } \)|2=p(x|n)   ·  ·
where $n$ is known as the number of ''degrees of freedom''. This distribution is used when estimating the ''mean'' of an unknown normally distributed value given $n + 1$ independent measurements, each with additive errors of unknown standard deviation, as in physical measurements. Or, alternatively, when estimating the unknown mean of a normal distribution with unknown standard deviation, given $n + 1$ samples.
satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|student_t_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|student_t_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|student_t_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/student_t_distribution/dsc n | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|student_t_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|student_t_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|student_t_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|student_t_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|student_t_distribution | (see dedicated page) |


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
std::student_t_distribution<> d{10.0f};
const int norm = 10'000;
const float cutoff = 0.000'3f;
std::map<int, int> hist{};
for (int n = 0; n != norm; ++n)
++hist[std::round(d(gen))];
std::vector<float> bars;
std::vector<int> indices;
for (const auto& [n, p] : hist)
if (float x = p * (1.0f / norm); cutoff < x)
{
bars.push_back(x);
indices.push_back(n);
}
for (draw_vbars<8, 5>(bars); const int n : indices)
std::cout << " " << std::setw(2) << n << "   ";
std::cout << '\n';
}
|p=true
|output=<nowiki/>
█████                               ┬ 0.3753
█████                               │
▁▁▁▁▁ █████                               │
█████ █████ ▆▆▆▆▆                         │
█████ █████ █████                         │
█████ █████ █████                         │
▄▄▄▄▄ █████ █████ █████ ▄▄▄▄▄                   │
▁▁▁▁▁ ▃▃▃▃▃ █████ █████ █████ █████ █████ ▃▃▃▃▃ ▁▁▁▁▁ ▁▁▁▁▁ ┴ 0.0049
-4    -3    -2    -1     0     1     2     3     4     5

## External links

