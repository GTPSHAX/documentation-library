---
title: std::ranges::chunk_view::inner-iterator::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/base
---

ddcl|since=c++23|1=
constexpr const ranges::iterator_t<V>& base() const &;
Returns the underlying cached iterator to current element (in current chunk) in `chunk_view`.
Let  be the underlying pointer to the enclosing `chunk_view`.
Equivalent to: .

## Parameters

(none)

## Return value

An iterator.

## Example


## See also

