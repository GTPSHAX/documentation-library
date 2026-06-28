---
title: operators (ranges::transform_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/iterator/operator_cmp
---


# 1=operator==,<,>,<=,>=,<=>small|(ranges::transform_view::''iterator'')


```cpp
dcl|num=1|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires std::equality_comparable<ranges::iterator_t<Base>>;
dcl|num=2|since=c++20|1=
friend constexpr bool operator<( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=3|since=c++20|1=
friend constexpr bool operator>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=4|since=c++20|1=
friend constexpr bool operator<=( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=5|since=c++20|1=
friend constexpr bool operator>=( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++20|1=
friend constexpr auto operator<=>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base> &&
std::three_way_comparable<ranges::iterator_t<Base>>;
```

Compares the underlying iterators.
1. Equivalent to `1=return x.current_ == y.current_;`, where  is the underlying iterator.
2. Equivalent to `1=return x.current_ < y.current_;`, where  is the underlying iterator.
3. Equivalent to `1=return y < x;`
4. Equivalent to `1=return !(y < x);`
5. Equivalent to `1=return !(x < y);`
6. Equivalent to `1=return x.current_ <=> y.current_;`, where  is the underlying iterator.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

result of comparison

## See also


| cpp/ranges/adaptor/sentinel/dsc operator cmp|transform_view | (see dedicated page) |

