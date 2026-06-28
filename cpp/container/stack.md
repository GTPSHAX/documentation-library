---
title: std::stack
type: Containers
source: https://en.cppreference.com/w/cpp/container/stack
---

ddcl|header=stack|1=
template<
class T,
class Container = std::deque<T>
> class stack;
The `std::stack` class is a container adaptor that gives the programmer the functionality of a [Stack (abstract data type)|stack](https://en.wikipedia.org/wiki/Stack (abstract data type)|stack) - specifically, a LIFO (last-in, first-out) data structure.
The class template acts as a wrapper to the underlying container - only a specific set of functions is provided. The stack pushes and pops the element from the back of the underlying container, known as the top of the stack.

## Template parameters


### Parameters

- `T` - The type of the stored elements. The program is ill-formed if `T` is not the same type as `Container::value_type`.
- `Container` - The type of the underlying container to use to store the elements. The container must satisfy the requirements of *SequenceContainer*. Additionally, it must provide the following functions with the usual semantics:
- * `back()`, e.g., `std::vector::back()`,
- * `push_back()`, e.g., `std::deque::push_back()`,
- * `pop_back()`, e.g., `std::list::pop_back()`.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc container_type|stack | (see dedicated page) |
| cpp/container/dsc value_type|stack | (see dedicated page) |
| cpp/container/dsc size_type|stack | (see dedicated page) |
| cpp/container/dsc reference|stack | (see dedicated page) |
| cpp/container/dsc const_reference|stack | (see dedicated page) |


## Member objects


| Item | Description |
|------|-------------|
| **Member** | Description |
| cpp/container/dsc c|stack | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|stack | (see dedicated page) |
| cpp/container/dsc destructor|stack | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |

#### Element access

| cpp/container/dsc top|stack | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|stack | (see dedicated page) |
| cpp/container/dsc size|stack | (see dedicated page) |

#### Modifiers

| cpp/container/dsc push|stack | (see dedicated page) |
| cpp/container/dsc push_range|stack | (see dedicated page) |
| cpp/container/dsc emplace|stack | (see dedicated page) |
| cpp/container/dsc pop|stack | (see dedicated page) |
| cpp/container/dsc swap|stack | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|stack | (see dedicated page) |
| cpp/container/dsc swap2|stack | (see dedicated page) |


## Helper classes


| cpp/container/dsc uses_allocator|stack | (see dedicated page) |
| cpp/container/dsc adaptor_formatter|stack | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_stack` | 202502L | C++26 | Constexpr `std::stack` |


## Example


## Defect reports


## See also


| cpp/container/dsc vector | (see dedicated page) |
| cpp/container/dsc vector bool | (see dedicated page) |
| cpp/container/dsc deque | (see dedicated page) |
| cpp/container/dsc list | (see dedicated page) |

