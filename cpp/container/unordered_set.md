---
title: std::unordered_set
type: Containers
source: https://en.cppreference.com/w/cpp/container/unordered_set
---


```cpp
**Header:** `<`unordered_set`>`
dcl|num=1|since=c++11|1=
template<
class Key,
class Hash = std::hash<Key>,
class KeyEqual = std::equal_to<Key>,
class Allocator = std::allocator<Key>
> class unordered_set;
dcl|num=2|since=c++17|1=
namespace pmr {
template<
class Key,
class Hash = std::hash<Key>,
class Pred = std::equal_to<Key>
> using unordered_set = std::unordered_set<Key, Hash, Pred,
std::pmr::polymorphic_allocator<Key>>;
}
```

`std::unordered_set` is an associative container that contains a set of unique objects of type `Key`. Search, insertion, and removal have average constant-time complexity.
Internally, the elements are not sorted in any particular order, but organized into buckets. Which bucket an element is placed into depends entirely on the hash of its value. This allows fast access to individual elements, since once a hash is computed, it refers to the exact bucket the element is placed into.
Container elements may not be modified (even by non const iterators) since modification could change an element's hash and corrupt the container.
`std::unordered_set` meets the requirements of *Container*, *AllocatorAwareContainer*, *UnorderedAssociativeContainer*.

## Iterator invalidation


| Operations |
| Invalidated |
| - |
| All read only operations, lc | swap, lc | std::swap |
| Never |
| - |
| lc | clear, lc | rehash, lc | reserve, lc | 1=operator= |
| Always |
| - |
| lc | insert, lc | emplace, lc | emplace_hint |
| Only if causes rehash |
| - |
| lc | erase |
| Only to the element erased |


### Notes

* The swap functions do not invalidate any of the iterators inside the container, but they do invalidate the iterator marking the end of the swap region.
* References and pointers to data stored in the container are only invalidated by erasing that element, even when the corresponding iterator is invalidated.
* After container move assignment, unless elementwise move assignment is forced by incompatible allocators, references, pointers, and iterators (other than the past-the-end iterator) to moved-from container remain valid, but refer to elements that are now in `*this`.

## Template parameters


## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| cpp/container/dsc key_type|unordered_set | (see dedicated page) |
| cpp/container/dsc value_type|unordered_set | (see dedicated page) |
| cpp/container/dsc size_type|unordered_set | (see dedicated page) |
| cpp/container/dsc difference_type|unordered_set | (see dedicated page) |
| cpp/container/dsc hasher|unordered_set | (see dedicated page) |
| cpp/container/dsc key_equal|unordered_set | (see dedicated page) |
| cpp/container/dsc allocator_type|unordered_set | (see dedicated page) |
| cpp/container/dsc reference|unordered_set | (see dedicated page) |
| cpp/container/dsc const_reference|unordered_set | (see dedicated page) |
| cpp/container/dsc pointer|unordered_set | (see dedicated page) |
| cpp/container/dsc const_pointer|unordered_set | (see dedicated page) |
| cpp/container/dsc iterator|unordered_set | (see dedicated page) |
| cpp/container/dsc const_iterator|unordered_set | (see dedicated page) |
| cpp/container/dsc local_iterator|unordered_set | (see dedicated page) |
| cpp/container/dsc const_local_iterator|unordered_set | (see dedicated page) |
| cpp/container/dsc node_type|unordered_set | (see dedicated page) |
| cpp/container/dsc insert_return_type|unordered_set | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|unordered_set | (see dedicated page) |
| cpp/container/dsc destructor|unordered_set | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc get_allocator|unordered_set | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|unordered_set | (see dedicated page) |
| cpp/container/dsc end|unordered_set | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|unordered_set | (see dedicated page) |
| cpp/container/dsc size|unordered_set | (see dedicated page) |
| cpp/container/dsc max_size|unordered_set | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|unordered_set | (see dedicated page) |
| cpp/container/dsc insert|unordered_set | (see dedicated page) |
| cpp/container/dsc insert_range|unordered_set | (see dedicated page) |
| cpp/container/dsc emplace|unordered_set | (see dedicated page) |
| cpp/container/dsc emplace_hint|unordered_set | (see dedicated page) |
| cpp/container/dsc erase|unordered_set | (see dedicated page) |
| cpp/container/dsc swap|unordered_set | (see dedicated page) |
| cpp/container/dsc extract|unordered_set | (see dedicated page) |
| cpp/container/dsc merge|unordered_set | (see dedicated page) |

#### Lookup

| cpp/container/dsc count|unordered_set | (see dedicated page) |
| cpp/container/dsc find|unordered_set | (see dedicated page) |
| cpp/container/dsc contains|unordered_set | (see dedicated page) |
| cpp/container/dsc equal_range|unordered_set | (see dedicated page) |

#### Bucket interface

| cpp/container/dsc begin(int)|unordered_set | (see dedicated page) |
| cpp/container/dsc end(int)|unordered_set | (see dedicated page) |
| cpp/container/dsc bucket_count|unordered_set | (see dedicated page) |
| cpp/container/dsc max_bucket_count|unordered_set | (see dedicated page) |
| cpp/container/dsc bucket_size|unordered_set | (see dedicated page) |
| cpp/container/dsc bucket|unordered_set | (see dedicated page) |

#### Hash policy

| cpp/container/dsc load_factor|unordered_set | (see dedicated page) |
| cpp/container/dsc max_load_factor|unordered_set | (see dedicated page) |
| cpp/container/dsc rehash|unordered_set | (see dedicated page) |
| cpp/container/dsc reserve|unordered_set | (see dedicated page) |

#### Observers

| cpp/container/dsc hash_function|unordered_set | (see dedicated page) |
| cpp/container/dsc key_eq|unordered_set | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp_unord|unordered_set | (see dedicated page) |
| cpp/container/dsc swap2|unordered_set | (see dedicated page) |
| cpp/container/dsc erase_if|unordered_set | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_unordered_set` | 202502L | C++26 | Constexpr `std::unordered_set` |


## Example


### Example

```cpp
#include <iostream>
#include <unordered_set>

void print(const auto& set)
{
    for (const auto& elem : set)
        std::cout << elem << ' ';
    std::cout << '\n';
}

int main()
{
    std::unordered_set<int> mySet{2, 7, 1, 8, 2, 8}; // creates a set of ints
    print(mySet);

    mySet.insert(5); // puts an element 5 in the set
    print(mySet);

    if (auto iter = mySet.find(5); iter != mySet.end())
        mySet.erase(iter); // removes an element pointed to by iter
    print(mySet);

    mySet.erase(7); // removes an element 7
    print(mySet);
}
```


**Output:**
```
8 1 7 2
5 8 1 7 2
8 1 7 2
8 1 2
```


## Defect reports


## See also


| cpp/container/dsc unordered_multiset | (see dedicated page) |
| cpp/container/dsc set | (see dedicated page) |
| cpp/container/dsc flat_set | (see dedicated page) |

