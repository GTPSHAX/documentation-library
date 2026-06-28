---
title: operators (ranges::enumerate_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator/operator_cmp
---


# 1=operator==,<=>small|(ranges::enumerate_view::''iterator'')


```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool
operator==( const /*iterator*/& x, const /*iterator*/& y ) noexcept;
dcl|num=2|since=c++23|1=
friend constexpr std::strong_ordering
operator<=>( const /*iterator*/& x, const /*iterator*/& y ) noexcept;
```

Compares the underlying `iterators`. Let  be the underlying index.
1. Equivalent to `1=return x.pos_ == y.pos_;`.
2. Equivalent to `1=return x.pos_ <=> y.pos_;`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

Result of comparison.

## See also


| cpp/ranges/adaptor/sentinel/dsc operator cmp|enumerate_view | (see dedicated page) |

