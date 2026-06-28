---
title: std::allocator_traits::allocate_at_least
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/allocate_at_least
---

ddcl|since=c++23|
static constexpr std::allocation_result<pointer, size_type>
allocate_at_least( Alloc& a, size_type n );
`allocate_at_least` calls `a.allocate_at_least(n)` and returns its result if the call is well-formed, otherwise, it is equivalent to }.
`allocator_at_least` tries to allocate a storage for at least `n` `value_type` objects, and provides a fallback mechanism that allocates a storage for exact `n` objects.

## Parameters


### Parameters

- `a` - an allocator used for allocating storage
- `n` - the lower bound of number of objects to allocate storage for

## Return value

`a.allocate_at_least(n)` if it is well-formed.
Otherwise, }.

## Exceptions

Throws what and when the selected allocation function throws.

## Notes

The `allocate_at_least` member function of *Allocator* types are mainly provided for contiguous containers, e.g. `std::vector` and `std::basic_string`, in order to reduce reallocation by making their capacity match the actually allocated size when possible. Because `allocate_at_least` provides a fallback mechanism, it can be directly used where appropriate.
Given an allocator object `a` of type `Alloc`, let `result` denote the value returned from `std::allocator_traits<Alloc>::allocate_at_least(a, n)`, the storage should be deallocated by `a.deallocate(result.ptr, m)` (typically called via `std::allocator_traits<Alloc>::deallocate(a, result.ptr, m)`) in order to avoid memory leak.
The argument `m` used in deallocation must be not less than `n` and not greater than `result.count`, otherwise, the behavior is undefined. Note that `n` is always equal to `result.count` if the allocator does not provide `allocate_at_least`, which means that `m` is required to be equal to `n`.

## Example

