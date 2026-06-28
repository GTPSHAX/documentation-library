---
title: std::ranges::common_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_view/size
---


```cpp
dcl|num=1|since=c++20|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++20|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements. Equivalent to .

## Return value

The number of elements.

## Example


### Example

```cpp
#include <ranges>
#include <string_view>

int main()
{
    constexpr static auto v1 = {1, 2, 3, 4, 5};
    constexpr auto common1{v1 {{!
```

static_assert(common1.size() == 5);
constexpr auto take3{v1 | std::views::reverse | std::views::take(3)};
constexpr auto common2{take3 | std::views::common};
static_assert(common2.size() == 3);
using namespace std::literals;
constexpr static auto v2 = {"∧"sv, "∨"sv, "∃"sv, "∀"sv};
static_assert(std::ranges::views::common(v2).size() == 4);
}

## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

