---
title: std::seed_seq
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/seed_seq
---

ddcl|header=random|since=c++11|
class seed_seq;
`std::seed_seq` consumes a sequence of integer-valued data and produces a requested number of 32-bit unsigned integer values, based on the consumed data. The produced values are distributed over the entire 32-bit range even if the consumed values are close.
It provides a way to seed a large number of random number engines or to seed a generator that requires a lot of entropy, given a small seed or a poorly distributed initial seed sequence.
meets the requirements of *SeedSequence*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


## Example


### Example

```cpp
#include <cstdint>
#include <iostream>
#include <random>

int main()
{
    std::seed_seq seq{1, 2, 3, 4, 5};
    std::vector<std::uint32_t> seeds(10);
    seq.generate(seeds.begin(), seeds.end());
    for (std::uint32_t n : seeds)
        std::cout << n << '\n';
}
```


**Output:**
```
4204997637
4246533866
1856049002
1129615051
690460811
1075771511
46783058
3904109078
1534123438
1495905678
```

