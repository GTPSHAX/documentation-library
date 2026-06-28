---
title: std::pmr::monotonic_buffer_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/monotonic_buffer_resource
---

ddcl|header=memory_resource|since=c++17|
class monotonic_buffer_resource : public std::pmr::memory_resource;
The class `std::pmr::monotonic_buffer_resource` is a special-purpose memory resource class that releases the allocated memory only when the resource is destroyed. It is intended for very fast memory allocations in situations where memory is used to build up a few objects and then is released all at once.
`monotonic_buffer_resource` can be constructed with an initial buffer. If there is no initial buffer, or if the buffer is exhausted, additional buffers are obtained from an ''upstream memory resource'' supplied at construction. The size of buffers obtained follows a geometric progression.
`monotonic_buffer_resource` is not thread-safe.

## Member functions


| cpp/memory/monotonic_buffer_resource/dsc constructor | (see dedicated page) |
| cpp/memory/monotonic_buffer_resource/dsc destructor | (see dedicated page) |
| cpp/memory/monotonic_buffer_resource/dsc operator{{= | (see dedicated page) |

#### Public member functions

| cpp/memory/monotonic_buffer_resource/dsc release | (see dedicated page) |
| cpp/memory/monotonic_buffer_resource/dsc upstream_resource | (see dedicated page) |

#### Protected member functions

| cpp/memory/monotonic_buffer_resource/dsc do_allocate | (see dedicated page) |
| cpp/memory/monotonic_buffer_resource/dsc do_deallocate | (see dedicated page) |
| cpp/memory/monotonic_buffer_resource/dsc do_is_equal | (see dedicated page) |


## Example

The program measures the time of creating huge double-linked lists using the following allocators:
* default standard allocator,
* default `pmr` allocator,
* `pmr` allocator with monotonic resource but without explicit memory buffer,
* `pmr` allocator with monotonic resource and external memory buffer (on stack).

### Example


**Output:**
```
t1 (default std alloc): 0.720 sec; t1/t1: 1.000
t2 (default pmr alloc): 0.915 sec; t1/t2: 0.787
t3 (pmr alloc  no buf): 0.370 sec; t1/t3: 1.945
t4 (pmr alloc and buf): 0.247 sec; t1/t4: 2.914
```

