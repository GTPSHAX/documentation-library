---
title: std::ranges::drop_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view/end
---


```cpp
dcl|num=1|since=c++20|
constexpr auto end() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++20|
constexpr auto end() const requires ranges::range<const V>;
```

Returns a sentinel or an iterator representing the end of the `drop_view`.

## Return value

.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <ranges>

int main()
{
    namespace ranges = std::ranges;
    constexpr char url[]{"https://cppreference.com"};

    const auto p = std::distance(ranges::begin(url), ranges::find(url, '/'));
    auto site = ranges::drop_view{url, p + 2}; // drop the prefix "https://"

    for (auto it = site.begin(); it != site.end(); ++it)
        std::cout << *it;
    std::cout << '\n';
}
```


**Output:**
```
cppreference.com
```


## See also


| cpp/ranges/adaptor/dsc begin|drop_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

