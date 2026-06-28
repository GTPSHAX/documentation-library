---
title: std::discrete_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/discrete_distribution
---

ddcl|header=random|since=c++11|1=
template< class IntType = int >
class discrete_distribution;
`std::discrete_distribution` produces random integers on the interval [0, n), where the probability of each individual integer `i` is defined as $w, that is the ''weight'' of the `i`th integer divided by the sum of all `n` weights.
`std::discrete_distribution` satisfies all requirements of *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|discrete_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|discrete_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|discrete_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/discrete_distribution/dsc probabilities | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|discrete_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|discrete_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|discrete_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|discrete_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|discrete_distribution | (see dedicated page) |


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <map>
#include <random>

int main()
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::discrete_distribution<> d({40, 10, 10, 40});
    std::map<int, int> map;

    for (int n = 0; n < 1e4; ++n)
        ++map[d(gen)];

    for (const auto& [num, count] : map)
        std::cout << num << " generated " << std::setw(4) << count << " times\n";
}
```


**Output:**
```
0 generated 4037 times
1 generated  962 times
2 generated 1030 times
3 generated 3971 times
```

