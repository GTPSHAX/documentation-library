---
title: std::ranges::stride_view::iterator<Const>::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/base
---


```cpp
dcl|num=1|since=c++23|1=
constexpr ranges::iterator_t<Base> base() &&;
dcl|num=2|since=c++23|1=
constexpr const ranges::iterator_t<Base>& base() const& noexcept;
```

Returns the underlying iterator. Let  be the underlying iterator.
1. Equivalent to: `return std::move(current_);`.
2. Equivalent to: `return current_;`.

## Parameters

(none)

## Example

