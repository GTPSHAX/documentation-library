---
title: std::ranges::elements_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/begin
---


```cpp
dcl|num=1|since=c++20|1=
constexpr auto begin() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++20|1=
constexpr auto begin() const requires ranges::range<const V>;
```

Returns an `iterator` to the first element of the `elements_view`.
Let  be the underlying view.
1. Equivalent to `1=return /*iterator*/<false>(ranges::begin(base_));`.
2. Equivalent to `1=return /*iterator*/<true>(ranges::begin(base_));`.

## Parameters

(none)

## Return value

Iterator to the first element.

## Example


## See also


| cpp/ranges/adaptor/dsc end|elements_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |

