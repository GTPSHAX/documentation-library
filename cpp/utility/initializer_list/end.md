---
title: std::initializer_list::end
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/initializer_list/end
---

ddcla|since=c++11|constexpr=c++14|
const T* end() const noexcept;
Obtains a pointer to one past the last element in the initializer list, i.e. .
If the initializer list is empty, the values of  and `end()` are unspecified, but will be identical.

## Return value

A pointer to one past the last element in the initializer list

## Complexity

Constant

## Example


### Example

```cpp
#include <initializer_list>
#include <iostream>
#include <numeric>

int main()
{
    static constexpr auto l = {1, 13, 1, 13, 1};
    static_assert(std::accumulate(l.begin(), l.end(), 13) == 42);

    std::initializer_list e = {2, 7, 1, 8, 2, 8, 1};
    std::cout << std::accumulate(std::begin(e), std::end(e), 13) << '\n';
}
```


**Output:**
```
42
```


## See also


| cpp/utility/initializer_list/dsc begin | (see dedicated page) |

