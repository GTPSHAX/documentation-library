---
title: operator==(ranges::take_while_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::take_while_view::''sentinel'')

ddcl|since=c++20|1=
friend constexpr bool operator==( const ranges::iterator_t<Base>& x,
const /*sentinel*/& y );
Compares a `take_while_view::/*sentinel*/` with an iterator into (possibly const-qualified) view `V`. The iterator is typically obtained from a call to `cpp/ranges/take_while_view/begin|take_while_view::begin`.
Returns `true` if `x` compares equal to the underlying sentinel of `y` (i.e. `y.base()`), or if the predicate returns `false` when applied to `*x`.

## Parameters


### Parameters

- `x` - iterator to compare
- `y` - sentinel to compare

## Return value

`1= y.end_ == x , where  denotes the stored sentinel and  denotes the stored pointer to predicate.

## Example

