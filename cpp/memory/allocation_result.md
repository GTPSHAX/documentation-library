---
title: std::allocation_result
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/allocation_result
---

ddcl|header=memory|since=c++23|1=
template< class Pointer, class SizeType = std::size_t >
struct allocation_result;
`allocation_result` specializations are returned from the `allocate_at_least` member function of appropriate *Allocator* types (e.g. `cpp/memory/allocator/allocate_at_least|std::allocator::allocate_at_least`) and `cpp/memory/allocator_traits/allocate_at_least|std::allocator_traits::allocate_at_least`.
Every specialization of `allocation_result` has no base classes or declared members other than `ptr` and `count`, thus it is suitable for  and .

## Template parameters


### Parameters

- `Pointer` - typically `std::allocator_traits<Alloc>::pointer`, where `Alloc` is an *Allocator* type
- `SizeType` - typically `std::allocator_traits<Alloc>::size_type`, where `Alloc` is an *Allocator* type

## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Notes

`Pointer` and `SizeType` are a pointer to an object type and `std::make_unsigned_t<std::ptrdiff_t>` (which is almost always same as `std::size_t`) by default.

## Example

