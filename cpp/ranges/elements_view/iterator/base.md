---
title: std::ranges::elements_view::iterator<Const>::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/iterator/base
---


```cpp
dcl | num=1 | since=c++20 |
constexpr const ranges::iterator_t<Base>& base() const & noexcept;
dcl | num=2 | since=c++20 |
constexpr ranges::iterator_t<Base> base() &&;
```

Returns the underlying iterator.
1. Returns a reference to the underlying iterator.
2. Move constructs the result from the underlying iterator.

## Parameters

(none)

## Return value

1. A reference to the underlying iterator.
1. An iterator move constructed from the underlying iterator.

## Example


## Defect reports

