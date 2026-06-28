---
title: operators (ranges::cartesian_product_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator/operator_cmp
---


# 1=operator==,<=>small|(ranges::cartesian_product_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires std::equality_comparable<ranges::iterator_t</*maybe-const*/<Const, First>>>;
dcl|num=2|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, std::default_sentinel_t );
dcl|num=2|since=c++23|1=
friend constexpr auto operator<=>( const /*iterator*/& x, const /*iterator*/& y )
requires /*all-random-access*/<Const, First, Vs...>;
```

Compares two `iterators` or an iterator and a sentinel.
Let  denote the underlying tuple of iterators.
1. Equivalent to: `1=return x.current_ == y.current_;`
2. Returns `true` if `1=std::get<i>(x.current_) == ranges::end(std::get<i>(x.parent_->bases_))` is `true` for any integer `0 ≤ i ≤ sizeof...(Vs)`. Otherwise, returns `false`.
3. Equivalent to: `1=return x.current_ <=> y.current_;`

## Parameters


### Parameters

- `x, y` - iterators or sentinels to compare

## Return value

The result of comparison.

## Example

