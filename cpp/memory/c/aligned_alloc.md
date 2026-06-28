---
title: std::aligned_alloc
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/c/aligned_alloc
---

ddcl|header=cstdlib|since=c++17|
void* aligned_alloc( std::size_t alignment, std::size_t size );
Allocate `size` bytes of uninitialized storage whose alignment is specified by `alignment` (implicitly creating objects in the destination area). The `size` parameter must be an integral multiple of `alignment`.

## Parameters


### Parameters

- `alignment` - specifies the alignment. Must be a valid alignment supported by the implementation.
- `size` - number of bytes to allocate. An integral multiple of `alignment`.

## Return value

On success, returns the pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with `std::free` or `std::realloc`.
On failure, returns a null pointer.

## Notes

Passing a `size` which is not an integral multiple of `alignment` or an `alignment` which is not valid or not supported by the implementation causes the function to fail and return a null pointer (C11, as published, specified undefined behavior in this case, this was corrected by ).
As an example of the "supported by the implementation" requirement, POSIX function [https://pubs.opengroup.org/onlinepubs/9699919799/functions/posix_memalign.html `posix_memalign`] accepts any `alignment` that is a power of two and a multiple of `sizeof(void*)`, and POSIX-based implementations of `aligned_alloc` inherit this requirements.
Fundamental alignments are always supported. If `alignment` is a power of two and not greater than `alignof(std::max_align_t)`, `aligned_alloc` may simply call `std::malloc`.
Regular `std::malloc` aligns memory suitable for any object type with a fundamental alignment.  This function is useful for over-aligned allocations, such as to [Streaming SIMD Extensions|SSE](https://en.wikipedia.org/wiki/Streaming SIMD Extensions|SSE), cache line, or [Page (computer memory)#Multiple page sizes|VM page](https://en.wikipedia.org/wiki/Page (computer memory)#Multiple page sizes|VM page) boundary.
This function is not supported in Microsoft C Runtime library because its implementation of `std::free` is [https://learn.microsoft.com/en-us/cpp/standard-library/cstdlib#remarks-6 unable to handle aligned allocations] of any kind. Instead, MS CRT provides [https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-malloc `_aligned_malloc`] (to be freed with [https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-free `_aligned_free`]).

## Example


### Example


**Output:**
```
default-aligned address:   0x2221c20
1024-byte aligned address: 0x2222400
```


## See also


| cpp/types/dsc aligned_storage | (see dedicated page) |

