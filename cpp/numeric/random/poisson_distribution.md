---
title: std::poisson_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/poisson_distribution
---

ddcl|header=random|since=c++11|1=
template< class IntType = int >
class poisson_distribution;
Produces random non-negative integer values $i$, distributed according to discrete probability function:
: \mu) = \frac{e^{-\mu}\mu^i}{i!}\)|2=P(i|μ) =
The value obtained is the probability of exactly $i$ occurrences of a random event if the expected, ''mean'' number of its occurrence under the same conditions (on the same time/space interval) is $μ$.
`std::poisson_distribution` satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|poisson_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|poisson_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|poisson_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/poisson_distribution/dsc mean | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|poisson_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|poisson_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|poisson_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|poisson_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|poisson_distribution | (see dedicated page) |


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

    // If an event occurs 4 times a minute on average, how
    // often is it that it occurs n times in one minute?
    std::poisson_distribution<> d(4);

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[d(gen)];

    for (auto [x, y] : hist)
        std::cout << std::hex << x << ' '
                  << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
0 *
1 *******
2 **************
3 *******************
4 *******************
5 ***************
6 **********
7 *****
8 **
9 *
a
b
c
d
```


## External links

