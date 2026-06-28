---
title: std::negative_binomial_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/negative_binomial_distribution
---

ddcl|header=random|since=c++11|1=
template< class IntType = int >
class negative_binomial_distribution;
Produces random non-negative integer values $i$, distributed according to discrete probability function:
:k, p) = \binom{k + i - 1}{i} \cdot p^k \cdot (1 - p)^i\)|2=P(i|k,p) = · p · (1 − p)
The value represents the number of failures in a series of independent yes/no trials (each succeeds with probability $p$), before exactly $k$ successes occur.
`std::negative_binomial_distribution` satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|negative_binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|negative_binomial_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|negative_binomial_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|negative_binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|negative_binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|negative_binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|negative_binomial_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|negative_binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|negative_binomial_distribution | (see dedicated page) |


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
    // Pat goes door-to-door selling cookies
    // At each house, there's a 75% chance that she sells one box
    // how many times will she be turned away before selling 5 boxes?
    std::negative_binomial_distribution<> d(5, 0.75);

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[d(gen)];

    for (auto [x, y] : hist)
        std::cout << std::hex << x << ' ' << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
0 ***********************
1 *****************************
2 **********************
3 *************
4 ******
5 ***
6 *
7
8
9
a
b
```


## External links

