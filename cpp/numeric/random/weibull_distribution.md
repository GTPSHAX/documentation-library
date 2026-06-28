---
title: std::weibull_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/weibull_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class weibull_distribution;
The `weibull_distribution` meets the requirements of a *RandomNumberDistribution* and produces random numbers according to the [Weibull distribution](https://en.wikipedia.org/wiki/Weibull distribution):
:mathjax-or
|1=\(\small{f(x;a,b)=\frac{a}{b} \cdot {(\frac{x}{b})}^{a-1} \cdot \exp{(-(\frac{a}{b})^{a})} }\)
|2=f(x;a,b) =  ·  · exp
$a$ is the [shape parameter](https://en.wikipedia.org/wiki/shape parameter) and $b$ the [scale parameter](https://en.wikipedia.org/wiki/scale parameter).
satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|weibull_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|weibull_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|weibull_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|weibull_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|weibull_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|weibull_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|weibull_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|weibull_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|weibull_distribution | (see dedicated page) |


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
    std::random_device rd;
    std::mt19937 gen(rd());

    std::weibull_distribution<> d;

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[std::round(d(gen))];

    std::cout << std::fixed << std::setprecision(1) << std::hex;
    for (auto [x, y] : hist)
        std::cout << x << ' ' << std::string(y / 200, '*') << '\n';
}
```


**Output:**
```
0 *******************
1 *******************
2 ******
3 **
4
5
6
7
8
```


## External links

