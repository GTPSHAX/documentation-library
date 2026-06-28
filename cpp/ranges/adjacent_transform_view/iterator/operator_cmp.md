---
title: operators (ranges::adjacent_transform_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/iterator/operator_cmp
---


# 1=operator==,<,>,<=,>=,<=>small|(ranges::adjacent_transform_view::''iterator'')


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
requires ranges::random_access_range<Base> and
std::three_way_comparable<ranges::iterator_t<Base>>;
```

Compares the underlying iterators: .
1. Equivalent to `1=return x.inner_ == y.inner_;`.
2. Equivalent to `1=return x.inner_ < y.inner_;`.
3. Equivalent to `1=return x.inner_ > y.inner_;`.
4. Equivalent to `1=return x.inner_ <= y.inner_;`.
5. Equivalent to `1=return x.inner_ >= y.inner_;`.
6. Equivalent to `1=return x.inner_ <=> y.inner_;`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

Result of comparison.

## Example

