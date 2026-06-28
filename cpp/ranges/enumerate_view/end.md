---
title: std::ranges::enumerate_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/end
---


```cpp
dcl|num=1|since=c++23|
constexpr auto end() requires (!__simple_view<V>);
dcl|num=2|since=c++23|
constexpr auto end() const requires /*range-with-movable-references*/<const V>;
```

Returns an `iterator` or a `sentinel` that compares equal to the end iterator of the `enumerate_view`.
Let `''base_''` denote the underlying view.
1. Equivalent to:

```cpp
if constexpr (ranges::forward_range<V> and 
              ranges::common_range<V>  and 
              ranges::sized_range<V>)
    return /*iterator*/<false>(ranges::end(base_), ranges::distance(base_));
else
    return /*sentinel*/<false>(ranges::end(base_));
```

2. Equivalent to:

```cpp
if constexpr (ranges::forward_range<const V> and 
              ranges::common_range<const V>  and 
              ranges::sized_range<const V>)
    return /*iterator*/<true>(ranges::end(base_), ranges::distance(base_));
else
    return /*sentinel*/<true>(ranges::end(base_));
```


## Parameters

(none)

## Return value

An `iterator` or a `sentinel` representing the end of the `enumerate_view`, as described above.

## Example


## Defect reports


## See also


| cpp/ranges/adaptor/dsc begin|enumerate_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

