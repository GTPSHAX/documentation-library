---
title: std::get_temporary_buffer
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/get_temporary_buffer
---


```cpp
**Header:** `<`memory`>`
dcl|until=c++11|1=
template< class T >
std::pair<T*, std::ptrdiff_t>
get_temporary_buffer( std::ptrdiff_t count );
dcl|since=c++11|deprecated=c++17|removed=c++20|1=
template< class T >
std::pair<T*, std::ptrdiff_t>
get_temporary_buffer( std::ptrdiff_t count ) noexcept;
```

If `count` is negative or zero, does nothing.
Otherwise, requests to allocate uninitialized contiguous storage for `count` adjacent objects of type `T`. The request is non-binding, and the implementation may instead allocate the storage for any other number of (including zero) adjacent objects of type `T`.
rrev|since=c++11|
It is implementation-defined whether over-aligned types are supported.

## Parameters


### Parameters

- `count` - the desired number of objects

## Return value

A `std::pair`, the member `first` is a pointer to the beginning of the allocated storage and the member `second` is the number of objects that fit in the storage that was actually allocated.
If `1=count <= 0` or allocated storage is not enough to store a single element of type `T`, the member `first` of the result is a null pointer and the member `second` is zero.

## Notes

This API was originally designed with the intent of providing a more efficient implementation than the general-purpose `operator new`, but no such implementation was created and the API was deprecated and removed.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2072 | C++98 | it was not allowed to allocate insufficient memory | allowed |


## See also


| cpp/memory/dsc return_temporary_buffer | (see dedicated page) |
| cpp/memory/allocator_traits/dsc allocate_at_least | (see dedicated page) |

