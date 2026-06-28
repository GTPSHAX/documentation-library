---
title: std::ranges::enumerate_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/size
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++23|1=
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements. Equivalent to `return ranges::size(base_);`, where  is the underlying view.

## Parameters

(none)

## Return value

The number of elements.

## Example


### Example

```cpp
#include <cassert>
#include <forward_list>
#include <ranges>
#include <string_view>

int main()
{
    constexpr static auto v1 = {1, 2, 3, 4, 5};
    constexpr auto ev1{v1 {{!
```

static_assert(ev1.size() == 5);
static_assert(std::ranges::sized_range<decltype(v1)>);
auto v2 = std::forward_list{1, 2, 3, 4, 5};
auto ev2 {v2 | std::views::enumerate};
static_assert(not std::ranges::sized_range<decltype(v2)>);
// auto size = ev2.size(); // Error: v2 is not a sized range
assert(std::ranges::distance(v2) == 5); // OK, distance does not require sized
// range, but has O(N) complexity here
}

## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

