---
title: std::ranges::drop_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view/size
---


```cpp
dcl|num=1|since=c++20|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++20|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Let  be the underlying view,  be the stored count (the number passed to the constructor, or `0` if `*this` is default constructed). Equivalent to
box|
`1=const auto s = ranges::size(``);`<br>
`1=const auto c = static_cast<decltype(s)>(``);`<br>
`return s < c ? 0 : s - c;`

## Return value

The number of elements.

## Example


### Example

```cpp
#include <array>
#include <ranges>

int main()
{
    constexpr std::array a{42, 43, 44};
    static_assert
    (
        std::ranges::drop_view{std::views::all(a), 0}.size() == 3 &&
        std::ranges::drop_view{std::views::all(a), 1}.size() == 2 &&
        std::ranges::drop_view{std::views::all(a), 2}.size() == 1 &&
        std::ranges::drop_view{std::views::all(a), 3}.size() == 0 &&
        std::ranges::drop_view{std::views::all(a), 4}.size() == 0
    );
}
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

