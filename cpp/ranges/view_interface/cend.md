---
title: std::ranges::view_interface::cend
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/view_interface/cend
---


```cpp
dcl | num=1 | since=c++23 |
constexpr auto cend();
dcl | num=2 | since=c++23 |
constexpr auto cend() const requires ranges::range<const D>;
```

The default implementation of `cend()` member function returns the sentinel for the constant iterator of the range.
1. Let `derived` be a reference bound to `static_cast<D&>(*this)`. Equivalent to `return ranges::cend(derived);`.
2. Same as , except that `derived` is `static_cast<const D&>(*this)`.

## Return value

The sentinel for the constant iterator of the range.

## Notes

All range adaptors and range factories in the standard library and `std::ranges::subrange` use the default implementation of `cend`.

## Example

