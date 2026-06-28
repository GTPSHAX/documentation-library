---
title: std::random_device
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/random_device
---

ddcl|header=random|since=c++11|1=
class random_device;
`std::random_device` is a uniformly-distributed integer random number generator that produces non-deterministic random numbers.
`std::random_device` may be implemented in terms of an implementation-defined pseudo-random number engine if a non-deterministic source (e.g. a hardware device) is not available to the implementation. In this case each  object may generate the same number sequence.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


#### Construction

| cpp/numeric/random/engine/dsc constructor|random_device | (see dedicated page) |

#### Generation

| cpp/numeric/random/engine/dsc operator()|random_device | (see dedicated page) |

#### Characteristics

| cpp/numeric/random/random_device/dsc entropy | (see dedicated page) |
| cpp/numeric/random/engine/dsc min|random_device | (see dedicated page) |
| cpp/numeric/random/engine/dsc max|random_device | (see dedicated page) |


## Notes

A notable implementation where  is deterministic in old versions of MinGW-w64 ([https://sourceforge.net/p/mingw-w64/bugs/338/ bug 338], fixed since GCC 9.2). The latest MinGW-w64 versions can be downloaded from [https://gcc-mcf.lhmouse.com/ GCC with the MCF thread model].

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
    std::map<int, int> hist;
    std::uniform_int_distribution<int> dist(0, 9);

    for (int n = 0; n != 20000; ++n)
        ++hist[dist(rd)]; // note: demo only: the performance of many
                          // implementations of random_device degrades sharply
                          // once the entropy pool is exhausted. For practical use
                          // random_device is generally only used to seed
                          // a PRNG such as mt19937

    for (auto [x, y] : hist)
        std::cout << x << " : " << std::string(y / 100, '*') << '\n';
}
```


**Output:**
```
0 : ********************
1 : *******************
2 : ********************
3 : ********************
4 : ********************
5 : *******************
6 : ********************
7 : ********************
8 : *******************
9 : ********************
```

