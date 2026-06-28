---
title: std::ranges::zip_transform_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/size
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto size()
requires ranges::sized_range</*InnerView*/>;
dcl|num=2|since=c++23|1=
constexpr auto size() const
requires ranges::sized_range<const /*InnerView*/>
```

Returns the number of elements in the `std::zip_transform_view|zip_transform_view`. Provided only if each underlying (adapted) range satisfies .
@1,2@ Equivalent to: .

## Parameters

(none)

## Return value

The number of elements, which is the minimum size among all sizes of adapted s.

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <deque>
#include <forward_list>
#include <functional>
#include <iostream>
#include <ranges>
#include <vector>

int main()
{
    auto x = std::vector{1, 2, 3, 4, 5};
    auto y = std::deque<short>{10, 20, 30};
    auto z = std::forward_list{100., 200.};

    auto v1 = std::views::zip_transform(std::plus{}, x, y);
    assert(v1.size() == std::min(x.size(), y.size()));
    assert(v1.size() == 3);
    for (int i : v1)
        std::cout << i << ' ';
    std::cout << '\n';

    [[maybe_unused]] auto v2 = std::views::zip_transform(std::plus{}, x, z);
//  auto sz = v2.size(); // Error: z doesn't have size(), so neither does v2
    static_assert(not std::ranges::sized_range<decltype(z)>);
}
```


**Output:**
```
11 22 33
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

