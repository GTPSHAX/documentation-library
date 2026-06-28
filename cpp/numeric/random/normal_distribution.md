---
title: std::normal_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/normal_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class normal_distribution;
Generates random numbers according to the [Normal distribution|Normal (or Gaussian) random number distribution](https://en.wikipedia.org/wiki/Normal distribution|Normal (or Gaussian) random number distribution). It is defined as:
: mathjax-or|1=\(\small{f(x;\mu,\sigma)}=\frac{1}{\sigma\sqrt{2\pi} }\exp{(-\frac{1}{2}{(\frac{x-\mu}{\sigma})}^2)}\)|2=f(x; μ,σ) =  exp
Here  is the [Mean](https://en.wikipedia.org/wiki/Mean) and  is the [Standard deviation](https://en.wikipedia.org/wiki/Standard deviation) (''stddev'').
satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|normal_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|normal_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|normal_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|normal_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|normal_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|normal_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|normal_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|normal_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|normal_distribution | (see dedicated page) |


## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <random>
#include <string>

int main()
{
    std::random_device rd{};
    std::mt19937 gen{rd()};

    // Values near the mean are the most likely. Standard deviation
    // affects the dispersion of generated values from the mean.
    std::normal_distribution d{5.0, 2.0};

    // Draw a sample from the normal distribution and round it to an integer.
    auto random_int = [&d, &gen]{ return std::lround(d(gen)); };

    std::map<long, unsigned> histogram{};
    for (auto n{10000}; n; --n)
        ++histogram[random_int()];

    for (const auto [k, v] : histogram)
        std::cout << std::setw(2) << k << ' ' << std::string(v / 200, '*') << '\n';
}
```


**Output:**
```
-1
 0
 1 *
 2 ***
 3 *****
 4 ********
 5 *********
 6 *********
 7 ******
 8 ***
 9 *
10
11
```


## External links

