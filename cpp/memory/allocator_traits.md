---
title: std::allocator_traits
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/allocator_traits
---

ddcl|header=memory|since=c++11|
template< class Alloc >
struct allocator_traits;
The `allocator_traits` class template provides the standardized way to access various properties of *Allocator*s. The standard containers and other standard library components access allocators through this template, which makes it possible to use any class type as an allocator, as long as the user-provided specialization of `std::allocator_traits` implements all required functionality.
rrev|since=c++23|
A program that declares an explicit or partial specialization of `std::allocator_traits` is ill-formed, no diagnostic required.
The default, non-specialized, `std::allocator_traits` contains the following members:

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member alias templates


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/memory/allocator_traits/dsc allocate | (see dedicated page) |
| cpp/memory/allocator_traits/dsc allocate_at_least | (see dedicated page) |
| cpp/memory/allocator_traits/dsc deallocate | (see dedicated page) |
| cpp/memory/allocator_traits/dsc construct | (see dedicated page) |
| cpp/memory/allocator_traits/dsc destroy | (see dedicated page) |
| cpp/memory/allocator_traits/dsc max_size | (see dedicated page) |
| cpp/memory/allocator_traits/dsc select_on_container_copy_construction | (see dedicated page) |


## Defect reports


## See also


| cpp/memory/dsc allocator | (see dedicated page) |
| cpp/memory/dsc scoped_allocator_adaptor | (see dedicated page) |
| cpp/memory/dsc pointer_traits | (see dedicated page) |

