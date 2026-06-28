---
title: std::ranges::transform_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/end
---


```cpp
dcl|num=1|since=c++20|
constexpr /*sentinel*/<false> end();
dcl|num=2|since=c++20|
constexpr /*iterator*/<false> end() requires ranges::common_range<V>;
dcl|num=3|since=c++20|
constexpr /*sentinel*/<true> end() const
requires ranges::range<const V> &&
std::regular_invocable<const F&, ranges::range_reference_t<const V>>;
dcl|num=4|since=c++20|
constexpr /*iterator*/<true> end() const
requires ranges::common_range<const V> &&
std::regular_invocable<const F&, ranges::range_reference_t<const V>>;
```

Returns a `sentinel` or an `iterator` representing the end of the `transform_view`.
Equivalent to:
1. .
2. box|`return``<false>{*this, ranges::end(`c/core|)};.
3. box|`return``<true>{ranges::end(`c/core|)};.
4. box|`return``<true>{*this, ranges::end(`c/core|)};.

## Parameters

(none)

## Return value

@1,3@ sentinel which compares equal to the end iterator
@2,4@ iterator to the element following the last element

## Notes

`end()` returns an iterator if and only if the underlying view is a : `transform_view<V,F>` models  whenever `V` does.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|transform_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |

