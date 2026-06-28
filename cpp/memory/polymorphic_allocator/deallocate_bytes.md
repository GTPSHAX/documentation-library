---
title: std::pmr::polymorphic_allocator::deallocate_bytes
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/deallocate_bytes
---

ddcl|since=c++20|1=
void deallocate_bytes( void* p,
std::size_t nbytes,
std::size_t alignment = alignof(std::max_align_t) );
Deallocates the storage pointed to by `p`, which must have been allocated from a `std::pmr::memory_resource` `x` that compares equal to `*resource()`, using `x.allocate(nbytes, alignment)`, typically through a call to `allocate_bytes(nbytes, alignment)`.
Equivalent to `resource()->deallocate(p, nbytes, alignment);`.

## Parameters


### Parameters

- `p` - pointer to memory to deallocate
- `nbytes` - the number of bytes originally allocated
- `alignment` - the alignment originally allocated

## Exceptions

Throws nothing.

## Notes

This function was introduced for use with the fully-specialized allocator `std::pmr::polymorphic_allocator<>`, but it may be useful in any specialization.

## See also


| cpp/memory/polymorphic_allocator/dsc deallocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc delete_object | (see dedicated page) |
| cpp/memory/allocator traits/dsc deallocate | (see dedicated page) |
| cpp/memory/memory resource/dsc deallocate | (see dedicated page) |

