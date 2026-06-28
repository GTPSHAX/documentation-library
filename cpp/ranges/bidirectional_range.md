---
title: std::ranges::bidirectional_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/bidirectional_range
---

ddcl|header = ranges|since=c++20|1=
template< class T >
concept bidirectional_range =
ranges::forward_range<T> && std::bidirectional_iterator<ranges::iterator_t<T>>;
The `bidirectional_range` concept is a refinement of  for which `ranges::begin` returns a model of .

## Example


### Example

```cpp
#include <forward_list>
#include <list>
#include <ranges>
#include <set>
#include <unordered_set>

int main()
{
    static_assert(
            std::ranges::bidirectional_range<std::set<int>> and
        not std::ranges::bidirectional_range<std::unordered_set<int>> and
            std::ranges::bidirectional_range<std::list<int>> and
        not std::ranges::bidirectional_range<std::forward_list<int>>
    );
}
```


## See also


| cpp/ranges/dsc forward_range | (see dedicated page) |
| cpp/ranges/dsc random_access_range | (see dedicated page) |

