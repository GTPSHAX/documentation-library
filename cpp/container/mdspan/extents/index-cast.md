---
title: std::extents::index-cast
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/index-cast
---

ddcl|since=c++23|notes=|
template< class OtherIndexType >
static constexpr auto /*index-cast*/( OtherIndexType&& i ) noexcept;
Casts the index `i` of type `OtherIndexType` into a certain integral type.
It is equivalent to:
* `return i;`, if `OtherIndexType` is an integral type other than `bool` and
* `return static_cast<index_type>(i);` otherwise.

## Parameters


### Parameters

- `i` - the index to be cast

## Return value

Cast index.

## Notes

A call to this function will always return an integral type other than `bool`. Integer-class types can use the `static_cast` branch without loss of precision because this function's call sites are already constrained on the convertibility of `OtherIndexType` to `index_type`.
