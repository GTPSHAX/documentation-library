---
title: Vs...>::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/begin
---


```cpp
dcl|num=1|since=c++23|1=
constexpr iterator<false> begin()
requires (!/*simple-view*/<First>  ...  !/*simple-view*/<Vs>);
dcl|num=2|since=c++23|1=
constexpr iterator<true> begin() const
requires (ranges::range<const First> && ... && ranges::range<const Vs>);
```

Returns an `iterator` to the first element of the `cartesian_product_view`.
Let  be the tuple of underlying views.
1. Equivalent to .
2. Equivalent to .

## Parameters

(none)

## Return value

An `iterator` to the first element.

## Example


### Example

```cpp
#include <array>
#include <format>
#include <iostream>
#include <ranges>
#include <string_view>
#include <tuple>
using namespace std::literals;

int main()
{
    constexpr auto a = std::array{"Curiously"sv, "Recurring"sv, "Template"sv, "Pattern"sv};

    constexpr auto v = std::ranges::cartesian_product_view(a[0], a[1], a[2], a[3]);

    constexpr std::tuple<char const&,
                         char const&,
                         char const&,
                         char const&> first{*v.begin()};

    std::cout << std::format("{}{}{}{}{}",
                             std::get<0>(first),
                             std::get<1>(first),
                             std::get<2>(first),
                             std::get<3>(first),
                             '\n');
}
```


**Output:**
```
CRTP
```


## See also


| cpp/ranges/adaptor/dsc end|cartesian_product_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

