---
title: std::gamma_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/gamma_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class gamma_distribution;
Produces random positive floating-point values $x$, distributed according to probability density function:
:mathjax-or|1=\(\mathsf{p}(x\mid\alpha,\beta) = \frac{e^{-x/\beta} }{\beta^\alpha\cdot\Gamma(\alpha)}\cdot x^{\alpha-1} \)|2=P(x|α,β)   · x
where $α$ is known as the ''shape'' parameter and $β$ is known as the ''scale'' parameter. The shape parameter is sometimes denoted by the letter $k$ and the scale parameter is sometimes denoted by the letter $θ$.
For floating-point $α$, the value obtained is the sum of $α$ independent exponentially distributed random variables, each of which has a mean of $β$.
`std::gamma_distribution` satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|gamma_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|gamma_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|gamma_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|gamma_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|gamma_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|gamma_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|gamma_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|gamma_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|gamma_distribution | (see dedicated page) |


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
    std::mt19937 gen(rd());

    // A gamma distribution with alpha = 1, and beta = 2
    // approximates an exponential distribution.
    std::gamma_distribution<> d(1, 2);

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[2 * d(gen)];

    for (auto const& [x, y] : hist)
        if (y / 100.0 > 0.5)
            std::cout << std::fixed << std::setprecision(1)
                      << x / 2.0 << '-' << (x + 1) / 2.0 << ' '
                      << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
0.0-0.5 **********************
0.5-1.0 ****************
1.0-1.5 *************
1.5-2.0 **********
2.0-2.5 ********
2.5-3.0 ******
3.0-3.5 *****
3.5-4.0 ****
4.0-4.5 ***
4.5-5.0 **
5.0-5.5 **
5.5-6.0 *
6.0-6.5 *
6.5-7.0
7.0-7.5
7.5-8.0
```


## External links

