---
title: std::ranges::adjacent_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/end
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto end() requires (!__SimpleView<V>);
dcl|num=2|since=c++23|1=
constexpr auto end() const requires ranges::range<const V>;
```

Returns an `iterator` or a `sentinel` representing the end of the `adjacent_view`.
Let `''base_''` be the underlying view.
1. Equivalent to:

```cpp
if constexpr (ranges::common_range<V>)
    return /*iterator*/<false>(__as_sentinel{}, ranges::begin(base_), ranges::end(base_));
else
    return /*sentinel*/<false>(ranges::end(base_));
```

2. Equivalent to:

```cpp
if constexpr (ranges::common_range<const V>)
    return /*iterator*/<true>(__as_sentinel{}, ranges::begin(base_), ranges::end(base_));
else
    return /*sentinel*/<true>(ranges::end(base_));
```


## Parameters

(none)

## Return value

An `iterator` to the element following the last element, if the underlying view `V` models . Otherwise, a `sentinel` which compares equal to the end iterator.

## Notes

`ranges::adjacent_view<V,N>` models  whenever the underlying view `V` does.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|adjacent_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

