---
title: std::unordered_multiset
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_multiset
---


```cpp
**Header:** `<`unordered_set`>`
dcl|num=1|since=c++11|1=
template<
class Key,
class Hash = std::hash<Key>,
class KeyEqual = std::equal_to<Key>,
class Allocator = std::allocator<Key>
> class unordered_multiset;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class Hash = std::hash<Key>,
class Pred = std::equal_to<Key>
> using unordered_multiset = std::unordered_multiset<Key, Hash, Pred,
std::pmr::polymorphic_allocator<Key>>;
}
```

`std::unordered_multiset` is an associative container that contains set of possibly non-unique objects of type Key. Search, insertion, and removal have average constant-time complexity.
Internally, the elements are not sorted in any particular order, but organized into buckets. Which bucket an element is placed into depends entirely on the hash of its value. This allows fast access to individual elements, since once hash is computed, it refers to the exact bucket the element is placed into.
The iteration order of this container is not required to be stable (so, for example, `std::equal` cannot be used to compare two `std::unordered_multiset`s), except that every group of elements whose keys compare ''equivalent'' (compare equal with `key_eq()` as the comparator) forms a contiguous subrange in the iteration order, also accessible with `equal_range()`.
`std::unordered_multiset` meets the requirements of *Container*, *AllocatorAwareContainer*, *UnorderedAssociativeContainer*.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|unordered_multiset | (see dedicated page) |
| cpp/container/dsc value_type|unordered_multiset | (see dedicated page) |
| cpp/container/dsc size_type|unordered_multiset | (see dedicated page) |
| cpp/container/dsc difference_type|unordered_multiset | (see dedicated page) |
| cpp/container/dsc hasher|unordered_multiset | (see dedicated page) |
| cpp/container/dsc key_equal|unordered_multiset | (see dedicated page) |
| cpp/container/dsc allocator_type|unordered_multiset | (see dedicated page) |
| cpp/container/dsc reference|unordered_multiset | (see dedicated page) |
| cpp/container/dsc const_reference|unordered_multiset | (see dedicated page) |
| cpp/container/dsc pointer|unordered_multiset | (see dedicated page) |
| cpp/container/dsc const_pointer|unordered_multiset | (see dedicated page) |
| cpp/container/dsc iterator|unordered_multiset | (see dedicated page) |
| cpp/container/dsc const_iterator|unordered_multiset | (see dedicated page) |
| cpp/container/dsc local_iterator|unordered_multiset | (see dedicated page) |
| cpp/container/dsc const_local_iterator|unordered_multiset | (see dedicated page) |
| cpp/container/dsc node_type|unordered_multiset | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|unordered_multiset | (see dedicated page) |
| cpp/container/dsc destructor|unordered_multiset | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|unordered_multiset | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|unordered_multiset | (see dedicated page) |
| cpp/container/dsc end|unordered_multiset | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|unordered_multiset | (see dedicated page) |
| cpp/container/dsc size|unordered_multiset | (see dedicated page) |
| cpp/container/dsc max_size|unordered_multiset | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|unordered_multiset | (see dedicated page) |
| cpp/container/dsc insert|unordered_multiset | (see dedicated page) |
| cpp/container/dsc insert_range|unordered_multiset | (see dedicated page) |
| cpp/container/dsc emplace|unordered_multiset | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_multiset | (see dedicated page) |
| cpp/container/dsc erase|unordered_multiset | (see dedicated page) |
| cpp/container/dsc swap|unordered_multiset | (see dedicated page) |
| cpp/container/dsc extract|unordered_multiset | (see dedicated page) |
| cpp/container/dsc merge|unordered_multiset | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|unordered_multiset | (see dedicated page) |
| cpp/container/dsc find|unordered_multiset | (see dedicated page) |
| cpp/container/dsc contains|unordered_multiset | (see dedicated page) |
| cpp/container/dsc equal_range|unordered_multiset | (see dedicated page) |

#### Bucket interface

| cpp/container/dsc begin(int)|unordered_multiset | (see dedicated page) |
| cpp/container/dsc end(int)|unordered_multiset | (see dedicated page) |
| cpp/container/dsc bucket_count|unordered_multiset | (see dedicated page) |
| cpp/container/dsc max_bucket_count|unordered_multiset | (see dedicated page) |
| cpp/container/dsc bucket_size|unordered_multiset | (see dedicated page) |
| cpp/container/dsc bucket|unordered_multiset | (see dedicated page) |

#### Hash policy

| cpp/container/dsc load_factor|unordered_multiset | (see dedicated page) |
| cpp/container/dsc max_load_factor|unordered_multiset | (see dedicated page) |
| cpp/container/dsc rehash|unordered_multiset | (see dedicated page) |
| cpp/container/dsc reserve|unordered_multiset | (see dedicated page) |

#### Observers

| cpp/container/dsc hash_function|unordered_multiset | (see dedicated page) |
| cpp/container/dsc key_eq|unordered_multiset | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp_unord|unordered_multiset | (see dedicated page) |
| cpp/container/dsc swap2|unordered_multiset | (see dedicated page) |
| cpp/container/dsc erase_if|unordered_multiset | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_unordered_set` | 202502L | C++26 | Constexpr `std::unordered_muliset` |


## Example


## See also


| cpp/container/dsc unordered_set | (see dedicated page) |
| cpp/container/dsc multiset | (see dedicated page) |
| cpp/container/dsc flat_multiset | (see dedicated page) |

