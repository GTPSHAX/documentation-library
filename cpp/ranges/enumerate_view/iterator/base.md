---
title: std::ranges::enumerate_view::iterator<Const>::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator/base
---


```cpp
dcl|num=1|since=c++23|1=
constexpr const ranges::iterator_t<Base>& base() const& noexcept;
dcl|num=2|since=c++23|1=
constexpr ranges::iterator_t<Base> base() &&;
```

Returns the underlying iterator. Let  be the underlying iterator.
1. Equivalent to: `return current_;`.
2. Equivalent to: `return std::move(current_);`.

## Parameters

(none)

## Return value

An iterator to the current element in `enumerate_view`.

## Example

