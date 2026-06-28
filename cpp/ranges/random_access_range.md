---
title: std::ranges::random_access_range
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/random_access_range
---

ddcl|header = ranges|since=c++20|1=
template< class T >
concept random_access_range =
ranges::bidirectional_range<T> && std::random_access_iterator<ranges::iterator_t<T>>;
The `random_access_range` concept is a refinement of  for which `ranges::begin` returns a model of .

## Example


### Example

```cpp
#include <array>
#include <deque>
#include <list>
#include <ranges>
#include <set>
#include <valarray>
#include <vector>

template<typename T> concept RAR = std::ranges::random_access_range<T>;

int main()
{
    int a[4];
    static_assert(
            RAR<std::vector<int>> and
            RAR<std::vector<bool>> and
            RAR<std::deque<int>> and
            RAR<std::valarray<int>> and
            RAR<decltype(a)> and
        not RAR<std::list<int>> and
        not RAR<std::set<int>> and
            RAR<std::array<std::list<int>,42>>
    );
}
```


## See also


| cpp/ranges/dsc sized_range | (see dedicated page) |
| cpp/ranges/dsc contiguous_range | (see dedicated page) |

