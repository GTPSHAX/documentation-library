---
title: std::ranges::view_interface::back
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/back
---


```cpp
dcl|num=1|since=c++20|
constexpr decltype(auto) back()
requires ranges::bidirectional_range<D> && ranges::common_range<D>;
dcl|num=2|since=c++20|
constexpr decltype(auto) back() const
requires ranges::bidirectional_range<const D> && ranges::common_range<const D>;
```

The default implementation of `back()` member function returns the last element in the view of the derived type. Whether the element is returned by value or by reference depends on the `operator*` of the iterator type.
Equivalent to `return *ranges::prev(ranges::end(derived));`, where `derived` is:
1. `static_cast<D&>(*this)`
2. `static_cast<const D&>(*this)`

## Return value

The last element in the view.

## Notes

In C++20, no type derived from `ranges::view_interface|std::ranges::view_interface` in the standard library provides their own `back()` member function.
However, following derived types cannot use the default implementations, as they never satisfy neither  nor :
* `ranges::basic_istream_view|std::ranges::basic_istream_view`
* `     ranges::lazy_split_view|std::ranges::lazy_split_view`
* `     ranges::split_view|std::ranges::split_view`
* `std::ranges::take_while_view`
The inherited `back()` member function is available for `std::ranges::empty_view`, but a call to it always results in undefined behavior.

## Example

