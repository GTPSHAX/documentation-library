---
title: std::ranges::join_with_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/base
---


```cpp
dcl|num=1|since=c++23|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++23|
constexpr V base() &&;
```

Returns a copy of the underlying view.

## Return value

1.
2.

## Example

