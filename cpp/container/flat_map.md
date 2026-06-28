---
title: std::flat_map
type: Containers
source: https://en.cppreference.com/w/cpp/container/flat_map
---

ddcl|header=flat_map|since=c++23|1=
template<
class Key,
class T,
class Compare = std::less<Key>,
class KeyContainer = std::vector<Key>,
class MappedContainer = std::vector<T>
> class flat_map;
The flat map is a container adaptor that gives the functionality of an associative container that contains key-value pairs with unique keys. Keys are sorted by using the comparison function `Compare`.
The class template `flat_map` acts as a wrapper to the two underlying containers, passed as objects of type `KeyContainer` and `MappedContainer` respectively. The first container is sorted, and for each key its corresponding value is in the second container at the same index (offset). The number of elements in both containers is the same.
Everywhere the standard library uses the *Compare* requirements, uniqueness is determined by using the equivalence relation. Informally, two objects `a` and `b` are considered equivalent if neither compares less than the other: `!comp(a, b) && !comp(b, a)`.
`std::flat_map` meets the requirements of *Container*, *ReversibleContainer*, , and all requirements of *AssociativeContainer* (including logarithmic search complexity), except that:
* requirements related to nodes are not applicable,
* iterator invalidation requirements differ,
* the complexity of insertion and erasure operations is linear.
A flat map supports most *AssociativeContainer*'s operations that use unique keys.

## Iterator invalidation


## Template parameters


### Parameters

- `Key` - The type of the keys. The program is ill-formed if `Key` is not the same type as `KeyContainer::value_type`.
- `T` - The type of mapped values. The program is ill-formed if `T` is not the same type as `MappedContainer::value_type`.
- `Compare` - A *Compare* type providing a strict weak ordering.
- `KeyContainer<br>MappedContainer` - The types of the underlying *SequenceContainer* to store keys and mapped values correspondingly. The iterators of such containers should satisfy *RandomAccessIterator* or model . Invocations of their member functions `size` and `max_size` should not exit via an exception.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_container_type|flat_map | (see dedicated page) |
| cpp/container/dsc mapped_container_type|flat_map | (see dedicated page) |
| cpp/container/dsc key_type|flat_map | (see dedicated page) |
| cpp/container/dsc mapped_type|flat_map | (see dedicated page) |
| cpp/container/dsc value_type|flat_map | (see dedicated page) |
| cpp/container/dsc key_compare|flat_map | (see dedicated page) |
| cpp/container/dsc reference|flat_map | (see dedicated page) |
| cpp/container/dsc const_reference|flat_map | (see dedicated page) |
| cpp/container/dsc size_type|flat_map | (see dedicated page) |
| cpp/container/dsc difference_type|flat_map | (see dedicated page) |
| cpp/container/dsc iterator|flat_map | (see dedicated page) |
| cpp/container/dsc const_iterator|flat_map | (see dedicated page) |
| cpp/container/dsc reverse_iterator|flat_map | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|flat_map | (see dedicated page) |
| cpp/container/dsc containers|flat_map | (see dedicated page) |


## Member classes


| cpp/container/dsc value_compare|flat_map | (see dedicated page) |
| cpp/container/dsc key_equiv|flat_map | (see dedicated page) |


## Member objects


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/container/dsc constructor|flat_map | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |

#### Element access

| cpp/container/dsc at|flat_map | (see dedicated page) |
| cpp/container/dsc operator_at|flat_map | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|flat_map | (see dedicated page) |
| cpp/container/dsc end|flat_map | (see dedicated page) |
| cpp/container/dsc rbegin|flat_map | (see dedicated page) |
| cpp/container/dsc rend|flat_map | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|flat_map | (see dedicated page) |
| cpp/container/dsc size|flat_map | (see dedicated page) |
| cpp/container/dsc max_size|flat_map | (see dedicated page) |

#### Modifiers

| cpp/container/dsc emplace|flat_map | (see dedicated page) |
| cpp/container/dsc emplace_hint|flat_map | (see dedicated page) |
| cpp/container/dsc try_emplace|flat_map | (see dedicated page) |
| cpp/container/dsc insert|flat_map | (see dedicated page) |
| cpp/container/dsc insert_range|flat_map | (see dedicated page) |
| cpp/container/dsc insert_or_assign|flat_map | (see dedicated page) |
| cpp/container/dsc extract|flat_map | (see dedicated page) |
| cpp/container/dsc replace|flat_map | (see dedicated page) |
| cpp/container/dsc erase|flat_map | (see dedicated page) |
| cpp/container/dsc swap|flat_map | (see dedicated page) |
| cpp/container/dsc clear|flat_map | (see dedicated page) |

#### Lookup

| cpp/container/dsc find|flat_map | (see dedicated page) |
| cpp/container/dsc count|flat_map | (see dedicated page) |
| cpp/container/dsc contains|flat_map | (see dedicated page) |
| cpp/container/dsc lower_bound|flat_map | (see dedicated page) |
| cpp/container/dsc upper_bound|flat_map | (see dedicated page) |
| cpp/container/dsc equal_range|flat_map | (see dedicated page) |

#### Observers

| cpp/container/dsc key_comp|flat_map | (see dedicated page) |
| cpp/container/dsc value_comp|flat_map | (see dedicated page) |
| cpp/container/dsc keys|flat_map | (see dedicated page) |
| cpp/container/dsc values|flat_map | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|flat_map | (see dedicated page) |
| cpp/container/dsc swap2|flat_map | (see dedicated page) |
| cpp/container/dsc erase_if|flat_map | (see dedicated page) |


## Helper classes


| cpp/container/dsc uses_allocator|flat_map | (see dedicated page) |


## Tags


| cpp/container/dsc sorted_unique | (see dedicated page) |


## 


## Notes

<!-- TODO: maybe this lyrics is unnecessary:
Some advantages of flat map over other standard associative containers are:
* Potentially faster lookup (even though search operations have logarithmic complexity).
* Much faster iteration: s instead of s.
* Less memory consumption for small objects (and for big objects if `KeyContainer::shrink_to_fit()` is available).
* Better cache performance (depending on `KeyContainer`, keys are stored in a contiguous block(s) of memory).
Some disadvantages of flat map are:
* Non-stable iterators (iterators are invalidated when inserting and erasing elements).
* Non-copyable and non-movable type values can not be stored.
* Weaker exception safety (copy/move constructors can throw when shifting values in erasures and insertions).
* Slower (i.e. linear) insertion and erasure, especially for non-movable types.
-->

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_flat_map` | 202207L | C++23 | `std::flat_map` and `std::flat_multimap` |
| `__cpp_lib_constexpr_flat_map` | 202502L | C++26 | Constexpr `std::flat_map` |


## Example

<!--TODO: N4950::24.6.9 says:
TODO: add this to the "Exceptions" sections of appropriate member functions:
6. If any member function in 24.6.9.2 exits via an exception, the invariants are restored.
[Note 2 : This can result in the flat_map’s being emptied. — end note].
-->
<!--TODO: N4950::24.6.9.1 says:
TODO: add to constructors:
9. The effect of calling a constructor that takes both key_container_type and mapped_container_type arguments with containers of different sizes is undefined.
10. The effect of calling a constructor or member function that takes a sorted_unique_t argument with a container, containers, or range that is not sorted with respect to key_comp(), or that contains equal elements, is undefined.
-->
