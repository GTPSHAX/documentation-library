---
title: std::ranges::join_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/end
---


```cpp
dcl|num=1|since=c++20|
constexpr auto end();
dcl|num=2|since=c++20|
constexpr auto end() const
requires ranges::input_range<const V> &&
std::is_reference_v<ranges::range_reference_t<const V>>;
```

Returns a `sentinel` or an `iterator` representing the end of the `join_view`.
Let  be the underlying view:
1. Equivalent to

```cpp
if constexpr (ranges::forward_range<V> &&
              std::is_reference_v<ranges::range_reference_t<V>> &&
              ranges::forward_range<ranges::range_reference_t<V>> &&
              ranges::common_range<V> &&
              ranges::common_range<ranges::range_reference_t<V>>)
    return /*iterator*/</*simple-view*/<V>>{*this, ranges::end(base_)};
else
    return /*sentinel*/</*simple-view*/<V>>{*this};
```

2. Equivalent to

```cpp
if constexpr (ranges::forward_range<const V> &&
              std::is_reference_v<ranges::range_reference_t<const V>> &&
              ranges::forward_range<ranges::range_reference_t<const V>> &&
              ranges::common_range<const V> &&
              ranges::common_range<ranges::range_reference_t<const V>>)
    return /*iterator*/<true>{*this, ranges::end(base_)};
else
    return /*sentinel*/<true>{*this};
```


## Parameters

(none)

## Return value

1. sentinel which compares equal to the end iterator.
2. iterator to the element following the last element.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|join_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

