---
title: std::vector::flip
type: Containers
source: https://en.cppreference.com/w/cpp/container/vector_bool/flip
---

ddcla|header=vector|constexpr=c++20|
void flip();
Toggles each `bool` (replaces with its opposite value) in the `vector`.

## Example


### Example

```cpp
#include <iostream>
#include <vector>

void print(const std::vector<bool>& vb)
{
    for (const bool b : vb)
        std::cout << b;
    std::cout << '\n';
}

int main()
{
    std::vector<bool> v{0, 1, 0, 1};
    print(v);
    v.flip();
    print(v);
}
```


**Output:**
```
0101
1010
```


## See also


| cpp/container/dsc operator_at|vector | (see dedicated page) |
| cpp/utility/bitset/dsc flip | (see dedicated page) |

