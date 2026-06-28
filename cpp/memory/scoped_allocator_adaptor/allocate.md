---
title: std::scoped_allocator_adaptor::allocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/scoped_allocator_adaptor/allocate
---


```cpp
**Header:** `<`scoped_allocator`>`
dcl|num=1|since=c++11|
pointer allocate( size_type n );
dcl|num=2|since=c++11|
pointer allocate( size_type n, const_void_pointer hint );
```

Uses the outer allocator to allocate uninitialized storage.
1. Calls `std::allocator_traits<OuterAlloc>::allocate(outer_allocator(), n)`.
2. Additionally provides memory locality hint, by calling `std::allocator_traits<OuterAlloc>::allocate(outer_allocator(), n, hint)`.

## Parameters


### Parameters

- `n` - the number of objects to allocate storage for
- `hint` - pointer to a nearby memory location

## Return value

The pointer to the allocated storage.

## See also


| cpp/memory/allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator_traits/dsc allocate | (see dedicated page) |

