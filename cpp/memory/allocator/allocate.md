---
title: std::allocator::allocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator/allocate
---


```cpp
dcl rev multi|num=1|until1=c++17|dcl1=
pointer allocate( size_type n, const void* hint = 0 );
|notes2=|dcl2=
T* allocate( std::size_t n, const void* hint );
dcl rev multi|num=2|since1=c++17|dcl1=
T* allocate( std::size_t n );
|since2=c++20|dcl2=
constexpr T* allocate( std::size_t n );
```

Allocates `n * sizeof(T)` bytes of uninitialized storage by calling `::operator new(std::size_t)` <sup>(since C++17)</sup> or `::operator new(std::size_t, std::align_val_t)`, but it is unspecified when and how this function is called. The pointer `hint` may be used to provide locality of reference: the allocator, if supported by the implementation, will attempt to allocate the new memory block as close as possible to `hint`.
Then, this function creates an array of type `T[n]` in the storage and starts its lifetime, but does not start lifetime of any of its elements.
Use of this function is ill-formed if `T` is an incomplete type.
rrev|since=c++20|
In order to use this function in a constant expression, the allocated storage must be deallocated within the evaluation of the same expression.

## Parameters


### Parameters

- `n` - the number of objects to allocate storage for
- `hint` - pointer to a nearby memory location

## Return value

Pointer to the first element of an array of `n` objects of type `T` whose elements have not been constructed yet.

## Exceptions

rrev|since=c++11|
Throws `std::bad_array_new_length` if `std::numeric_limits<std::size_t>::max() / sizeof(T) < n`.
Throws `std::bad_alloc` if allocation fails.

## Notes

The "unspecified when and how" wording makes it possible to combine or optimize away heap allocations made by the standard library containers, even though such optimizations are disallowed for direct calls to `::operator new`. For example, this is implemented by libc++ ([https://github.com/llvm-mirror/libcxx/blob/master@%7B2017-02-09%7D/include/memory#L1766-L1772] and [https://github.com/llvm-mirror/libcxx/blob/master@%7B2017-02-09%7D/include/new#L211-L217]).
After calling `allocate()` and before construction of elements, pointer arithmetic of `T*` is well-defined within the allocated array, but the behavior is undefined if elements are accessed.

## Defect reports


## See also


| cpp/memory/allocator_traits/dsc allocate | (see dedicated page) |

