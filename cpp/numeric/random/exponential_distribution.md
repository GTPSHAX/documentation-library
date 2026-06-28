---
title: std::exponential_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/exponential_distribution
---

ddcl|header=random|since=c++11|1=
template< class RealType = double >
class exponential_distribution;
Produces random non-negative floating-point values , distributed according to probability density function:
:\lambda) = \lambda e^{-\lambda x}\)|2=P(x|λ) = λe
The value obtained is the time/distance until the next random event if random events occur at constant rate  per unit of time/distance. For example, this distribution describes the time between the clicks of a Geiger counter or the distance between point mutations in a DNA strand.
This is the continuous counterpart of `std::geometric_distribution`.
`std::exponential_distribution` satisfies *RandomNumberDistribution*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/numeric/random/distribution/dsc constructor|exponential_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc reset|exponential_distribution | (see dedicated page) |

#### Generation

| cpp/numeric/random/distribution/dsc operator()|exponential_distribution | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/exponential_distribution/dsc lambda | (see dedicated page) |
| cpp/numeric/random/distribution/dsc param|exponential_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc min|exponential_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc max|exponential_distribution | (see dedicated page) |


## Non-member functions


| cpp/numeric/random/distribution/dsc operator_cmp|exponential_distribution | (see dedicated page) |
| cpp/numeric/random/distribution/dsc operator_ltltgtgt|exponential_distribution | (see dedicated page) |


## Notes

Some implementations may occasionally return infinity if `RealType` is `float`. This is .

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

    // if particles decay once per second on average,
    // how much time, in seconds, until the next one?
    std::exponential_distribution<> d(1);

    std::map<int, int> hist;
    for (int n = 0; n != 10000; ++n)
        ++hist[2 * d(gen)];

    for (auto const& [x, y] : hist)
        std::cout << std::fixed << std::setprecision(1)
                  << x / 2.0 << '-' << (x + 1) / 2.0 << ' '
                  << std::string(y / 200, '*') << '\n';
}
```


**Output:**
```
0.0-0.5 *******************
0.5-1.0 ***********
1.0-1.5 *******
1.5-2.0 ****
2.0-2.5 **
2.5-3.0 *
3.0-3.5
3.5-4.0
```


## External links

