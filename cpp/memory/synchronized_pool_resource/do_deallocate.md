---
title: std::pmr::synchronized_pool_resource::do_deallocate
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/synchronized_pool_resource/do_deallocate
---

ddcl|since=c++17|1=
virtual void do_deallocate( void* p, std::size_t bytes, std::size_t alignment );
Returns the memory at `p` to the pool. It is unspecified if or under what circumstances this operation will result in a call to `deallocate()` on the upstream memory resource.

## Exceptions

Throws nothing.

## See also


| cpp/memory/memory_resource/dsc deallocate | (see dedicated page) |
| cpp/memory/memory_resource/dsc do_deallocate | (see dedicated page) |

