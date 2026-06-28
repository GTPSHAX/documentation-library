---
title: std::ranges::take_while_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/end
---


```cpp
dcl|num=1|since=c++20|
constexpr auto end() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++20|
constexpr auto end() const requires
ranges::range<const V> &&
std::indirect_unary_predicate<const Pred, ranges::iterator_t<const V>>;
```

Returns a `sentinel` representing the end of the view.
Let  denote the underlying view.
1. Effectively returns `/*sentinel*/<false>(ranges::end(base_), std::addressof(pred()))`.
2. Effectively returns `/*sentinel*/<true>(ranges::end(base_), std::addressof(pred()))`.
Overload  does not participate in overload resolution if `V` is a simple view (that is, if `V` and `const V` are views with the same iterator and sentinel types).

## Parameters

(none)

## Return value

A `sentinel` representing the end of the view.

## Example


## Defect reports


## See also


| cpp/ranges/adaptor/dsc begin|take_while_view | (see dedicated page) |
| cpp/ranges/adaptor/sentinel/dsc operator cmp|take_while_view | (see dedicated page) |

