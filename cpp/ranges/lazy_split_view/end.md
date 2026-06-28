---
title: std::ranges::lazy_split_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/end
---


```cpp
dcl|num=1|since=c++20|1=
constexpr auto end() requires ranges::forward_range<V> && ranges::common_range<V>;
dcl|num=2|since=c++20|1=
constexpr auto end() const;
```

Returns an iterator or sometimes a sentinel representing the end of the . Let  be the underlying view.
1. Returns an iterator. Equivalent to:
}.
2. Returns an  or a `std::default_sentinel`.
Equivalent to:

```cpp
if constexpr (ranges::forward_range<V> && ranges::forward_range<const V> &&
              ranges::common_range<const V>)
    return /*outer_iterator*/<true>{*this, ranges::end(base_)};
else
    return std::default_sentinel;
```


## Return value

An  or a `std::default_sentinel` representing the end of the .

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string_view>

int main()
{
    constexpr std::string_view keywords{"false float for friend"};
    std::ranges::lazy_split_view kw{keywords, ' '};
    const auto count = std::ranges::distance(kw.begin(), kw.end());
    std::cout << "Words count: " << count << '\n';
}
```


**Output:**
```
Words count: 4
```


## See also


| cpp/ranges/adaptor/dsc begin|lazy_split_view | (see dedicated page) |
| cpp/ranges/adaptor/dsc end|split_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

