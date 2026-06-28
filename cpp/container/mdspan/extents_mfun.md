---
title: std::mdspan::extents
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents_mfun
---


```cpp
dcl|since=c++23|
constexpr const extents_type& extents() const noexcept;
```

Returns a const reference to the extents of the layout mapping . Equivalent to `return map_.extents();`.

## Parameters

(none)

## Return value

A const reference to the extents.

## Example


## See also

