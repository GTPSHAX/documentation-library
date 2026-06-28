---
title: std::ranges::take_while_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/begin
---


```cpp
dcl|num=1|since=c++20|
constexpr auto begin() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++20|
constexpr auto begin() const requires
ranges::range<const V> &&
std::indirect_unary_predicate<const Pred, ranges::iterator_t<const V>>;
```

Returns an iterator to the first element of the view. Effectively calls `ranges::begin` on the underlying view .
Overload  does not participate in overload resolution if `V` is a simple view (that is, if `V` and `const V` are views with the same iterator and sentinel types).

## Parameters

(none)

## Return value

`ranges::begin(base_)`, where  is the underlying view.

## Example


## Defect reports


## See also


| cpp/ranges/adaptor/dsc end|take_while_view | (see dedicated page) |
| cpp/ranges/adaptor/sentinel/dsc operator cmp|take_while_view | (see dedicated page) |

