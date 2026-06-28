---
title: std::geometric_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/geometric_distribution
---

ddcl|header=random|since=c++11|1=
template< class IntType = int >
class geometric_distribution;
Produces random non-negative integer values $i$, distributed according to discrete probability function:
:p) = p \cdot (1-p)^i\)|2=P(i|p) = p · (1 − p)
The value represents the number of failures in a series of independent yes/no trials (each succeeds with probability p), before exactly 1 success occurs.
`std::geometric_distribution<>(p)` is exactly equivalent to `std::negative_binomial_distribution<>(1, p)`. It is also the discrete counterpart of `std::exponential_distribution`.
`std::geometric_distribution` satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|geometric_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|geometric_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|geometric_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/geometric_distribution/dsc p | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|geometric_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|geometric_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|geometric_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|geometric_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|geometric_distribution | (see dedicated page) |


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

    std::geometric_distribution<> d;
        // same as 
        // std::negative_binomial_distribution<> d(1, 0.5):

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[d(gen)];

    for (auto [x, y] : hist)
    {
        const char c = x < 10 ? x + '0' : x - 10 + 'a';
        std::cout << c << ' ' << std::string(y / 100, '*') << '\n';
    }
}
```


**Output:**
```
0 *************************************************
1 *************************
2 ************
3 ******
4 **
5 *
6
7
8
9
```


## External links

