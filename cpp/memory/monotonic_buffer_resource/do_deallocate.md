---
title: std::pmr::monotonic_buffer_resource::do_deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/monotonic_buffer_resource/do_deallocate
---

ddcl|since=c++17 |1=
virtual void do_deallocate( void* p, std::size_t bytes, std::size_t alignment );
This function has no effect. Memory used by a `monotonic_buffer_resource`, as its name indicates, increases monotonically until the resource is destroyed.

## Exceptions

Throws nothing.

## See also


|  cpp/memory/memory_resource/dsc deallocate | (see dedicated page) |
|  cpp/memory/memory_resource/dsc do_deallocate | (see dedicated page) |

