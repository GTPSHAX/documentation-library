---
title: std::pmr::get_default_resource
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/get_default_resource
---

ddcl|header=memory_resource | since=c++17|
std::pmr::memory_resource* get_default_resource() noexcept;
Gets the default memory resource pointer.
The ''default memory resource pointer'' is used by certain facilities when an explicit memory resource is not supplied. The initial default memory resource pointer is the return value of `std::pmr::new_delete_resource`.
This function is thread-safe. Previous call to `std::pmr::set_default_resource` ''synchronizes with'' (see `std::memory_order`) the subsequent `std::pmr::get_default_resource` calls.

## Return value

Returns the value of the default memory resource pointer.

## See also


| cpp/memory/dsc set_default_resource | (see dedicated page) |
| cpp/memory/dsc new_delete_resource | (see dedicated page) |

