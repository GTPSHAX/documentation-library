---
title: std::initializer_list::size
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/initializer_list/size
---

ddcla|since=c++11|constexpr=c++14|
size_type size() const noexcept;
Obtains the number of elements in the initializer list.

## Return value

`std::distance(begin(), end())`

## Complexity

Constant

## Example


### Example

```cpp
#include <initializer_list>

static_assert(std::initializer_list{1, 2, 3}.size() == 3);

int main() {}
```

