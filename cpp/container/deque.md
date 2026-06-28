---
title: std::deque
type: Containers
source: https://en.cppreference.com/w/cpp/container/deque
---


```cpp
**Header:** `<`deque`>`
dcl|num=1|1=
template<
class T,
class Allocator = std::allocator<T>
> class deque;
dcl|num=2|since=c++17|1=
namespace pmr {
template< class T >
using deque = std::deque<T, std::pmr::polymorphic_allocator<T>>;
}
```

`std::deque` (double-ended queue) is an indexed sequence container that allows fast insertion and deletion at both its beginning and its end. In addition, insertion and deletion at either end of a deque never invalidates pointers or references to the rest of the elements.
As opposed to `std::vector`, the elements of a deque are not stored contiguously: typical implementations use a sequence of individually allocated fixed-size arrays, with additional bookkeeping, which means indexed access to deque must perform two pointer dereferences, compared to vector's indexed access which performs only one.
The storage of a deque is automatically expanded and contracted as needed. Expansion of a deque is cheaper than the expansion of a `std::vector` because it does not involve copying of the existing elements to a new memory location. On the other hand, deques typically have large minimal memory cost; a deque holding just one element has to allocate its full internal array (e.g. 8 times the object size on 64-bit libstdc++; 16 times the object size or 4096 bytes, whichever is larger, on 64-bit libc++).
The complexity (efficiency) of common operations on deques is as follows:
* Random access - constant $O(1)$.
* Insertion or removal of elements at the end or beginning - constant $O(1)$.
* Insertion or removal of elements - linear $O(n)$.
`std::deque` meets the requirements of *Container*, *AllocatorAwareContainer*, *SequenceContainer* and *ReversibleContainer*.

## Template parameters


### Parameters


## Iterator invalidation


| Operations |
| Invalidated |
| - |
| All read only operations. |
| Never. |
| - |
| lc | swap, lc | std::swap |
| The past-the-end iterator may be invalidated (implementation defined). |
| - |
| lc | shrink_to_fit, lc | clear, lc | insert,<br>lc | emplace, lc | push_front, lc | push_back,<br>lc | emplace_front, lc | emplace_back |
| Always. |
| - |
| lc | erase |
| If erasing at begin - only erased elements.<br> |
| rev1 |
| rev2 |
| - |
| lc | resize |
| If the new size is smaller than the old one - only erased elements and the<br> past-the-end iterator.<br> |
| - |
| lc | pop_front, lc | pop_back |
| To the element erased. |
| rev1=The past-the-end iterator may be invalidated (implementation defined). |
| rev2=The past-the-end iterator is also invalidated. |


### Invalidation notes

* When inserting at either end of the deque, references are not invalidated by `insert` and `emplace`.
* `push_front`, `push_back`, `emplace_front` and `emplace_back` do not invalidate any references to elements of the deque.
* When erasing at either end of the deque, references to non-erased elements are not invalidated by `erase`, `pop_front` and `pop_back`.
* A call to `resize` with a smaller size does not invalidate any references to non-erased elements.
* A call to `resize` with a bigger size does not invalidate any references to elements of the deque.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc value_type|deque | (see dedicated page) |
| cpp/container/dsc allocator_type|deque | (see dedicated page) |
| cpp/container/dsc size_type|deque | (see dedicated page) |
| cpp/container/dsc difference_type|deque | (see dedicated page) |
| cpp/container/dsc reference|deque | (see dedicated page) |
| cpp/container/dsc const_reference|deque | (see dedicated page) |
| cpp/container/dsc pointer|deque | (see dedicated page) |
| cpp/container/dsc const_pointer|deque | (see dedicated page) |
| cpp/container/dsc iterator|deque | (see dedicated page) |
| cpp/container/dsc const_iterator|deque | (see dedicated page) |
| cpp/container/dsc reverse_iterator|deque | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|deque | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|deque | (see dedicated page) |
| cpp/container/dsc destructor|deque | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc assign|deque | (see dedicated page) |
| cpp/container/dsc assign_range|deque | (see dedicated page) |
| cpp/container/dsc get_allocator|deque | (see dedicated page) |

#### Element access

| cpp/container/dsc at|deque | (see dedicated page) |
| cpp/container/dsc operator_at|deque | (see dedicated page) |
| cpp/container/dsc front|deque | (see dedicated page) |
| cpp/container/dsc back|deque | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|deque | (see dedicated page) |
| cpp/container/dsc end|deque | (see dedicated page) |
| cpp/container/dsc rbegin|deque | (see dedicated page) |
| cpp/container/dsc rend|deque | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|deque | (see dedicated page) |
| cpp/container/dsc size|deque | (see dedicated page) |
| cpp/container/dsc max_size|deque | (see dedicated page) |
| cpp/container/dsc shrink_to_fit|deque | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|deque | (see dedicated page) |
| cpp/container/dsc insert|deque | (see dedicated page) |
| cpp/container/dsc insert_range|deque | (see dedicated page) |
| cpp/container/dsc emplace|deque | (see dedicated page) |
| cpp/container/dsc erase|deque | (see dedicated page) |
| cpp/container/dsc push_back|deque | (see dedicated page) |
| cpp/container/dsc emplace_back|deque | (see dedicated page) |
| cpp/container/dsc append_range|deque | (see dedicated page) |
| cpp/container/dsc pop_back|deque | (see dedicated page) |
| cpp/container/dsc push_front|deque | (see dedicated page) |
| cpp/container/dsc emplace_front|deque | (see dedicated page) |
| cpp/container/dsc prepend_range|deque | (see dedicated page) |
| cpp/container/dsc pop_front|deque | (see dedicated page) |
| cpp/container/dsc resize|deque | (see dedicated page) |
| cpp/container/dsc swap|deque | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|deque | (see dedicated page) |
| cpp/container/dsc swap2|deque | (see dedicated page) |
| cpp/container/dsc erase seq|deque | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


## Example


### Example

```cpp
#include <deque>
#include <iostream>

int main()
{
    // Create a deque containing integers
    std::deque<int> d = {7, 5, 16, 8};

    // Add an integer to the beginning and end of the deque
    d.push_front(13);
    d.push_back(25);

    // Iterate and print values of deque
    for (int n : d)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
13 7 5 16 8 25
```


## Defect reports


## See also


| cpp/container/dsc queue | (see dedicated page) |

