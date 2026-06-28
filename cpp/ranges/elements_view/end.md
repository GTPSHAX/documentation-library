---
title: std::ranges::elements_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/end
---


```cpp
dcl|num=1|since=c++20|1=
constexpr auto end() requires (!/*simple-view*/<V> && !ranges::common_range<V>);
dcl|num=2|since=c++20|1=
constexpr auto end() requires (!/*simple-view*/<V> && ranges::common_range<V>);
dcl|num=3|since=c++20|1=
constexpr auto end() const requires ranges::range<const V>;
dcl|num=4|since=c++20|1=
constexpr auto end() const requires ranges::common_range<const V>;
```

Returns a `sentinel` or an `iterator` representing the end of the `elements_view`.
Let  be the underlying view. Equivalent to:
1. }.
2. }.
3. }.
4. }.

## Parameters

(none)

## Return value

@1,3@ `sentinel` which compares equal to the end iterator
@2,4@ `iterator` to the element following the last element

## Notes

`end()` returns an iterator if and only if the underlying view is a : `elements_view<V,F>` models  whenever `V` does.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|elements_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

