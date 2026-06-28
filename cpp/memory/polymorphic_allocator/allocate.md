---
title: std::pmr::polymorphic_allocator::allocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator/allocate
---


```cpp
dcl|since=c++17|
T* allocate( std::size_t n );
```

Allocates storage for `n` objects of type `T` using the underlying memory resource. Equivalent to `return static_cast<T*>(resource()->allocate(n * sizeof(T), alignof(T)));`.

## Parameters


### Parameters

- `n` - the number of objects to allocate storage for

## Return value

A pointer to the allocated storage.

## Exceptions

Throws `std::bad_array_new_length` if `n > std::numeric_limits<std::size_t>::max() / sizeof(T)`; may also throw any exceptions thrown by the call to `resource()->allocate`.

## Defect reports


## See also


| cpp/memory/polymorphic_allocator/dsc allocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc new_object | (see dedicated page) |
| cpp/memory/allocator traits/dsc allocate | (see dedicated page) |
| cpp/memory/memory resource/dsc allocate | (see dedicated page) |

