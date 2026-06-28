---
title: std::binomial_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/binomial_distribution
---

ddcl|header=random|since=c++11|1=
template< class IntType = int >
class binomial_distribution;
Produces random non-negative integer values $i$, distributed according to discrete probability function:
:t,p) = \binom{t}{i} \cdot p^i \cdot (1-p)^{t-i}\)|2=P(i|t,p)  · p · (1 − p)
The value obtained is the number of successes in a sequence of $t$ yes/no experiments, each of which succeeds with probability $p$.
`std::binomial_distribution` satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|binomial_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|binomial_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/distribution/dsc params|binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|binomial_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|binomial_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|binomial_distribution | (see dedicated page) |


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
    // perform 4 trials, each succeeds 1 in 2 times
    std::binomial_distribution<> d(4, 0.5);

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[d(gen)];

    for (auto const& [x, y] : hist)
        std::cout << x << ' ' << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
0 ******
1 ************************
2 *************************************
3 *************************
4 ******
```


## External links

