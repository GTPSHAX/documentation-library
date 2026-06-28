---
title: operators (ranges::join_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/iterator/operator_cmp
---


# 1=operator==small|(ranges::join_view::''iterator'', ranges::join_view::''iterator'')


```cpp
dcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires
/*ref-is-glvalue*/ &&
std::equality_comparable<ranges::iterator_t<Base>> &&
std::equality_comparable<ranges::iterator_t<ranges::range_reference_t<Base>>>;
```

Compares the underlying iterators.
Equivalent to: `1=return (x.outer_ == y.outer_) and (x.inner_ == y.inner_);`, where  and  are the underlying iterators. The constant `/*ref-is-glvalue*/` in the requires-clause is equal to `std::is_reference_v<ranges::range_reference_t<Base>>`.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value

Result of comparison.

## Example


## See also


| cpp/ranges/adaptor/sentinel/dsc operator cmp|join_view | (see dedicated page) |

