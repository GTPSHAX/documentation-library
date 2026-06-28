---
title: std::pmr::polymorphic_allocator::allocate_bytes
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/allocate_bytes
---


```cpp
dcl|since=c++20|1=
void* allocate_bytes( std::size_t nbytes,
std::size_t alignment = alignof(std::max_align_t) );
```

Allocates `nbytes` bytes of storage at specified alignment `alignment` using the underlying memory resource. Equivalent to `return resource()->allocate(nbytes, alignment);`.

## Parameters


### Parameters

- `nbytes` - the number of bytes to allocate
- `alignment` - the alignment to use

## Return value

A pointer to the allocated storage.

## Notes

This function was introduced for use with the fully-specialized allocator `std::pmr::polymorphic_allocator<>`, but it may be useful in any specialization.
The return type is `void*` (rather than, e.g., `std::byte*`) to support conversion to an arbitrary pointer type `U*` by `static_cast<U*>`.

## Exceptions

May throw any exceptions thrown by the call to `resource()->allocate`.

## See also


| cpp/memory/polymorphic_allocator/dsc allocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc new_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator traits/dsc allocate | (see dedicated page) |
| cpp/memory/memory resource/dsc allocate | (see dedicated page) |

