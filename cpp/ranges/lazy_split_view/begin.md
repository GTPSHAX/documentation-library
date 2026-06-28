---
title: std::ranges::lazy_split_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/begin
---


```cpp
dcl|num=1|since=c++20|
constexpr auto begin();
dcl|num=2|since=c++20|
constexpr auto begin() const
requires ranges::forward_range<V> && ranges::forward_range<const V>;
```

Returns an  to the first element of the `lazy_split_view`.
Let  be the underlying view and  be the underlying caching object (may not be present).
1. Equivalent to

```cpp
constexpr auto begin()
{
    if constexpr (ranges::forward_range<V>)
        return /*outer_iterator*/</*simple_view*/<V>>{*this, ranges::begin(base_)};
    else
    {
        current_ = ranges::begin(base_);
        return /*outer_iterator*/<false>{*this};
    }
}
```

2. Equivalent to }.

## Return value

to the first element.

## Example


## See also


| cpp/ranges/adaptor/dsc end|lazy_split_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

