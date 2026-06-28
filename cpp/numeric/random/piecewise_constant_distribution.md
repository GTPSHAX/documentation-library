---
title: std::piecewise_constant_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/piecewise_constant_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class piecewise_constant_distribution;
`std::piecewise_constant_distribution` produces random floating-point numbers, which are uniformly distributed within each of the several subintervals $[b, each with its own weight $w. The set of interval boundaries and the set of weights are the parameters of this distribution.
The probability density for any $b is $, where $S$ is the sum of all weights.
satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|piecewise_constant_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|piecewise_constant_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|piecewise_constant_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/piecewise_constant_distribution/dsc params | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|piecewise_constant_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|piecewise_constant_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|piecewise_constant_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|piecewise_constant_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|piecewise_constant_distribution | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <map>
#include <random>
#include <string>

int main()
{
    std::random_device rd;
    std::mt19937 gen(rd());
    // 50% of the time, generate a random number between 0 and 1
    // 50% of the time, generate a random number between 10 and 15
    std::vector<double> i {0, 1, 10, 15};
    std::vector<double> w {1, 0, 1};
    std::piecewise_constant_distribution<> d(i.begin(), i.end(), w.begin());

    std::map<int, int> hist;
    for (int n {}; n < 1e4; ++n)
        ++hist[d(gen)];

    for (std::cout << std::hex << std::uppercase; auto [x, y] : hist)
        std::cout << x << ' ' << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
0 **************************************************
A **********
B *********
C *********
D **********
E *********
```


## References

