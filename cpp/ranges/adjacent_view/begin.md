---
title: std::ranges::adjacent_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/begin
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto begin() requires (!__SimpleView<V>);
dcl|num=2|since=c++23|1=
constexpr auto begin() const requires ranges::range<const V>;
```

Returns an `iterator` to the first element of the `adjacent_view`.
Let  be the underlying view.
1. Equivalent to `1=return /*iterator*/<false>(ranges::begin(base_), ranges::end(base_));`.
2. Equivalent to `1=return /*iterator*/<true>(ranges::begin(base_), ranges::end(base_));`.

## Parameters

(none)

## Return value

Iterator to the first element.

## Example


### Example

```cpp
#include <ranges>
#include <tuple>
#include <type_traits>

int main()
{
    constexpr static auto v = {'A', 'B', 'C', 'D', 'E'};

    constexpr auto view = std::views::adjacent<3>(v);

    constexpr auto tuple = *view.begin();

    static_assert
    (
        std::is_same_v
        <
            decltype(tuple),
            const std::tuple<char const&, char const&, char const&>
        >
    );

    static_assert
    (
        std::get<0>(tuple) == 'A' &&
        std::get<1>(tuple) == 'B' &&
        std::get<2>(tuple) == 'C'
    );
}
```


## See also


| cpp/ranges/adaptor/dsc end|adjacent_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

