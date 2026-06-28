---
title: std::ranges::join_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/begin
---


```cpp
dcl|num=1|since=c++20|
constexpr auto begin();
dcl|num=2|since=c++20|
constexpr auto begin() const
requires ranges::input_range<const V> &&
std::is_reference_v<ranges::range_reference_t<const V>>;
```

Returns an `iterator` to the first element of the `join_view`. Given  is the underlying view,
1. Equivalent to
* } if `/*simple-view*/<V>` is satisfied and `ranges::range_reference_t<V>` is reference type. Otherwise,
* }.
2. Equivalent to }.

## Parameters

(none)

## Return value

Iterator to the first element.

## Notes

When `ranges::range_reference_t<V>` is not a reference type, that is, deferencing an iterator of `V` returns a prvalue temporary, the `join_view` is only an , in which case only single-pass iteration is supported, and repeated calls to `begin()` may not give meaningful results.

## Example


## See also


| cpp/ranges/adaptor/dsc end|join_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

