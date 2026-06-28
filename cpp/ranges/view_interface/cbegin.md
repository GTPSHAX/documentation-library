---
title: std::ranges::view_interface::cbegin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/cbegin
---


```cpp
dcl|num=1|since=c++23|
constexpr auto cbegin();
dcl|num=2|since=c++23|
constexpr auto cbegin() const requires ranges::range<const D>;
```

The default implementation of `cbegin()` member function returns a constant beginning iterator of the range.
1. Let `derived` be a reference bound to `static_cast<D&>(*this)`.
@@ Equivalent to `return ranges::cbegin(derived);`.
2. Same as , except that `derived` is `static_cast<const D&>(*this)`.

## Return value

A constant beginning iterator of the range.

## Notes

All range adaptors and range factories in the standard library and `std::ranges::subrange` use the default implementation of `cbegin`.

## Example

