---
title: std::ranges::adjacent_transform_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/begin
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto begin();
dcl|num=2|since=c++23|1=
constexpr auto begin() const
requires ranges::range<const InnerView> &&
std::regular_invocable<const F&,
/*REPEAT*/(ranges::range_reference_t<const V>, N)...>;
```

Returns an `iterator` to the first element of the `adjacent_transform_view`.
Let  be the underlying `ranges::adjacent_view`.
1. Equivalent to `1=return /*iterator*/<false>(*this, inner_.begin());`.
2. Equivalent to `1=return /*iterator*/<true>(*this, inner_.begin());`.

## Parameters

(none)

## Return value

Iterator to the first element.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    auto sum = [](auto... args) { return (... + args); };

    constexpr auto view = std::views::iota(13, 1337)
                        {{!
```

static_assert(*view.begin() == 42 and 42 == 13 + 14 + 15);
}

## See also


| cpp/ranges/adaptor/dsc end|adjacent_transform_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

