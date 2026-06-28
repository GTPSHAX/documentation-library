---
title: iter_swap(ranges::adjacent_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/iterator/iter_swap
---


# iter_swapsmall|(ranges::adjacent_view::''iterator'')


```cpp
dcl|since=c++23|
friend constexpr void iter_swap( const /*iterator*/& x, const /*iterator*/& y )
noexcept( /*see below*/ )
requires std::indirectly_swappable<ranges::iterator_t<Base>>;
```

Swaps the objects pointed to by two underlying arrays of iterators (denoted as ).
Equivalent to:

```cpp
for (std::size_t i{}; i != N; ++i)
{
    std::ranges::iter_swap(x.current_[i], y.current_[i]);
}
```

The behavior is undefined if before the operation none of the iterators in `x.current_` is equal to an iterator in `y.current_`.

## Parameters


### Parameters

- `x, y` - iterators

## Return value

(none)

## Exceptions

noexcept|std::ranges::iter_swap(declval<ranges::iterator_t<Base>>(),
declval<ranges::iterator_t<Base>>())

## See also


| cpp/iterator/ranges/dsc iter swap | (see dedicated page) |
| cpp/algorithm/dsc iter swap | (see dedicated page) |

