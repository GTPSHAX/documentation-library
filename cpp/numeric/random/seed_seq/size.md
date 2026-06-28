---
title: std::seed_seq::size
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/seed_seq/size
---

ddcl|since=c++11|
std::size_t size() const noexcept;
Returns the size of the underlying seed sequence.

## Return value


## Complexity

Constant time.

## Example


### Example

```cpp
#include <iostream>
#include <random>

int main()
{
    std::seed_seq s1 = {-1, 0, 1};
    std::cout << s1.size() << '\n';
}
```


**Output:**
```
3
```


## Defect report

