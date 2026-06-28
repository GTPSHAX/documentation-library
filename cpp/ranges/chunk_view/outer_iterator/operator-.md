---
title: operator-(ranges::chunk_view::outer-iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/outer_iterator/operator-
---


# operator-small|(ranges::chunk_view::''outer-iterator'')


```cpp
dcl|num=1|since=c++23|
friend constexpr difference_type operator-( std::default_sentinel_t s,
const /*outer-iterator*/& i )
requires ranges::sized_sentinel_for<ranges::sentinel_t<V>,
ranges::iterator_t<V>>;
dcl|num=2|since=c++23|
friend constexpr difference_type operator-( const /*outer-iterator*/& i,
std::default_sentinel_t s )
requires ranges::sized_sentinel_for<ranges::sentinel_t<V>,
ranges::iterator_t<V>>;
```

Calculates the distance (in number of chunks) between the `iterator` and sentinel.
Let  be the underlying pointer to enclosing `chunk_view`.
1. Equivalent to:

```cpp
const auto dist = ranges::end(i.parent_->base_) - *i.parent_->current_;
if (dist < i.parent_->remainder_)
    return dist == 0 ? 0 : 1;
return /*div-ceil*/(dist - i.parent_->remainder_, i.parent_->n_) + 1;
```

2. Equivalent to: `1=return -(s - i);`.

## Parameters


### Parameters

- `i` - the `iterator`
- `s` - the sentinel

## Return value

The distance between given iterator and sentinel.

## Example


## See also

