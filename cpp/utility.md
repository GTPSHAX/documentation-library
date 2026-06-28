---
title: Utility library
type: Utilities
source: https://en.cppreference.com/w/cpp/utility
---


# Utility library

C++ includes a variety of utility libraries that provide functionality ranging from  to . These libraries can be broadly divided into two groups:
* language support libraries, and
* general-purpose libraries.

# Language support

Language support libraries provide classes and functions that interact closely with language features and support common language idioms.

## <sup>(C++20)</sup>

The header  supplies implementation-dependent information about the C++ standard library (such as the version number and release date). It also defines the .

## Type support

Basic types (e.g. `std::size_t`, `std::nullptr_t`), RTTI (e.g. `std::type_info`)

## 

Termination (e.g. `std::abort`, `std::atexit`), environment (e.g. `std::system`), signals (e.g. `std::raise`).

## Dynamic memory management

Smart pointers (e.g. `std::shared_ptr`), allocators (e.g. `std::allocator` or `std::pmr::memory_resource`), C-style memory management (e.g. `std::malloc`).

## Error handling

Exceptions (e.g. `std::exception`, `std::terminate`), assertions (e.g. `assert`).

## 

Support for functions that take an arbitrary number of parameters (via e.g. `va_start`, `va_arg`, `va_end`).

## <sup>(C++11)</sup>


| initializer_list | |
| cpp/utility/dsc initializer_list | (see dedicated page) |


## <sup>(C++20)</sup>


| source_location | |
| cpp/utility/dsc source_location | (see dedicated page) |


## Three-way comparison <sup>(C++20)</sup>


| compare | |
| cpp/utility/compare/dsc three_way_comparable | (see dedicated page) |
| cpp/utility/compare/dsc partial_ordering | (see dedicated page) |
| cpp/utility/compare/dsc weak_ordering | (see dedicated page) |
| cpp/utility/compare/dsc strong_ordering | (see dedicated page) |
| cpp/utility/compare/dsc named_comparison_functions | (see dedicated page) |
| cpp/utility/compare/dsc compare_three_way | (see dedicated page) |
| cpp/utility/compare/dsc compare_three_way_result | (see dedicated page) |
| cpp/utility/compare/dsc common_comparison_category | (see dedicated page) |
| cpp/utility/compare/dsc strong_order | (see dedicated page) |
| cpp/utility/compare/dsc weak_order | (see dedicated page) |
| cpp/utility/compare/dsc partial_order | (see dedicated page) |
| cpp/utility/compare/dsc compare_strong_order_fallback | (see dedicated page) |
| cpp/utility/compare/dsc compare_weak_order_fallback | (see dedicated page) |
| cpp/utility/compare/dsc compare_partial_order_fallback | (see dedicated page) |
| cpp/utility/compare/dsc type_order | (see dedicated page) |


## Coroutine support <sup>(C++20)</sup>

Types for coroutine support (e.g. `std::coroutine_traits`, `std::coroutine_handle`).

## Contract support <sup>(C++26)</sup>

Types for contract support (e.g. `cpp/contract/contract_violation|std::contracts::contract_violation`).

# General-purpose utilities


## Swap


| utility | |
| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/utility/dsc exchange | (see dedicated page) |
| concepts | |
| cpp/utility/ranges/dsc swap | (see dedicated page) |


## Type operations <sup>(C++11)</sup>


| utility | |
| cpp/utility/dsc forward | (see dedicated page) |
| cpp/utility/dsc forward_like | (see dedicated page) |
| cpp/utility/dsc move | (see dedicated page) |
| cpp/utility/dsc move_if_noexcept | (see dedicated page) |
| cpp/utility/dsc as_const | (see dedicated page) |
| cpp/utility/dsc declval | (see dedicated page) |
| cpp/utility/dsc to_underlying | (see dedicated page) |


## Integer comparison functions <sup>(C++20)</sup>


| utility | |
| cpp/utility/dsc intcmp | (see dedicated page) |
| cpp/utility/dsc in_range | (see dedicated page) |


## Relational operators <sup>(until C++20)</sup>


| utility | |
| std::rel_ops | |
| cpp/utility/rel_ops/dsc operator_cmp | (see dedicated page) |


## Construction tags <sup>(C++11)</sup>


| utility | |
| cpp/utility/dsc piecewise_construct | (see dedicated page) |
| cpp/utility/dsc in_place | (see dedicated page) |
| cpp/utility/dsc nontype | (see dedicated page) |


## and


| utility | |
| cpp/utility/dsc pair | (see dedicated page) |
| tuple | |
| cpp/utility/dsc tuple | (see dedicated page) |
| cpp/utility/dsc apply | (see dedicated page) |
| cpp/utility/dsc make_from_tuple | (see dedicated page) |

#### {{rl|tuple/tuple-like|Tuple protocol

| tuple | |
| utility | |
| array | |
| ranges | |
| complex | |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/utility/dsc tuple_element | (see dedicated page) |


## Sum types and type erased wrappers <sup>(C++17)</sup>


| optional | |
| cpp/utility/dsc optional | (see dedicated page) |
| expected | |
| cpp/utility/dsc expected | (see dedicated page) |
| variant | |
| cpp/utility/dsc variant | (see dedicated page) |
| any | |
| cpp/utility/dsc any | (see dedicated page) |


## 


| bitset | |
| cpp/utility/dsc bitset | (see dedicated page) |


## <sup>(C++20)</sup>

The header  provides several function templates to access, manipulate, and process individual bits and bit sequences. The byte ordering (endianness) of scalar types can be inspected via `std::endian` facility.

## <sup>(C++11)</sup>

Partial function application (e.g. `std::bind`) and related utilities: utilities for binding such as `std::ref`  and `std::placeholders`, polymorphic function wrappers: `std::function`, predefined functors (e.g. `std::plus`, `std::equal_to`), pointer-to-member to function converters `std::mem_fn`.

## <sup>(C++11)</sup>


| functional | |
| cpp/utility/dsc hash | (see dedicated page) |


## See also

