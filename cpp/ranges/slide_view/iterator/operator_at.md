---
title: std::ranges::slide_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/iterator/operator_at
---

ddcl|since=c++23|
constexpr auto operator[]( difference_type pos ) const
requires ranges::random_access_range<Base>;
Returns an element at specified relative location.
Let  and  be the underlying data members. Equivalent to: `return views::counted(current_ + pos, n_);`.

## Parameters


### Parameters

- `pos` - position relative to current location

## Return value

The element (of type ) at displacement `pos` relative to the current location.

## Example


## See also

