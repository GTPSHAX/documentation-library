---
title: operator-(ranges::chunk_view::inner-iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/operator-
---


# operator-small|(ranges::chunk_view::''inner-iterator'')


```cpp
dcl|num=1|since=c++23|
friend constexpr difference_type operator-( std::default_sentinel_t s,
const /*inner-iterator*/& i )
requires ranges::sized_sentinel_for<ranges::sentinel_t<V>,
ranges::iterator_t<V>>;
dcl|num=2|since=c++23|
friend constexpr difference_type operator-( const /*inner-iterator*/& i,
std::default_sentinel_t s )
requires ranges::sized_sentinel_for<ranges::sentinel_t<V>,
ranges::iterator_t<V>>;
```

Calculates the distance (in number of underlying elements) between the `iterator` and sentinel.
Let  be the underlying pointer to the enclosing `chunk_view`.
1. Equivalent to:<br>c|1=
return ranges::min(i.parent_->remainder_,
ranges::end(i.parent_->base_) - *i.parent_->current_);
2. Equivalent to: `1=return -(s - i);`.

## Parameters


### Parameters

- `i` - the `iterator`
- `s` - the sentinel

## Return value

The distance between given iterator and sentinel.

## Example


## See also

