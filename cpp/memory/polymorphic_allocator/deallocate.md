---
title: std::pmr::polymorphic_allocator::deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/deallocate
---

ddcl|since=c++17|
void deallocate( T* p, std::size_t n );
Deallocates the storage pointed to by `p`, which must have been allocated from a `std::pmr::memory_resource` `x` that compares equal to `*resource()` using `x.allocate(n * sizeof(T), alignof(T))`.
Equivalent to `this->resource()->deallocate(p, n * sizeof(T), alignof(T));`.

## Parameters


### Parameters

- `p` - pointer to memory to deallocate
- `n` - the number of objects originally allocated

## Exceptions

Throws nothing.

## See also


| cpp/memory/polymorphic_allocator/dsc deallocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc deallocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc delete_object | (see dedicated page) |
| cpp/memory/allocator traits/dsc deallocate | (see dedicated page) |
| cpp/memory/memory resource/dsc deallocate | (see dedicated page) |

