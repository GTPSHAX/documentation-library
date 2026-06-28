---
title: std::flat_multiset
type: Containers
source: https://en.cppreference.com/w/cpp/container/flat_multiset
---

ddcl|header=flat_set|since=c++23|1=
template<
class Key,
class Compare = std::less<Key>,
class KeyContainer = std::vector<Key>
> class flat_multiset;
The flat multiset is a container adaptor that gives the functionality of an associative container that stores a sorted set of objects of type `Key`. Unlike `std::flat_set`, multiple keys with equivalent values are allowed. Sorting is done using the key comparison function `Compare`.
The class template `flat_multiset` acts as a wrapper to the underlying sorted container passed as object of type `KeyContainer`.
Everywhere the standard library uses the *Compare* requirements, uniqueness is determined by using the equivalence relation. Informally, two objects `a` and `b` are considered equivalent if neither compares less than the other: `!comp(a, b) && !comp(b, a)`.
`std::flat_multiset` meets the requirements of *Container*, *ReversibleContainer*, , and all requirements of *AssociativeContainer* (including logarithmic search complexity), except that:
* requirements related to nodes are not applicable,
* iterator invalidation requirements differ,
* the complexity of insertion and erasure operations is linear.
A flat multiset supports most *AssociativeContainer*'s operations that use equal keys.

## Iterator invalidation


## Template parameters


### Parameters

- `Key` - The type of the stored elements. The program is ill-formed if `Key` is not the same type as `KeyContainer::value_type`.
- `Compare` - A *Compare* type providing a strict weak ordering.
- `KeyContainer` - The type of the underlying *SequenceContainer* to store the elements. The iterators of such container should satisfy *RandomAccessIterator* or model .

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc container_type|flat_multiset | (see dedicated page) |
| cpp/container/dsc key_type|flat_multiset | (see dedicated page) |
| cpp/container/dsc value_type|flat_multiset | (see dedicated page) |
| cpp/container/dsc key_compare|flat_multiset | (see dedicated page) |
| cpp/container/dsc value_compare2|flat_multiset | (see dedicated page) |
| cpp/container/dsc reference|flat_multiset | (see dedicated page) |
| cpp/container/dsc const_reference|flat_multiset | (see dedicated page) |
| cpp/container/dsc size_type|flat_multiset | (see dedicated page) |
| cpp/container/dsc difference_type|flat_multiset | (see dedicated page) |
| cpp/container/dsc iterator|flat_multiset | (see dedicated page) |
| cpp/container/dsc const_iterator|flat_multiset | (see dedicated page) |
| cpp/container/dsc reverse_iterator|flat_multiset | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|flat_multiset | (see dedicated page) |


## Member objects


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/container/dsc constructor|flat_multiset | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|flat_multiset | (see dedicated page) |
| cpp/container/dsc end|flat_multiset | (see dedicated page) |
| cpp/container/dsc rbegin|flat_multiset | (see dedicated page) |
| cpp/container/dsc rend|flat_multiset | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|flat_multiset | (see dedicated page) |
| cpp/container/dsc size|flat_multiset | (see dedicated page) |
| cpp/container/dsc max_size|flat_multiset | (see dedicated page) |

#### Modifiers

| cpp/container/dsc emplace|flat_multiset | (see dedicated page) |
| cpp/container/dsc emplace_hint|flat_multiset | (see dedicated page) |
| cpp/container/dsc insert|flat_multiset | (see dedicated page) |
| cpp/container/dsc insert_range|flat_multiset | (see dedicated page) |
| cpp/container/dsc extract|flat_multiset | (see dedicated page) |
| cpp/container/dsc replace|flat_multiset | (see dedicated page) |
| cpp/container/dsc erase|flat_multiset | (see dedicated page) |
| cpp/container/dsc swap|flat_multiset | (see dedicated page) |
| cpp/container/dsc clear|flat_multiset | (see dedicated page) |

#### Lookup

| cpp/container/dsc find|flat_multiset | (see dedicated page) |
| cpp/container/dsc count|flat_multiset | (see dedicated page) |
| cpp/container/dsc contains|flat_multiset | (see dedicated page) |
| cpp/container/dsc lower_bound|flat_multiset | (see dedicated page) |
| cpp/container/dsc upper_bound|flat_multiset | (see dedicated page) |
| cpp/container/dsc equal_range|flat_multiset | (see dedicated page) |

#### Observers

| cpp/container/dsc key_comp|flat_multiset | (see dedicated page) |
| cpp/container/dsc value_comp|flat_multiset | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|flat_multiset | (see dedicated page) |
| cpp/container/dsc swap2|flat_multiset | (see dedicated page) |
| cpp/container/dsc erase_if|flat_multiset | (see dedicated page) |


## Helper classes


| cpp/container/dsc uses_allocator|flat_multiset | (see dedicated page) |


## Tags


| cpp/container/dsc sorted_equivalent | (see dedicated page) |


## 


## Notes

<!-- TODO: maybe this lyrics is unnecessary:
Some advantages of flat multiset over other standard associative containers are:
* Potentially faster lookup (even though search operations have logarithmic complexity).
* Much faster iteration: s instead of s.
* Less memory consumption for small objects (and for big objects if `KeyContainer::shrink_to_fit()` is available).
* Better cache performance (depending on `KeyContainer`, keys are stored in a contiguous block(s) of memory).
Some disadvantages of flat multiset are:
* Non-stable iterators (iterators are invalidated when inserting and erasing elements).
* Non-copyable and non-movable type values can not be stored.
* Weaker exception safety (copy/move constructors can throw when shifting values in erasures and insertions).
* Slower (i.e. linear) insertion and erasure, especially for non-movable types.
-->

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_flat_set` | 202207L | C++23 | `std::flat_set` and `std::flat_multiset` |
| `__cpp_lib_constexpr_flat_set` | 202502L | C++26 | Constexpr `std::flat_multiset` |


## Example

<!--TODO: N4950::24.6.12 says:
TODO: add this to the "Exceptions" sections of appropriate member functions:
6. If any member function in 24.6.12.2 exits via an exception, the invariant is restored.
[Note 2 : This can result in the flat_multiset’s being emptied. — end note].
-->
<!--TODO: N4950::24.6.12.9 says:
TODO: add to constructors:
9. The effect of calling a constructor or member function that takes a sorted_equivalent_t argument with a range that is not sorted with respect to key_comp(), or that contains equal elements, is undefined.
-->
