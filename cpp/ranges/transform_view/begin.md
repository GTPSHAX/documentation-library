---
title: std::ranges::transform_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/begin
---


```cpp
dcl|num=1|since=c++20|1=
constexpr /*iterator*/<false> begin();
dcl|num=2|since=c++20|1=
constexpr /*iterator*/<true> begin() const
requires ranges::range<const V> &&
std::regular_invocable<const F&, ranges::range_reference_t<const V>>;
```

Returns an `iterator` to the first element of the `transform_view`.
1. Equivalent to box|`return``<false>{*this, ranges::begin(`c/core|)};.
2. Equivalent to box|`return``<true>{*this, ranges::begin(`c/core|)};.

## Return value

Iterator to the first element.

## Example


## See also


| cpp/ranges/adaptor/dsc end|transform_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

