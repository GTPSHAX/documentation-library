---
title: std::pmr::polymorphic_allocator::deallocate_object
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/deallocate_object
---

ddcl|since=c++20|1=
template< class U >
void deallocate_object( U* p, std::size_t n = 1 );
Deallocates the storage pointed to by `p`, which must have been allocated from a `std::pmr::memory_resource` `x` that compares equal to `*resource()`, using `x.allocate(n * sizeof(U), alignof(U))`, typically through a call to `allocate_object<U>(n)`.
Equivalent to `deallocate_bytes(p, n * sizeof(U), alignof(U));`.

## Parameters


### Parameters

- `p` - pointer to memory to deallocate
- `n` - number of objects of type U the memory was for

## Exceptions

Throws nothing.

## Notes

This function was introduced for use with the fully-specialized allocator `std::pmr::polymorphic_allocator<>`, but it may be useful in any specialization.

## See also


| cpp/memory/polymorphic_allocator/dsc deallocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc delete_object | (see dedicated page) |
| cpp/memory/allocator traits/dsc deallocate | (see dedicated page) |
| cpp/memory/memory resource/dsc deallocate | (see dedicated page) |

