---
title: std::allocator_traits::allocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits/allocate
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|anchor=no|since=c++11|constexpr=c++20|
static pointer allocate( Alloc& a, size_type n );
dcla|num=2|anchor=no|since=c++11|constexpr=c++20|
static pointer allocate( Alloc& a, size_type n, const_void_pointer hint );
```

Uses the allocator `a` to allocate `n * sizeof(Alloc::value_type)` bytes of uninitialized storage. An array of type `Alloc::value_type[n]` is created in the storage, but none of its elements are constructed.
1. Calls `a.allocate(n)`.
2. Additionally passes memory locality hint `hint`. Calls `a.allocate(n, hint)` if possible. If not possible (e.g. `a` has no two-argument member function `allocate`), calls `a.allocate(n)`.

## Parameters


### Parameters

- `a` - allocator to use
- `n` - the number of objects to allocate storage for
- `hint` - pointer to a nearby memory location

## Return value

The pointer returned by the call to `a.allocate(n)`.

## Notes

`Alloc::allocate` was not required to create array object until `P0593R6`, which made using non-default allocator for `std::vector` and some other containers not well-defined according to a strict reading of the core language specification.
After calling `allocate` and before construction of elements, pointer arithmetic of `Alloc::value_type*` is well-defined within the allocated array, but the behavior is undefined if elements are accessed.

## Example

