---
title: std::pmr::memory_resource::do_allocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/do_allocate
---

ddcl|since=c++17|1=
virtual void* do_allocate( std::size_t bytes, std::size_t alignment ) = 0;
Allocates storage with a size of at least `bytes` bytes, aligned to the specified `alignment`.
`alignment` shall be a power of two.

## Exceptions

Throws an exception if storage of the requested size and alignment cannot be obtained.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2843 | C++17 | handling of unsupported alignment contradictory | throws an exception |


## See also


| cpp/memory/memory_resource/dsc allocate | (see dedicated page) |

