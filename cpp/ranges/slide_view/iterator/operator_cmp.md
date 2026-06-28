---
title: operators (ranges::slide_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/iterator/operator_cmp
---


# 1=operator==,<,>,<=,>=,<=>small|(ranges::slide_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y );
dcl|num=2|since=c++23|1=
friend constexpr bool operator<( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=3|since=c++23|1=
friend constexpr bool operator>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=4|since=c++23|1=
friend constexpr bool operator<=( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=5|since=c++23|1=
friend constexpr bool operator>=( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++23|1=
friend constexpr auto operator<=>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base> &&
std::three_way_comparable<ranges::iterator_t<Base>>;
```

Compares the underlying iterators.
Let  and  be the underlying iterators to the begin and end of the sliding window, respectively.
1. Equivalent to:
* `1=return x.last_ele_ == y.last_ele_;`, if  is present. Otherwise,
* `1=return x.current_ == y.current_;`.
2. Equivalent to `return x.current_ < y.current_;`.
3. Equivalent to `return y < x;`.
4. Equivalent to `return !(y < x);`.
5. Equivalent to `return !(x < y);`.
6. Equivalent to `1=return x.current_ <=> y.current_;`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

The result of comparison.

## Example

