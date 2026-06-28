---
title: std::unordered_multimap
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_multimap
---


```cpp
**Header:** `<`unordered_map`>`
dcl|num=1|since=c++11|1=
template<
class Key,
class T,
class Hash = std::hash<Key>,
class KeyEqual = std::equal_to<Key>,
class Allocator = std::allocator<std::pair<const Key, T>>
> class unordered_multimap;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class T,
class Hash = std::hash<Key>,
class Pred = std::equal_to<Key>
> using unordered_multimap =
std::unordered_multimap<Key, T, Hash, Pred,
std::pmr::polymorphic_allocator<std::pair<const Key, T>>>;
}
```

`std::unordered_multimap` is an unordered associative container that supports equivalent keys (an unordered_multimap may contain multiple copies of each key value) and that associates values of another type with the keys. The unordered_multimap class supports forward iterators. Search, insertion, and removal have average constant-time complexity.
Internally, the elements are not sorted in any particular order, but organized into buckets. Which bucket an element is placed into depends entirely on the hash of its key. This allows fast access to individual elements, since once the hash is computed, it refers to the exact bucket the element is placed into.
The iteration order of this container is not required to be stable (so, for example, `std::equal` cannot be used to compare two `std::unordered_multimap`s), except that every group of elements whose keys compare ''equivalent'' (compare equal with `key_eq()` as the comparator) forms a contiguous subrange in the iteration order, also accessible with `std::unordered_multimap::equal_range|equal_range()`.
`std::unordered_multimap` meets the requirements of *Container*, *AllocatorAwareContainer*, *UnorderedAssociativeContainer*.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|unordered_multimap | (see dedicated page) |
| cpp/container/dsc mapped_type|unordered_multimap | (see dedicated page) |
| cpp/container/dsc value_type|unordered_multimap | (see dedicated page) |
| cpp/container/dsc size_type|unordered_multimap | (see dedicated page) |
| cpp/container/dsc difference_type|unordered_multimap | (see dedicated page) |
| cpp/container/dsc hasher|unordered_multimap | (see dedicated page) |
| cpp/container/dsc key_equal|unordered_multimap | (see dedicated page) |
| cpp/container/dsc allocator_type|unordered_multimap | (see dedicated page) |
| cpp/container/dsc reference|unordered_multimap | (see dedicated page) |
| cpp/container/dsc const_reference|unordered_multimap | (see dedicated page) |
| cpp/container/dsc pointer|unordered_multimap | (see dedicated page) |
| cpp/container/dsc const_pointer|unordered_multimap | (see dedicated page) |
| cpp/container/dsc iterator|unordered_multimap | (see dedicated page) |
| cpp/container/dsc const_iterator|unordered_multimap | (see dedicated page) |
| cpp/container/dsc local_iterator|unordered_multimap | (see dedicated page) |
| cpp/container/dsc const_local_iterator|unordered_multimap | (see dedicated page) |
| cpp/container/dsc node_type|unordered_multimap | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|unordered_multimap | (see dedicated page) |
| cpp/container/dsc destructor|unordered_multimap | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|unordered_multimap | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|unordered_multimap | (see dedicated page) |
| cpp/container/dsc end|unordered_multimap | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|unordered_multimap | (see dedicated page) |
| cpp/container/dsc size|unordered_multimap | (see dedicated page) |
| cpp/container/dsc max_size|unordered_multimap | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|unordered_multimap | (see dedicated page) |
| cpp/container/dsc insert|unordered_multimap | (see dedicated page) |
| cpp/container/dsc insert_range|unordered_multimap | (see dedicated page) |
| cpp/container/dsc emplace|unordered_multimap | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_multimap | (see dedicated page) |
| cpp/container/dsc erase|unordered_multimap | (see dedicated page) |
| cpp/container/dsc swap|unordered_multimap | (see dedicated page) |
| cpp/container/dsc extract|unordered_multimap | (see dedicated page) |
| cpp/container/dsc merge|unordered_multimap | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|unordered_multimap | (see dedicated page) |
| cpp/container/dsc find|unordered_multimap | (see dedicated page) |
| cpp/container/dsc contains|unordered_multimap | (see dedicated page) |
| cpp/container/dsc equal_range|unordered_multimap | (see dedicated page) |

#### Bucket interface

| cpp/container/dsc begin(int)|unordered_multimap | (see dedicated page) |
| cpp/container/dsc end(int)|unordered_multimap | (see dedicated page) |
| cpp/container/dsc bucket_count|unordered_multimap | (see dedicated page) |
| cpp/container/dsc max_bucket_count|unordered_multimap | (see dedicated page) |
| cpp/container/dsc bucket_size|unordered_multimap | (see dedicated page) |
| cpp/container/dsc bucket|unordered_multimap | (see dedicated page) |

#### Hash policy

| cpp/container/dsc load_factor|unordered_multimap | (see dedicated page) |
| cpp/container/dsc max_load_factor|unordered_multimap | (see dedicated page) |
| cpp/container/dsc rehash|unordered_multimap | (see dedicated page) |
| cpp/container/dsc reserve|unordered_multimap | (see dedicated page) |

#### Observers

| cpp/container/dsc hash_function|unordered_multimap | (see dedicated page) |
| cpp/container/dsc key_eq|unordered_multimap | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp_unord|unordered_multimap | (see dedicated page) |
| cpp/container/dsc swap2|unordered_multimap | (see dedicated page) |
| cpp/container/dsc erase_if|unordered_multimap | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_unordered_map` | 202502L | C++26 | Constexpr `std::unordered_multimap` |


## Example


## See also


| cpp/container/dsc unordered_map | (see dedicated page) |
| cpp/container/dsc multimap | (see dedicated page) |
| cpp/container/dsc flat_multimap | (see dedicated page) |

