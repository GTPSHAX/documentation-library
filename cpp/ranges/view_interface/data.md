---
title: std::ranges::view_interface::data
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/data
---


```cpp
dcl | num=1 | since=c++20 | 1=
constexpr auto data()
requires std::contiguous_iterator<ranges::iterator_t<D>>;
dcl | num=2 | since=c++20 | 1=
constexpr auto data() const
requires ranges::range<const D> &&
std::contiguous_iterator<ranges::iterator_t<const D>>;
```

The default implementation of `data()` member function obtains the address denoted by the beginning iterator via `std::to_address`, which is also the lowest address of the contiguous storage (implied by ) referenced by the view of the derived type when the view is not empty.
1. Let `derived` be `static_cast<D&>(*this)`. Equivalent to `return std::to_address(ranges::begin(derived));`.
2. Same as , except that `derived` is `static_cast<const D&>(*this)`.

## Return value

The address denoted by the beginning iterator.

## Notes

Following derived types may use the default implementation of `data()`:
* `     ranges::common_view|std::ranges::common_view`
* `std::ranges::drop_view`
* `std::ranges::drop_while_view`
* `std::ranges::ref_view`
* `std::ranges::subrange`
* `std::ranges::take_view`
* `std::ranges::take_while_view`
Following types are derived from `ranges::view_interface|std::ranges::view_interface` and do not declare their own `data()` member function, but they cannot use the default implementation, because their iterator types never satisfy :
* `ranges::basic_istream_view|std::ranges::basic_istream_view`
* `     ranges::elements_view|std::ranges::elements_view`
* `std::ranges::filter_view`
* `std::ranges::iota_view`
* `     ranges::join_view|std::ranges::join_view`
* `     ranges::lazy_split_view|std::ranges::lazy_split_view`
* `std::ranges::reverse_view`
* `     ranges::split_view|std::ranges::split_view`
* `std::ranges::transform_view`

## Example

constexpr static std::array a { 1,2,3,4,5 };
constexpr auto v { a | std::views::take(3) };
static_assert( &a[0] == v.data() );
}
| output=C++20!

## See also

