---
title: std::multiset
type: Containers
source: https://en.cppreference.com/w/cpp/container/multiset
---


```cpp
**Header:** `<`set`>`
dcl|num=1|1=
template<
class Key,
class Compare = std::less<Key>,
class Allocator = std::allocator<Key>
> class multiset;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class Compare = std::less<Key>
> using multiset = std::multiset<Key, Compare, std::pmr::polymorphic_allocator<Key>>;
}
```

`std::multiset` is an associative container that contains a sorted set of objects of type Key. Unlike set, multiple keys with equivalent values are allowed. Sorting is done using the key comparison function Compare. Search, insertion, and removal operations have logarithmic complexity.
Everywhere the standard library uses the *Compare* requirements, equivalence is determined by using the equivalence relation as described on *Compare*. In imprecise terms, two objects `a` and `b` are considered equivalent if neither compares less than the other: `!comp(a, b) && !comp(b, a)`.
rrev|since=c++11|
The order of the elements that compare equivalent is the order of insertion and does not change.
`std::multiset` meets the requirements of *Container*, *AllocatorAwareContainer*, *AssociativeContainer* and *ReversibleContainer*.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|multiset | (see dedicated page) |
| cpp/container/dsc value_type|multiset | (see dedicated page) |
| cpp/container/dsc size_type|multiset | (see dedicated page) |
| cpp/container/dsc difference_type|multiset | (see dedicated page) |
| cpp/container/dsc key_compare|multiset | (see dedicated page) |
| cpp/container/dsc value_compare2|multiset | (see dedicated page) |
| cpp/container/dsc allocator_type|multiset | (see dedicated page) |
| cpp/container/dsc reference|multiset | (see dedicated page) |
| cpp/container/dsc const_reference|multiset | (see dedicated page) |
| cpp/container/dsc pointer|multiset | (see dedicated page) |
| cpp/container/dsc const_pointer|multiset | (see dedicated page) |
| cpp/container/dsc iterator|multiset | (see dedicated page) |
| cpp/container/dsc const_iterator|multiset | (see dedicated page) |
| cpp/container/dsc reverse_iterator|multiset | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|multiset | (see dedicated page) |
| cpp/container/dsc node_type|multiset | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|multiset | (see dedicated page) |
| cpp/container/dsc destructor|multiset | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|multiset | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|multiset | (see dedicated page) |
| cpp/container/dsc end|multiset | (see dedicated page) |
| cpp/container/dsc rbegin|multiset | (see dedicated page) |
| cpp/container/dsc rend|multiset | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|multiset | (see dedicated page) |
| cpp/container/dsc size|multiset | (see dedicated page) |
| cpp/container/dsc max_size|multiset | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|multiset | (see dedicated page) |
| cpp/container/dsc insert|multiset | (see dedicated page) |
| cpp/container/dsc insert_range|multiset | (see dedicated page) |
| cpp/container/dsc emplace|multiset | (see dedicated page) |
| cpp/container/dsc emplace_hint|multiset | (see dedicated page) |
| cpp/container/dsc erase|multiset | (see dedicated page) |
| cpp/container/dsc swap|multiset | (see dedicated page) |
| cpp/container/dsc extract|multiset | (see dedicated page) |
| cpp/container/dsc merge|multiset | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|multiset | (see dedicated page) |
| cpp/container/dsc find|multiset | (see dedicated page) |
| cpp/container/dsc contains|multiset | (see dedicated page) |
| cpp/container/dsc equal_range|multiset | (see dedicated page) |
| cpp/container/dsc lower_bound|multiset | (see dedicated page) |
| cpp/container/dsc upper_bound|multiset | (see dedicated page) |

#### Observers

| cpp/container/dsc key_comp|multiset | (see dedicated page) |
| cpp/container/dsc value_comp|multiset | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|multiset | (see dedicated page) |
| cpp/container/dsc swap2|multiset | (see dedicated page) |
| cpp/container/dsc erase_if|multiset | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


## Example


## See also


| cpp/container/dsc set | (see dedicated page) |
| cpp/container/dsc unordered_multiset | (see dedicated page) |
| cpp/container/dsc flat_multiset | (see dedicated page) |

