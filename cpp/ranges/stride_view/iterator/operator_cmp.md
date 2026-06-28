---
title: operators (ranges::stride_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/operator_cmp
---


# 1=operator==,<,>,<=,>=,<=>small|(ranges::stride_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, std::default_sentinel_t );
dcl|num=2|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires std::equality_comparable<ranges::iterator_t<Base>>;
dcl|num=3|since=c++23|1=
friend constexpr bool operator<( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=4|since=c++23|1=
friend constexpr bool operator>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=5|since=c++23|1=
friend constexpr bool operator<=( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++23|1=
friend constexpr bool operator>=( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=7|since=c++23|1=
friend constexpr auto operator<=>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base> and
std::three_way_comparable<ranges::iterator_t<Base>>;
```

Compares the underlying iterators/sentinels.
Let  be the underlying iterator, and  be the underlying sentinel.
1. Equivalent to `1=return x.current_ == x.end_;`.
2. Equivalent to `1=return x.current_ == y.current_;`.
3. Equivalent to `1=return x.current_ < y.current_;`.
4. Equivalent to `1=return y < x;`
5. Equivalent to `1=return !(y < x);`
6. Equivalent to `1=return !(x < y);`
7. Equivalent to `1=return x.current_ <=> y.current_;`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

result of comparison

## Example

