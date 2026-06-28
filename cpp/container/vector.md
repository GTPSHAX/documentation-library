---
title: std::vector
type: Containers
source: https://en.cppreference.com/w/cpp/container/vector
---


```cpp
**Header:** `<`vector`>`
dcl|num=1|1=
template<
class T,
class Allocator = std::allocator<T>
> class vector;
dcl|since=c++17|num=2|1=
namespace pmr {
template< class T >
using vector = std::vector<T, std::pmr::polymorphic_allocator<T>>;
}
```

1. `std::vector` is a sequence container that encapsulates dynamic size arrays.
2. `std::pmr::vector` is an alias template that uses a polymorphic allocator.
The elements are stored contiguously, which means that elements can be accessed not only through iterators, but also using offsets to regular pointers to elements. This means that a pointer to an element of a vector may be passed to any function that expects a pointer to an element of an array.
The storage of the vector is handled automatically, being expanded as needed. Vectors usually occupy more space than static arrays, because more memory is allocated to handle future growth. This way a vector does not need to reallocate each time an element is inserted, but only when the additional memory is exhausted. The total amount of allocated memory can be queried using `capacity()` function. Extra memory can be returned to the system via a call to `shrink_to_fit()`.
Reallocations are usually costly operations in terms of performance. The `reserve()` function can be used to eliminate reallocations if the number of elements is known beforehand.
The complexity (efficiency) of common operations on vectors is as follows:
* Random access - constant $𝓞(1)$.
* Insertion or removal of elements at the end - amortized constant $𝓞(1)$.
* Insertion or removal of elements - linear in the distance to the end of the vector $𝓞(n)$.
`std::vector` (for `T` other than `bool`) meets the requirements of *Container*<sup>(since C++11)</sup> , *AllocatorAwareContainer*, *SequenceContainer*<sup>(since C++17)</sup> , *ContiguousContainer* and *ReversibleContainer*.
> **TODO:** Add bits from

## Template parameters


### Parameters


## Specializations

The standard library provides a specialization of `std::vector` for the type `bool`, which may be optimized for space efficiency.


| cpp/container/dsc vector bool | (see dedicated page) |


## Iterator invalidation


| Operations |
| Invalidated |
| - |
| All read only operations |
| Never. |
| - |
| lc | swap, lc | std::swap |
| lc | end() |
| - |
| lc | clear, lc | 1=operator=, lc | assign |
| Always. |
| - |
| lc | reserve, lc | shrink_to_fit |
| If the vector changed capacity, all of them. If not, none. |
| - |
| lc | erase |
| Erased elements and all elements after them (including lc | end()). |
| - |
| lc | push_back, lc | emplace_back |
| If the vector changed capacity, all of them. If not, only lc | end(). |
| - |
| lc | insert, lc | emplace |
| If the vector changed capacity, all of them.<br>If not, only those at or after the insertion point (including lc | end()). |
| - |
| lc | resize |
| If the vector changed capacity, all of them. If not, only lc | end() and any elements erased. |
| - |
| lc | pop_back |
| The element erased and lc | end(). |


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc value_type|vector | (see dedicated page) |
| cpp/container/dsc allocator_type|vector | (see dedicated page) |
| cpp/container/dsc size_type|vector | (see dedicated page) |
| cpp/container/dsc difference_type|vector | (see dedicated page) |
| cpp/container/dsc reference|vector | (see dedicated page) |
| cpp/container/dsc const_reference|vector | (see dedicated page) |
| cpp/container/dsc pointer|vector | (see dedicated page) |
| cpp/container/dsc const_pointer|vector | (see dedicated page) |
| cpp/container/dsc iterator|vector | (see dedicated page) |
| cpp/container/dsc const_iterator|vector | (see dedicated page) |
| cpp/container/dsc reverse_iterator|vector | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|vector | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|vector | (see dedicated page) |
| cpp/container/dsc destructor|vector | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc assign|vector | (see dedicated page) |
| cpp/container/dsc assign_range|vector | (see dedicated page) |
| cpp/container/dsc get_allocator|vector | (see dedicated page) |

#### Element access

| cpp/container/dsc at|vector | (see dedicated page) |
| cpp/container/dsc operator_at|vector | (see dedicated page) |
| cpp/container/dsc front|vector | (see dedicated page) |
| cpp/container/dsc back|vector | (see dedicated page) |
| cpp/container/dsc data|vector | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|vector | (see dedicated page) |
| cpp/container/dsc end|vector | (see dedicated page) |
| cpp/container/dsc rbegin|vector | (see dedicated page) |
| cpp/container/dsc rend|vector | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|vector | (see dedicated page) |
| cpp/container/dsc size|vector | (see dedicated page) |
| cpp/container/dsc max_size|vector | (see dedicated page) |
| cpp/container/dsc reserve|vector | (see dedicated page) |
| cpp/container/dsc capacity|vector | (see dedicated page) |
| cpp/container/dsc shrink_to_fit|vector | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|vector | (see dedicated page) |
| cpp/container/dsc insert|vector | (see dedicated page) |
| cpp/container/dsc insert_range|vector | (see dedicated page) |
| cpp/container/dsc emplace|vector | (see dedicated page) |
| cpp/container/dsc erase|vector | (see dedicated page) |
| cpp/container/dsc push_back|vector | (see dedicated page) |
| cpp/container/dsc emplace_back|vector | (see dedicated page) |
| cpp/container/dsc append_range|vector | (see dedicated page) |
| cpp/container/dsc pop_back|vector | (see dedicated page) |
| cpp/container/dsc resize|vector | (see dedicated page) |
| cpp/container/dsc swap|vector | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|vector | (see dedicated page) |
| cpp/container/dsc swap2|vector | (see dedicated page) |
| cpp/container/dsc erase seq|vector | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <vector>

int main()
{
    // Create a vector containing integers
    std::vector<int> v = {8, 4, 5, 9};

    // Add two more integers to vector
    v.push_back(6);
    v.push_back(9);

    // Overwrite element at position 2
    v[2] = -1;

    // Print out the vector
    for (int n : v)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
8 4 -1 9 6 9
```


## Defect reports


## See also


| cpp/container/dsc inplace_vector | (see dedicated page) |
| cpp/container/dsc array | (see dedicated page) |
| cpp/container/dsc deque | (see dedicated page) |

