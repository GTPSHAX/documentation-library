---
title: std::forward_list
type: Containers
source: https://en.cppreference.com/w/cpp/container/forward_list
---


```cpp
**Header:** `<`forward_list`>`
dcl|since=c++11|num=1|1=
template<
class T,
class Allocator = std::allocator<T>
> class forward_list;
dcl|since=c++17|num=2|1=
namespace pmr {
template< class T >
using forward_list = std::forward_list<T, std::pmr::polymorphic_allocator<T>>;
}
```

`std::forward_list` is a container that supports fast insertion and removal of elements from anywhere in the container. Fast random access is not supported. It is implemented as a singly-linked list. Compared to `std::list` this container provides more space efficient storage when bidirectional iteration is not needed.
Adding, removing and moving the elements within the list, or across several lists, does not invalidate the iterators currently referring to other elements in the list. However, an iterator or reference referring to an element is invalidated when the corresponding element is removed (via `erase_after`) from the list.
`std::forward_list` meets the requirements of *Container* (except for the `size` member function and that `1=operator==`'s complexity is always linear), *AllocatorAwareContainer* and *SequenceContainer*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc value_type|forward_list | (see dedicated page) |
| cpp/container/dsc allocator_type|forward_list | (see dedicated page) |
| cpp/container/dsc size_type|forward_list | (see dedicated page) |
| cpp/container/dsc difference_type|forward_list | (see dedicated page) |
| cpp/container/dsc reference|forward_list | (see dedicated page) |
| cpp/container/dsc const_reference|forward_list | (see dedicated page) |
| cpp/container/dsc pointer|forward_list | (see dedicated page) |
| cpp/container/dsc const_pointer|forward_list | (see dedicated page) |
| cpp/container/dsc iterator|forward_list | (see dedicated page) |
| cpp/container/dsc const_iterator|forward_list | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|forward_list | (see dedicated page) |
| cpp/container/dsc destructor|forward_list | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc assign|forward_list | (see dedicated page) |
| cpp/container/dsc assign_range|forward_list | (see dedicated page) |
| cpp/container/dsc get_allocator|forward_list | (see dedicated page) |

#### Element access

| cpp/container/dsc front|forward_list | (see dedicated page) |

#### Iterators

| cpp/container/dsc before_begin|forward_list | (see dedicated page) |
| cpp/container/dsc begin|forward_list | (see dedicated page) |
| cpp/container/dsc end|forward_list | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|forward_list | (see dedicated page) |
| cpp/container/dsc max_size|forward_list | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|forward_list | (see dedicated page) |
| cpp/container/dsc insert_after|forward_list | (see dedicated page) |
| cpp/container/dsc emplace_after|forward_list | (see dedicated page) |
| cpp/container/dsc insert_range_after|forward_list | (see dedicated page) |
| cpp/container/dsc erase_after|forward_list | (see dedicated page) |
| cpp/container/dsc push_front|forward_list | (see dedicated page) |
| cpp/container/dsc emplace_front|forward_list | (see dedicated page) |
| cpp/container/dsc prepend_range|forward_list | (see dedicated page) |
| cpp/container/dsc pop_front|forward_list | (see dedicated page) |
| cpp/container/dsc resize|forward_list | (see dedicated page) |
| cpp/container/dsc swap|forward_list | (see dedicated page) |

#### Operations

| cpp/container/dsc merge|forward_list | (see dedicated page) |
| cpp/container/dsc splice_after|forward_list | (see dedicated page) |
| cpp/container/dsc remove|forward_list | (see dedicated page) |
| cpp/container/dsc reverse|forward_list | (see dedicated page) |
| cpp/container/dsc unique|forward_list | (see dedicated page) |
| cpp/container/dsc sort|forward_list | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|forward_list | (see dedicated page) |
| cpp/container/dsc swap2|forward_list | (see dedicated page) |
| cpp/container/dsc erase seq|forward_list | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


## Example

