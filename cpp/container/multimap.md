---
title: std::multimap
type: Containers
source: https://en.cppreference.com/w/cpp/container/multimap
---


```cpp
**Header:** `<`map`>`
dcl|num=1|1=
template<
class Key,
class T,
class Compare = std::less<Key>,
class Allocator = std::allocator<std::pair<const Key, T>>
> class multimap;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class T,
class Compare = std::less<Key>
> using multimap = std::multimap<Key, T, Compare,
std::pmr::polymorphic_allocator<std::pair<const Key, T>>>;
}
```

`std::multimap` is an associative container that contains a sorted list of key-value pairs, while permitting multiple entries with the same key. Sorting is done according to the comparison function `Compare`, applied to the keys. Search, insertion, and removal operations have logarithmic complexity.
Iterators of `std::multimap` iterate in non-descending order of keys, where non-descending is defined by the comparison that was used for construction. That is, given
* `m`, a `std::multimap`
* `it_l` and `it_r`, dereferenceable iterators to `m`, with `it_l < it_r`.
`1=m.value_comp()(*it_r, *it_l) == false` (least to greatest if using the default comparison).
rrev|since=c++11|
The order of the key-value pairs whose keys compare equivalent is the order of insertion and does not change.
Everywhere the standard library uses the *Compare* requirements, equivalence is determined by using the equivalence relation as described on *Compare*. In imprecise terms, two objects `a` and `b` are considered equivalent if neither compares less than the other: `!comp(a, b) && !comp(b, a)`.
`std::multimap` meets the requirements of *Container*, *AllocatorAwareContainer*, *AssociativeContainer* and *ReversibleContainer*.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|multimap | (see dedicated page) |
| cpp/container/dsc mapped_type|multimap | (see dedicated page) |
| cpp/container/dsc value_type|multimap | (see dedicated page) |
| cpp/container/dsc size_type|multimap | (see dedicated page) |
| cpp/container/dsc difference_type|multimap | (see dedicated page) |
| cpp/container/dsc key_compare|multimap | (see dedicated page) |
| cpp/container/dsc allocator_type|multimap | (see dedicated page) |
| cpp/container/dsc reference|multimap | (see dedicated page) |
| cpp/container/dsc const_reference|multimap | (see dedicated page) |
| cpp/container/dsc pointer|multimap | (see dedicated page) |
| cpp/container/dsc const_pointer|multimap | (see dedicated page) |
| cpp/container/dsc iterator|multimap | (see dedicated page) |
| cpp/container/dsc const_iterator|multimap | (see dedicated page) |
| cpp/container/dsc reverse_iterator|multimap | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|multimap | (see dedicated page) |
| cpp/container/dsc node_type|multimap | (see dedicated page) |


## Member classes


| cpp/container/dsc value_compare|multimap | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|multimap | (see dedicated page) |
| cpp/container/dsc destructor|multimap | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|multimap | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|multimap | (see dedicated page) |
| cpp/container/dsc end|multimap | (see dedicated page) |
| cpp/container/dsc rbegin|multimap | (see dedicated page) |
| cpp/container/dsc rend|multimap | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|multimap | (see dedicated page) |
| cpp/container/dsc size|multimap | (see dedicated page) |
| cpp/container/dsc max_size|multimap | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|multimap | (see dedicated page) |
| cpp/container/dsc insert|multimap | (see dedicated page) |
| cpp/container/dsc insert_range|multimap | (see dedicated page) |
| cpp/container/dsc emplace|multimap | (see dedicated page) |
| cpp/container/dsc emplace_hint|multimap | (see dedicated page) |
| cpp/container/dsc erase|multimap | (see dedicated page) |
| cpp/container/dsc swap|multimap | (see dedicated page) |
| cpp/container/dsc extract|multimap | (see dedicated page) |
| cpp/container/dsc merge|multimap | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|multimap | (see dedicated page) |
| cpp/container/dsc find|multimap | (see dedicated page) |
| cpp/container/dsc contains|multimap | (see dedicated page) |
| cpp/container/dsc equal_range|multimap | (see dedicated page) |
| cpp/container/dsc lower_bound|multimap | (see dedicated page) |
| cpp/container/dsc upper_bound|multimap | (see dedicated page) |

#### Observers

| cpp/container/dsc key_comp|multimap | (see dedicated page) |
| cpp/container/dsc value_comp|multimap | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|multimap | (see dedicated page) |
| cpp/container/dsc swap2|multimap | (see dedicated page) |
| cpp/container/dsc erase_if|multimap | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_map` | 202502L | C++26 | Constexpr `std::multimap` |


## Example


## See also


| cpp/container/dsc map | (see dedicated page) |
| cpp/container/dsc unordered_multimap | (see dedicated page) |
| cpp/container/dsc flat_multimap | (see dedicated page) |

