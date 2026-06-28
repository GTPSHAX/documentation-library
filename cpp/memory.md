---
title: Dynamic memory management
type: Utilities
source: https://en.cppreference.com/w/cpp/memory
---


# Memory management library


## Smart pointers <sup>(C++11)</sup>

Smart pointers enable automatic, exception-safe, object lifetime management.


| memory | |

#### Pointer categories

| cpp/memory/dsc unique_ptr | (see dedicated page) |
| cpp/memory/dsc shared_ptr | (see dedicated page) |
| cpp/memory/dsc weak_ptr | (see dedicated page) |
| cpp/memory/dsc auto_ptr | (see dedicated page) |

#### Helper classes

| cpp/memory/dsc owner_less | (see dedicated page) |
| cpp/memory/dsc owner_hash | (see dedicated page) |
| cpp/memory/dsc owner_equal | (see dedicated page) |
| cpp/memory/dsc enable_shared_from_this | (see dedicated page) |
| cpp/memory/dsc bad_weak_ptr | (see dedicated page) |
| cpp/memory/dsc default_delete | (see dedicated page) |

#### Smart pointer adaptors {{mark since c++23

| cpp/memory/dsc out_ptr_t | (see dedicated page) |
| cpp/memory/out_ptr_t/dsc out_ptr | (see dedicated page) |
| cpp/memory/dsc inout_ptr_t | (see dedicated page) |
| cpp/memory/inout_ptr_t/dsc inout_ptr | (see dedicated page) |


## Allocators

Allocators are class templates encapsulating memory allocation strategy. This allows generic containers to decouple memory management from the data itself.


| memory | |
| cpp/memory/dsc allocator | (see dedicated page) |
| cpp/memory/dsc allocator_traits | (see dedicated page) |
| cpp/memory/dsc allocation_result | (see dedicated page) |
| cpp/memory/dsc allocator_arg | (see dedicated page) |
| cpp/memory/dsc uses_allocator | (see dedicated page) |
| cpp/memory/dsc uses_allocator_construction_args | (see dedicated page) |
| cpp/memory/dsc make_obj_using_allocator | (see dedicated page) |
| cpp/memory/dsc uninitialized_construct_using_allocator | (see dedicated page) |
| scoped_allocator | |
| cpp/memory/dsc scoped_allocator_adaptor | (see dedicated page) |
| memory_resource | |
| std::pmr | |
| cpp/memory/dsc polymorphic_allocator | (see dedicated page) |


## Memory resources <sup>(C++17)</sup>

Memory resources implement memory allocation strategies that can be used by `std::pmr::polymorphic_allocator`.


| memory_resource | |
| std::pmr | |
| cpp/memory/dsc memory_resource | (see dedicated page) |
| cpp/memory/dsc new_delete_resource | (see dedicated page) |
| cpp/memory/dsc null_memory_resource | (see dedicated page) |
| cpp/memory/dsc get_default_resource | (see dedicated page) |
| cpp/memory/dsc set_default_resource | (see dedicated page) |
| cpp/memory/dsc pool_options | (see dedicated page) |
| cpp/memory/dsc synchronized_pool_resource | (see dedicated page) |
| cpp/memory/dsc unsynchronized_pool_resource | (see dedicated page) |
| cpp/memory/dsc monotonic_buffer_resource | (see dedicated page) |


## Specialized `<memory>` algorithms


## Explicit lifetime management <sup>(C++23)</sup>


| memory | |
| cpp/memory/dsc start_lifetime_as | (see dedicated page) |


## Types for composite class design <sup>(C++26)</sup>


| memory | |
| cpp/memory/dsc indirect | (see dedicated page) |
| cpp/memory/dsc polymorphic | (see dedicated page) |


## Miscellaneous


| memory | |
| cpp/memory/dsc pointer_traits | (see dedicated page) |
| cpp/memory/dsc to_address | (see dedicated page) |
| cpp/memory/dsc addressof | (see dedicated page) |
| cpp/memory/dsc align | (see dedicated page) |
| cpp/memory/dsc assume_aligned | (see dedicated page) |
| cpp/memory/dsc is_sufficiently_aligned | (see dedicated page) |


## Low level memory management

Includes e.g. `operator new`, `operator delete`, `std::set_new_handler`.


| new | |


## C-style memory management

Includes e.g. `std::malloc`, `std::free`.


| cstdlib | |


## Uninitialized storage <sup>(until C++20)</sup>

Several utilities are provided to create and access raw storage.


| memory | |
| cpp/memory/dsc raw_storage_iterator | (see dedicated page) |
| cpp/memory/dsc get_temporary_buffer | (see dedicated page) |
| cpp/memory/dsc return_temporary_buffer | (see dedicated page) |


## Garbage collector support <sup>(until C++23)</sup>


| memory | |
| cpp/memory/gc/dsc declare_reachable | (see dedicated page) |
| cpp/memory/gc/dsc undeclare_reachable | (see dedicated page) |
| cpp/memory/gc/dsc declare_no_pointers | (see dedicated page) |
| cpp/memory/gc/dsc undeclare_no_pointers | (see dedicated page) |
| cpp/memory/gc/dsc pointer_safety | (see dedicated page) |
| cpp/memory/gc/dsc get_pointer_safety | (see dedicated page) |

