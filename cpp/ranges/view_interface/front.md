---
title: std::ranges::view_interface::front
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/front
---


```cpp
dcl|num=1|since=c++20|
constexpr decltype(auto) front()
requires ranges::forward_range<D>;
dcl|num=2|since=c++20|
constexpr decltype(auto) front() const
requires ranges::forward_range<const D>;
```

The default implementation of `front()` member function returns the first element in the view of the derived type. Whether the element is returned by value or by reference depends on the `operator*` of the iterator type.
Equivalent to `return *ranges::begin(derived);`, where `derived` is:
1. `static_cast<D&>(*this)`
2. `static_cast<const D&>(*this)`

## Return value

The first element in the view.

## Notes

In C++20, no type derived from `ranges::view_interface|std::ranges::view_interface` in the standard library provides their own `front()` member function. Almost all of these types use the default implementation.
A notable exception is `ranges::basic_istream_view|std::ranges::basic_istream_view`. For it never satisfies , the view cannot use the inherited `front()`.
The inherited `front()` member function is available for `std::ranges::empty_view`, but a call to it always results in undefined behavior.

## Example

