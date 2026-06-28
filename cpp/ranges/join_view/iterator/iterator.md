---
title: std::ranges::join_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++20|1=
/*iterator*/() requires std::default_initializable<OuterIter> &&
std::default_initializable<InnerIter> = default;
dcl|num=2|since=c++20|1=
constexpr /*iterator*/( Parent& parent, OuterIter outer );
dcl|num=3|since=c++20|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
std::convertible_to<ranges::iterator_t<V>, OuterIter> &&
std::convertible_to<ranges::iterator_t<InnerRng>, InnerIter>;
```

Constructs an iterator.
1. Default constructor. Value-initializes the underlying iterators, and initializes the pointer to parent `ranges::join_view` with `nullptr`.
2. Initializes the underlying  iterator with `std::move(outer)`, and the pointer to parent  with `std::addressof(parent)`; then calls .
3. Converts `/*iterator*/<false>` to `/*iterator*/<true>`. Move constructs the underlying iterators  with `std::move(i.outer_)`,  with `std::move(i.inner_)`, and underlying pointer to parent  with `i.parent_`.

## Parameters


### Parameters

- `parent` - a (possibly const-qualified) `ranges::join_view`
- `outer` - an iterator into (possibly const-qualified) `ranges::iterator_t<Base>`
- `i` - an `/*iterator*/<false>`

## Example

