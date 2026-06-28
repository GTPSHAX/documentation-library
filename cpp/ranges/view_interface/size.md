---
title: std::ranges::view_interface::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/size
---


```cpp
dcl|num=1|since=c++20|1=
constexpr auto size() requires ranges::forward_range<D> &&
std::sized_sentinel_for<ranges::sentinel_t<D>,
ranges::iterator_t<D>>;
dcl|num=2|since=c++20|1=
constexpr auto size() const requires ranges::forward_range<const D> &&
std::sized_sentinel_for<ranges::sentinel_t<const D>,
ranges::iterator_t<const D>>;
```

The default implementation of `size()` member function obtains the size of the range by calculating the difference between the sentinel and the beginning iterator.

## Return value

1. .
2. .

## Notes

Following derived types may use the default implementation of `size()`:
* `std::ranges::drop_while_view`
Following types are derived from `ranges::view_interface|std::ranges::view_interface` and do not declare their own `size()` member function, but they cannot use the default implementation, because their iterator and sentinel types never satisfy :
* `ranges::basic_istream_view|std::ranges::basic_istream_view`
* `std::ranges::filter_view`
* `ranges::join_view|std::ranges::join_view`
* `ranges::lazy_split_view|std::ranges::lazy_split_view`
* `ranges::split_view|std::ranges::split_view`
* `std::ranges::take_while_view`

## Defect reports


## See also


| cpp/iterator/dsc size | (see dedicated page) |
| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |

