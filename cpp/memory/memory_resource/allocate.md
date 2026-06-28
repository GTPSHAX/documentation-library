---
title: std::pmr::memory_resource::allocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/allocate
---


```cpp
dcl|since=c++17|1=
void* allocate( std::size_t bytes,
std::size_t alignment = alignof(std::max_align_t) );
```

Allocates storage with a size of at least `bytes` bytes, aligned to the specified `alignment`.
Equivalent to `return do_allocate(bytes, alignment);`.

## Exceptions

Throws an exception if storage of the requested size and alignment cannot be obtained.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2843 | C++17 | over-alignment was allowed to be unsupported | alignment must be honoured |


## See also


| cpp/memory/memory_resource/dsc do_allocate | (see dedicated page) |

