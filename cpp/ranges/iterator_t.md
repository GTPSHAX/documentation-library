---
title: std::ranges::sentinel_t
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/iterator_t
---


```cpp
**Header:** `<`ranges`>`
dcl|num=1|since=c++20|1=
template< class T >
using iterator_t = decltype(ranges::begin(std::declval<T&>()));
dcl|num=2|since=c++23|1=
template< ranges::range R >
using const_iterator_t = decltype(ranges::cbegin(std::declval<R&>()));
dcl|num=3|since=c++20|1=
template< ranges::range R >
using sentinel_t = decltype(ranges::end(std::declval<R&>()));
dcl|num=4|since=c++23|1=
template< ranges::range R >
using const_sentinel_t = decltype(ranges::cend(std::declval<R&>()));
```

1. Used to obtain the iterator type of the type `T`.
2. Used to obtain the constant iterator type of the  type `R`.
3. Used to obtain the sentinel type of the range type `R`.
4. Used to obtain the constant sentinel type of the range type `R`.

## Template parameters


### Parameters

- `T` - a type that can be used in `std::ranges::begin`
- `R` - a  type or a  type

## Notes

`iterator_t` can be applied to non-range types, e.g. arrays with unknown bound.

## Defect reports


## See also


| cpp/iterator/dsc iter_t | (see dedicated page) |
| cpp/ranges/dsc range_size_t | (see dedicated page) |
| cpp/ranges/dsc range_reference_t | (see dedicated page) |

