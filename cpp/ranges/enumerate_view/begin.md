---
title: std::ranges::enumerate_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/begin
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto begin() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++23|1=
constexpr auto begin() const requires /*range-with-movable-references*/<const V>;
```

Returns an `iterator` to the first element of the `enumerate_view`.
Let  denote the underlying view.
1. Equivalent to `1=return /*iterator*/<false>(ranges::begin(base_), 0);`.
2. Equivalent to `1=return /*iterator*/<true>(ranges::begin(base_), 0);`.

## Parameters

(none)

## Return value

Iterator to the first element.

## Example


## See also


| cpp/ranges/adaptor/dsc end|enumerate_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

