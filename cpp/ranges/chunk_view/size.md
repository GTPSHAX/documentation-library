---
title: std::ranges::chunk_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/size
---


```cpp
dcl|num=1|since=c++23|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++23|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements, which is the smallest integer value that is not less than the quotient of dividing the size of underlying view  by the underlying data member , that holds the number passed to the constructor (`0` if default constructed). Equivalent to
box|
`return``(``(ranges::distance(``),``));`
.

## Return value

The number of elements.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    constexpr static auto v = {1, 2, 3, 4, 5};
    constexpr auto w{ std::ranges::chunk_view(v, 2) };
    static_assert(w.size() == (5 / 2 + (5 % 2 ? 1 : 0)));
}
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

