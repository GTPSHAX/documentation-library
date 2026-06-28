---
title: operator==(ranges::join_with_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/iterator/operator_cmp
---


# 1=operator==small|(ranges::join_with_view::''iterator'')


```cpp
dcl|since=c++23|1=
friend constexpr bool operator==( const /*iterator*/& x, const /*iterator*/& y )
requires std::is_reference_v<InnerBase> &&
std::equality_comparable<ranges::iterator_t<Base>> &&
std::equality_comparable<ranges::iterator_t<InnerBase>>;
```

Compares whether the iterators `x` and `y` are equal. They only compare equal if their `outer iterators` and `inner iterators` compare equal respectively.

## Parameters


### Parameters

- `x, y` - iterators to compare

## Return value


## See also


| cpp/ranges/adaptor/sentinel/dsc operator cmp|join_with_view | (see dedicated page) |

