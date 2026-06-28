---
title: operators (ranges::zip_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/iterator/operator_cmp
---


# 1=operator==,<=>small|(ranges::zip_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires (std::equality_comparable<
ranges::iterator_t</*maybe-const*/<Const, Views>>> && ...);
dcl|num=2|since=c++23|1=
friend constexpr auto operator<=>( const /*iterator*/& x, const /*iterator*/& y )
requires ranges::random_access_range<Base>;
```

Compares the underlying iterators.
Let  be the underlying ''tuple-like'' object of iterators to elements of adapted views.
1. Returns:
* `1= x.current_ == y.current_` if `/*all-bidirectional*/<Const, Views...>` is true.
* Otherwise, `true` if there exists an integer `1= 0 <= i < sizeof...(Views)` such that `1= bool(std::get<i>(x.current_) == std::get<i>(y.current_))` is true.
* Otherwise, `false`.
2. Equivalent to `1=return x.current_ <=> y.current_;`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

The result of comparison

## See also


| cpp/ranges/adaptor/sentinel/dsc operator cmp|zip_view | (see dedicated page) |

