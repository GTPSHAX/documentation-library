---
title: std::ranges::drop_while_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_while_view/end
---

ddcl|since=c++20|
constexpr auto end();
Returns a sentinel or an iterator representing the end of the `drop_while_view`.
Effectively returns `ranges::end(base_)`, where  is the underlying view.

## Parameters

(none)

## Return value

A sentinel or an iterator representing the end of the view.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <ranges>

int main()
{
    static constexpr auto data = {0, -1, -2, 3, 1, 4, 1, 5}; 
    auto view = std::ranges::drop_while_view{data, [](int x) { return x <= 0; }<!---->};
    assert(view.end()[-1] == 5);
}
```


## See also


| cpp/ranges/adaptor/dsc begin|drop_while_view | (see dedicated page) |

