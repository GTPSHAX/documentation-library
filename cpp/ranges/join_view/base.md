---
title: std::ranges::join_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/base
---


```cpp
dcl | num=1 | since=c++20 |
constexpr V base() const& requires std::copy_constructible<V>;
dcl | num=2 | since=c++20 |
constexpr V base() &&;
```

Returns a copy of the underlying view.
1. Copy constructs the result from the underlying view.
2. Move constructs the result from the underlying view.

## Parameters

(none)

## Return value

A copy of the underlying view.

## Example

