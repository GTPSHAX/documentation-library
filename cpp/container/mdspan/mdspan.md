---
title: std::mdspan::mdspan
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/mdspan
---


```cpp
dcla|num=1|since=c++23|
constexpr mdspan();
dcla|num=2|since=c++23|
template< class... OtherIndexTypes >
constexpr explicit mdspan( data_handle_type p, OtherIndexTypes... exts );
dcla|num=3|since=c++23|1=
template< class OtherIndexType, std::size_t N >
constexpr explicit(N != rank_dynamic())
mdspan( data_handle_type p, std::span<OtherIndexType, N> exts );
dcla|num=4|since=c++23|1=
template< class OtherIndexType, std::size_t N >
constexpr explicit(N != rank_dynamic())
mdspan( data_handle_type p,
const std::array<OtherIndexType, N>& exts );
dcla|num=5|since=c++23|
constexpr mdspan( data_handle_type p, const extents_type& ext );
dcla|num=6|since=c++23|
constexpr mdspan( data_handle_type p, const mapping_type& m );
dcla|num=7|since=c++23|
constexpr mdspan( data_handle_type p, const mapping_type& m,
const accessor_type& a );
dcla|num=8|since=c++23|
template< class OtherElementType, class OtherExtents,
class OtherLayoutPolicy, class OtherAccessor >
constexpr explicit(/* see below */)
mdspan( const mdspan<OtherElementType, OtherExtents,
OtherLayoutPolicy, OtherAccessor>& other );
dcla|num=9|since=c++23|1=
constexpr mdspan( const mdspan& rhs ) = default;
dcla|num=10|since=c++23|1=
constexpr mdspan( mdspan&& rhs ) = default;
```

Constructs an `mdspan`, optionally using user-supplied data handle `p`, layout mapping `m`, and accessor `a`. If extents `exts` or `ext` are supplied, they are converted to `extents_type` and used to initialize the layout mapping.

## Parameters


### Parameters

- `p` - a handle to the underlying data
- `m` - a layout mapping
- `a` - an accessor
- `ext` - a `std::extents` object
- `exts` - represents a multi-dimensional extents
- `other` - another mdspan to convert from
- `rhs` - another mdspan to copy or move from

## Effects

For the data members listed in the table below:
* If the corresponding initializer is empty, the data member is value-initialized.
* If the corresponding intiializer is not empty, the data member is direct-non-list-initialized with that initializer.


| rowspan=2 | Overload |
| colspan=3 | Initializer for... |
| - |
| normal | rlpsi | /#ptr_ |
| normal | rlpsi | /#map_ |
| normal | rlpsi | /#acc_ |
| - |
| vl | 1 |
| colspan=3 | (empty) |
| - |
| vl | 2 |
| rowspan=6 | c | std::move(p) |
| style="text-align: start;" | c multi |
| extents_type |
| (static_cast<index_type> |
| (std::move(exts))...) |
| rowspan=5 | (empty) |
| - |
| vl | 3 |
| rowspan=2 | c | extents_type(exts) |
| - |
| vl | 4 |
| - |
| vl | 5 |
| c | ext |
| - |
| vl | 6 |
| rowspan=2 | c | m |
| - |
| vl | 7 |
| c | a |
| - |
| vl | 8 |
| box | c/core | other.rlpsi | /#ptr_ |
| box | c/core | other.rlpsi | /#map_ |
| box | c/core | other.rlpsi | /#acc_ |


## Constraints and supplement information

1. :
* `rank_dynamic() > 0`
* `std::is_default_constructible_v<data_handle_type>`
* `std::is_default_constructible_v<mapping_type>`
* `std::is_default_constructible_v<accessor_type>`
@@ .
2. :
* `(std::is_convertible_v<OtherIndexTypes, index_type> && ...)`
* `(std::is_nothrow_constructible<index_type, OtherIndexTypes> && ...)`
* `1=sizeof...(OtherIndexTypes) == rank()
* `std::is_constructible_v<mapping_type, extents_type>`
* `std::is_default_constructible_v<accessor_type>`
@@ .
@3,4@ :
* `std::is_convertible_v<const OtherIndexType&, index_type>`
* `std::is_nothrow_constructible_v<index_type, const OtherIndexType&>`
* `1=N == rank()
* `std::is_constructible_v<mapping_type, extents_type>`
* `std::is_default_constructible_v<accessor_type>`
@@ .
5. :
* `std::is_constructible_v<mapping_type, const extents_type&>`
* `std::is_default_constructible_v<accessor_type>`
@@ .
6. .
@@ .
7. .
8. The expression inside `explicit` is equivalent to c multi
|!std::is_convertible_v<const OtherLayoutPolicy::template mapping<OtherExtents>&,
|                       mapping_type>
|     !std::is_convertible_v<const OtherAccessor&, accessor_type>.
@@ :
* c multi
|std::is_constructible_v
|    <mapping_type, const OtherLayoutPolicy::template mapping<OtherExtents>&>
* `std::is_default_constructible_v<accessor_type>`
@@ :
* `std::is_constructible_v<data_handle_type, const OtherAccessor::data_handle_type&>`
* `std::is_constructible_v<extents_type, OtherExtents>`
@@ .
@@ cpp/hardened ub if|since=c++26|c multi
|static_extent(r)  std::dynamic_extent
|     static_extent(r)  other.extent(r) is `false` for some rank index `r` of `extents_type`

## Example


## See also

