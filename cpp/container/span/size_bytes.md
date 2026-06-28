---
title: std::span::size_bytes
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/size_bytes
---

ddcl|since=c++20|
constexpr size_type size_bytes() const noexcept;
Returns the size of the sequence in bytes.

## Return value

`size() * sizeof(element_type)`.

## Example


### Example

```cpp
#include <cstdint>
#include <iostream>
#include <span>

constexpr static std::int32_t a[]{1, 2, 3, 4, 5};
constexpr static std::span s{a};

static_assert
(
    sizeof(int32_t) == 4 &&
    std::size(a) == 5 &&
    sizeof a == 20 &&
    s.size() == 5 &&
    s.size_bytes() == 20
);

int main()
{
    // typically, a static span holds only a pointer:
    std::cout << sizeof(s) << '\n';
}
```


**Output:**
```
8
```


## See also


| cpp/container/span/dsc size | (see dedicated page) |

