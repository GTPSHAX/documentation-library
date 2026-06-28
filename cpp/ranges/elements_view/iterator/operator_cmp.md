---
title: operators (ranges::elements_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/iterator/operator_cmp
---


# 1=operator==,<,>,<=,>=,<=>petty|(ranges::elements_view::''iterator'')


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
1. Equivalent to `1=return x.base() == y.base();`.
2. Equivalent to `1=return x.base() < y.base();`.
3. Equivalent to `return y < x;`.
4. Equivalent to `return !(y < x);`.
5. Equivalent to `return !(x < y);`.
6. Equivalent to `1=return x.base() <=> y.base();`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

Result of comparison.

## See also


| cpp/ranges/adaptor/sentinel/dsc operator cmp|elements_view | (see dedicated page) |

