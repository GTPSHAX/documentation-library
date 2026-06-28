---
title: std::ranges::chunk_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/end
---


```cpp
dcl|num=1|since=c++23|
constexpr std::default_sentinel_t end() const noexcept;
dcl|num=2|since=c++23|
constexpr auto end() requires (!__simple_view<V>);
dcl|num=3|since=c++23|
constexpr auto end() const requires ranges::forward_range<const V>;
```

Returns an `iterator` or a `std::default_sentinel` that compares equal to the end iterator of the `chunk_view`.
1. Available only if `V` models . Equivalent to: `return std::default_sentinel`.
@2,3@ Available if `V` models . Let  denote the underlying adapted view,  denote the stored chunk size, and  denote the nested iterator class.
2. Equivalent to

```cpp
if constexpr (ranges::common_range<V> && ranges::sized_range<V>)
{
    auto missing = (n_ - ranges::distance(base_) % n_) % n_;
    return iterator<false>(this, ranges::end(base_), missing);
}
else if constexpr (ranges::common_range<V> && !ranges::bidirectional_range<V>)
    return iterator<false>(this, ranges::end(base_));
else
    return std::default_sentinel;
```

3. Equivalent to

```cpp
if constexpr (ranges::common_range<const V> && ranges::sized_range<const V>)
{
    auto missing = (n_ - ranges::distance(base_) % n_) % n_;
    return iterator<true>(this, ranges::end(base_), missing);
}
else if constexpr (ranges::common_range<const V> && !ranges::bidirectional_range<const V>)
    return iterator<true>(this, ranges::end(base_));
else
    return std::default_sentinel;
```


## Return value

An iterator or sentinel representing the end of the `chunk_view`, as described above.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|chunk_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

