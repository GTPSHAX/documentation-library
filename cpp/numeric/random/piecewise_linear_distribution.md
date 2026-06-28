---
title: std::piecewise_linear_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/piecewise_linear_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class piecewise_linear_distribution;
`std::piecewise_linear_distribution` produces random floating-point numbers, which are distributed according to a linear probability density function within each of the several subintervals mathjax-or|\(\small{[b_i, b_{i+1})}\)|[b, b). The distribution is such that the probability density at each interval boundary is exactly the predefined value }.
The probability density for any mathjax-or|\(\small{ b_i \le x < b_{i+1} }\)|b≤x<b is mathjax-or|\(\small{p_i\frac{b_{i+1}-x}{b_{i+1}-b_i} + p_{i+1}\frac{x-b_i}{b_{i+1}-b_i} }\)| + , where probability densities at interval boundaries } are calculated as } where } is the sum of all mathjax-or|\(\small{\frac{1}{2}(w_k + w_{k+1})(b_{k+1} - b_k)}\)|(w+w)(b−b).
The set of interval boundaries } and the set of weights at boundaries } are the parameters of this distribution.
satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|piecewise_linear_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|piecewise_linear_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|piecewise_linear_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/piecewise_linear_distribution/dsc params | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|piecewise_linear_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|piecewise_linear_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|piecewise_linear_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|piecewise_linear_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|piecewise_linear_distribution | (see dedicated page) |


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <map>
#include <random>
#include <string>

int main()
{
    std::random_device rd;
    std::mt19937 gen{rd()};
    // increase the probability from 0 to 5
    // remain flat from 5 to 10
    // decrease from 10 to 15 at the same rate
    std::vector<double> i{0, 5, 10, 15};
    std::vector<double> w{0, 1, 1, 0};
    std::piecewise_linear_distribution<> d{i.begin(), i.end(), w.begin()};

    std::map<int, int> hist;
    for (int n{}; n < 1e4; ++n)
        ++hist[d(gen)];

    for (auto [x, y] : hist)
        std::cout << std::setw(2) << std::setfill('0') << x
                  << ' ' << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
00 *
01 ***
02 ****
03 ******
04 *********
05 *********
06 *********
07 **********
08 *********
09 **********
10 *********
11 *******
12 ****
13 ***
14 *
```

