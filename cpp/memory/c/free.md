---
title: std::free
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/c/free
---

ddcl|header=cstdlib|
void free( void* ptr );
Deallocates the space previously allocated by `std::malloc`, `std::calloc`<sup>(since C++17)</sup> , `std::aligned_alloc`, or `std::realloc`.
If `ptr` is a null pointer, the function does nothing.
The behavior is undefined if the value of `ptr` does not equal a value returned earlier by `std::malloc`, `std::calloc`<sup>(since C++17)</sup> , `std::aligned_alloc`, or `std::realloc`.
The behavior is undefined if the memory area referred to by `ptr` has already been deallocated, that is, `std::free` or `std::realloc` has already been called with `ptr` as the argument and no calls to `std::malloc`, `std::calloc`<sup>(since C++17)</sup> , `std::aligned_alloc`, or `std::realloc` resulted in a pointer equal to `ptr` afterwards.
The behavior is undefined if after `std::free` returns, an access is made through the pointer `ptr` (unless another allocation function happened to result in a pointer value equal to `ptr`).

## Parameters


### Parameters

- `ptr` - pointer to the memory to deallocate

## Return value

(none)

## Notes

The function accepts (and does nothing with) the null pointer to reduce the amount of special-casing. Whether allocation succeeds or not, the pointer returned by an allocation function can be passed to `std::free`.

## Example


## See also

