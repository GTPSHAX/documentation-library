---
title: std::pmr::unsynchronized_pool_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/unsynchronized_pool_resource
---

ddcl|header=memory_resource|since=c++17|
class unsynchronized_pool_resource : public std::pmr::memory_resource;
The class `std::pmr::unsynchronized_pool_resource` is a general-purpose memory resource class with the following properties:
* It owns the allocated memory and frees it on destruction, even if `deallocate` has not been called for some of the allocated blocks.
* It consists of a collection of ''pools'' that serves requests for different block sizes. Each pool manages a collection of ''chunks'' that are then divided into blocks of uniform size.
* Calls to `cpp/memory/unsynchronized_pool_resource/do_allocate` are dispatched to the pool serving the smallest blocks accommodating the requested size.
* Exhausting memory in the pool causes the next allocation request for that pool to allocate an additional chunk of memory from the ''upstream allocator'' to replenish the pool. The chunk size obtained increases geometrically.
* Allocations requests that exceed the largest block size are served from the ''upstream allocator'' directly.
* The largest block size and maximum chunk size may be tuned by passing a `std::pmr::pool_options` struct to its constructor.
`unsynchronized_pool_resource` is not thread-safe, and cannot be accessed from multiple threads simultaneously; use `cpp/memory/synchronized_pool_resource` if access from multiple threads is required.

## Member functions


| cpp/memory/unsynchronized_pool_resource/dsc constructor | (see dedicated page) |
| cpp/memory/unsynchronized_pool_resource/dsc destructor | (see dedicated page) |
| cpp/memory/unsynchronized_pool_resource/dsc operator{{= | (see dedicated page) |

#### Public member functions

| cpp/memory/unsynchronized_pool_resource/dsc release | (see dedicated page) |
| cpp/memory/unsynchronized_pool_resource/dsc upstream_resource | (see dedicated page) |
| cpp/memory/unsynchronized_pool_resource/dsc options | (see dedicated page) |

#### Protected member functions

| cpp/memory/unsynchronized_pool_resource/dsc do_allocate | (see dedicated page) |
| cpp/memory/unsynchronized_pool_resource/dsc do_deallocate | (see dedicated page) |
| cpp/memory/unsynchronized_pool_resource/dsc do_is_equal | (see dedicated page) |

