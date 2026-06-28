---
title: std::bernoulli_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/bernoulli_distribution
---

ddcl|header=random|since=c++11|1=
class bernoulli_distribution;
Produces random boolean values, according to the discrete probability function. The probability of  is
:$1=P(b
`std::bernoulli_distribution` satisfies *RandomNumberDistribution*.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|bernoulli_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|bernoulli_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|bernoulli_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/bernoulli_distribution/dsc p | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|bernoulli_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|bernoulli_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|bernoulli_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|bernoulli_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|bernoulli_distribution | (see dedicated page) |


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
    // give "true" 1/4 of the time
    // give "false" 3/4 of the time
    std::bernoulli_distribution d(0.25);

    std::map<bool, int> hist;
    for (int n = 0; n < 10000; ++n)
        ++hist[d(gen)];

    std::cout << std::boolalpha;
    for (auto const& [key, value] : hist)
        std::cout << std::setw(5) << key << ' '
                  << std::string(value / 500, '*') << '\n';
}
```


**Output:**
```
false ***************
 true ****
```


## External links

