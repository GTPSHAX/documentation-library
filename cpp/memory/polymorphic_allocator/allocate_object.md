---
title: std::pmr::polymorphic_allocator::allocate_object
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/allocate_object
---


```cpp
dcl|since=c++20|1=
template< class U >
U* allocate_object( std::size_t n = 1 );
```

Allocates storage for `n` objects of type `U` using the underlying memory resource.
If `std::numeric_limits<std::size_t>::max() / sizeof(U) < n`, throws `std::bad_array_new_length`, otherwise equivalent to `return static_cast<U*>(allocate_bytes(n * sizeof(U), alignof(U)));`.

## Parameters


### Parameters

- `n` - the number of objects to allocate storage for

## Return value

A pointer to the allocated storage.

## Notes

This function was introduced for use with the fully-specialized allocator `std::pmr::polymorphic_allocator<>`, but it may be useful in any specialization as a shortcut to avoid having to rebind from `std::pmr::polymorphic_allocator<T>` to `std::pmr::polymorphic_allocator<U>`.
Since `U` is not deduced, it must be provided as a template argument when calling this function.

## Exceptions

Throws `std::bad_array_new_length` if `n > std::numeric_limits<std::size_t>::max() / sizeof(U)`; may also be any exceptions thrown by the call to `resource()->allocate`.

## See also


| cpp/memory/polymorphic_allocator/dsc allocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc new_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator traits/dsc allocate | (see dedicated page) |
| cpp/memory/memory resource/dsc allocate | (see dedicated page) |

