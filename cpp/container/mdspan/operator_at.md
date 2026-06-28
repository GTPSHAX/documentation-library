---
title: std::mdspan::operator[]
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/operator_at
---


```cpp
dcl|num=1|since=c++23|
template< class... OtherIndexTypes >
constexpr reference operator[]( OtherIndexTypes... indices ) const;
dcl|num=2|since=c++23|
template< class OtherIndexType >
constexpr reference operator[]
( std::span<OtherIndexType, rank()> indices ) const;
dcl|num=3|since=c++23|
template< class OtherIndexType >
constexpr reference operator[]
( const std::array<OtherIndexType, rank()>& indices ) const;
```

Returns a reference to the `indices` element of the mdspan.
1. Equivalent to .
@@ :
* `(std::is_convertible_v<OtherIndexTypes, index_type> && ...)`
* `(std::is_nothrow_constructible_v<index_type, OtherIndexTypes> && ...)`
* `1=sizeof...(OtherIndexTypes) == rank()`
@@
@2,3@ Let `P` be a parameter pack such that c multi
|std::is_same_v<std::make_index_sequence<rank()>,
|               std::index_sequence<P...>> is `true`, equivalent to .
@@ :
* `std::is_convertible_v<const OtherIndexType&, index_type>`
* `std::is_nothrow_constructible_v<index_type, const OtherIndexType&>`

## Parameters


### Parameters

- `indices` - the indices of the element to access

## Return value

A reference to the element.

## Example


## See also

