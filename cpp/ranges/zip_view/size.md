---
title: std::ranges::zip_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/size
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto size()
requires (ranges::sized_range<Views> && ...);
dcl|num=2|since=c++23|1=
constexpr auto size() const
requires (ranges::sized_range<const Views> && ...);
```

Returns the number of elements in the `zip_view`. Provided only if each underlying (adapted) range satisfies .
Equivalent to:

```cpp
return std::apply
(
    [](auto... sizes)
    {
        using CT = /*make-unsigned-like-t*/<std::common_type_t<decltype(sizes)...>>;
        return ranges::min({CT(sizes)...});
    },
    /*tuple-transform*/(ranges::size, views_)
);
```


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
#include <ranges>
#include <vector>

int main()
{
    auto x = std::vector{1, 2, 3, 4, 5};
    auto y = std::deque{'a', 'b', 'c'};
    auto z = std::forward_list{1., 2.};

    auto v1 = std::views::zip(x, y);
    assert(v1.size() == std::min(x.size(), y.size()));
    assert(v1.size() == 3);

    [[maybe_unused]] auto v2 = std::views::zip(x, z);
//  auto sz = v2.size(); // Error, v2 does not have size():
    static_assert(not std::ranges::sized_range<decltype(z)>);
}
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

