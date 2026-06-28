---
title: std::pmr::memory_resource::deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/memory_resource/deallocate
---

ddcl|since=c++17|1=
void deallocate( void* p,
std::size_t bytes,
std::size_t alignment = alignof(std::max_align_t) );
Deallocates the storage pointed to by `p`. `p` shall have been returned by a prior call to `allocate(bytes, alignment)` on a `memory_resource` that compares equal to `*this`, and the storage it points to shall not yet have been deallocated.
Equivalent to `do_deallocate(p, bytes, alignment);`.

## Exceptions

Throws nothing.

## See also


| cpp/memory/memory_resource/dsc do_deallocate | (see dedicated page) |

