---
title: std::pmr::polymorphic_allocator
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/polymorphic_allocator
---


```cpp
**Header:** `<`memory_resource`>`
dcl rev multi
|since1=c++17|dcl1=
template< class T >
class polymorphic_allocator;
|since2=c++20|dcl2=
template< class T = std::byte >
class polymorphic_allocator;
```

The class template `std::pmr::polymorphic_allocator` is an *Allocator* which exhibits different allocation behavior depending upon the `std::pmr::memory_resource` from which it is constructed. Since `memory_resource` uses runtime polymorphism to manage allocations, different container instances with `polymorphic_allocator` as their static allocator type are interoperable, but can behave as if they had different allocator types.
All specializations of `polymorphic_allocator` meet the .
The `polymorphic_allocator::construct` member function does , so that the elements of a container using a `polymorphic_allocator` will use that same allocator for their own allocations. For example, a `std::pmr::vector<std::pmr::string>` will use the same `memory_resource` for the `vector`'s storage and each `string`'s storage.
For non-polymorphic allocators, similar propagation can be achieved with the help of `std::scoped_allocator_adaptor`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | definition |


## Member functions


| cpp/memory/polymorphic_allocator/dsc constructor | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc destructor | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc operator{{= | (see dedicated page) |

#### Public member functions

| cpp/memory/polymorphic_allocator/dsc allocate | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc deallocate | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc construct | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc destroy | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc deallocate_bytes | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc deallocate_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc new_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc delete_object | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc select_on_container_copy_construction | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc resource | (see dedicated page) |


## Non-member functions


| cpp/memory/polymorphic_allocator/dsc operator eq | (see dedicated page) |


## Notes

`polymorphic_allocator` does not propagate on container copy assignment, move assignment, or swap. As a result, move assignment of a `polymorphic_allocator`-using container can throw, and swapping two `polymorphic_allocator`-using containers whose allocators do not compare equal results in undefined behavior.

## See also


| cpp/memory/dsc memory_resource | (see dedicated page) |

