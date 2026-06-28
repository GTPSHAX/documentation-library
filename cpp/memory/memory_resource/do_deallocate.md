---
title: std::pmr::memory_resource::do_deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/do_deallocate
---

ddcl|since=c++17|1=
virtual void do_deallocate( void* p, std::size_t bytes, std::size_t alignment ) = 0;
Deallocates the storage pointed to by `p`.
`p` must have been returned by a prior call to `allocate(bytes, alignment)` on a `memory_resource` that compares equal to `*this`, and the storage it points to must not yet have been deallocated, otherwise the behavior is undefined.

## Exceptions

Throws nothing.

## See also


| cpp/memory/memory_resource/dsc deallocate | (see dedicated page) |

