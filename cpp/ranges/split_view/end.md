---
title: std::ranges::split_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/end
---

ddcl|since=c++20|
constexpr auto end() const;
Returns an `iterator` or a `sentinel` representing the end of the resulting subrange. Equivalent to:
box|c/core|
constexpr auto end()
{
if constexpr (ranges::common_range<V>)
return`{*this, ranges::end(`;
else
returnc/core|{*this};
}

## Return value

An `iterator` or a `sentinel`.

## Example


### Example

```cpp
#include <cassert>
#include <ranges>
#include <string_view>

int main()
{
    constexpr std::string_view keywords{"bitand bitor bool break"};
    std::ranges::split_view kw{keywords, ' '};
    assert(4 == std::ranges::distance(kw.begin(), kw.end()));
}
```


## See also


| cpp/ranges/adaptor/dsc begin|split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|lazy_split_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

