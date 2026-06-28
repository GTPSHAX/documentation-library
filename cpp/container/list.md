---
title: std::list
type: Containers
source: https://en.cppreference.com/w/cpp/container/list
---


```cpp
**Header:** `<`list`>`
dcl|num=1|1=
template<
class T,
class Allocator = std::allocator<T>
> class list;
dcl|num=2|since=c++17|1=
namespace pmr {
template< class T >
using list = std::list<T, std::pmr::polymorphic_allocator<T>>;
}
```

`std::list` is a container that supports constant time insertion and removal of elements from anywhere in the container. Fast random access is not supported. It is usually implemented as a doubly-linked list. Compared to `std::forward_list` this container provides bidirectional iteration capability while being less space efficient.
Adding, removing and moving the elements within the list or across several lists does not invalidate the iterators or references. An iterator is invalidated only when the corresponding element is deleted.
`std::list` meets the requirements of *Container*, *AllocatorAwareContainer*, *SequenceContainer* and *ReversibleContainer*.

## Template parameters


### Parameters


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc value_type|list | (see dedicated page) |
| cpp/container/dsc allocator_type|list | (see dedicated page) |
| cpp/container/dsc size_type|list | (see dedicated page) |
| cpp/container/dsc difference_type|list | (see dedicated page) |
| cpp/container/dsc reference|list | (see dedicated page) |
| cpp/container/dsc const_reference|list | (see dedicated page) |
| cpp/container/dsc pointer|list | (see dedicated page) |
| cpp/container/dsc const_pointer|list | (see dedicated page) |
| cpp/container/dsc iterator|list | (see dedicated page) |
| cpp/container/dsc const_iterator|list | (see dedicated page) |
| cpp/container/dsc reverse_iterator|list | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|list | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|list | (see dedicated page) |
| cpp/container/dsc destructor|list | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |
| cpp/container/dsc assign|list | (see dedicated page) |
| cpp/container/dsc assign_range|list | (see dedicated page) |
| cpp/container/dsc get_allocator|list | (see dedicated page) |

#### Element access

| cpp/container/dsc front|list | (see dedicated page) |
| cpp/container/dsc back|list | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|list | (see dedicated page) |
| cpp/container/dsc end|list | (see dedicated page) |
| cpp/container/dsc rbegin|list | (see dedicated page) |
| cpp/container/dsc rend|list | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|list | (see dedicated page) |
| cpp/container/dsc size|list | (see dedicated page) |
| cpp/container/dsc max_size|list | (see dedicated page) |

#### Modifiers

| cpp/container/dsc clear|list | (see dedicated page) |
| cpp/container/dsc insert|list | (see dedicated page) |
| cpp/container/dsc insert_range|list | (see dedicated page) |
| cpp/container/dsc emplace|list | (see dedicated page) |
| cpp/container/dsc erase|list | (see dedicated page) |
| cpp/container/dsc push_back|list | (see dedicated page) |
| cpp/container/dsc emplace_back|list | (see dedicated page) |
| cpp/container/dsc append_range|list | (see dedicated page) |
| cpp/container/dsc pop_back|list | (see dedicated page) |
| cpp/container/dsc push_front|list | (see dedicated page) |
| cpp/container/dsc emplace_front|list | (see dedicated page) |
| cpp/container/dsc prepend_range|list | (see dedicated page) |
| cpp/container/dsc pop_front|list | (see dedicated page) |
| cpp/container/dsc resize|list | (see dedicated page) |
| cpp/container/dsc swap|list | (see dedicated page) |

#### Operations

| cpp/container/dsc merge|list | (see dedicated page) |
| cpp/container/dsc splice|list | (see dedicated page) |
| cpp/container/dsc remove|list | (see dedicated page) |
| cpp/container/dsc reverse|list | (see dedicated page) |
| cpp/container/dsc unique|list | (see dedicated page) |
| cpp/container/dsc sort|list | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|list | (see dedicated page) |
| cpp/container/dsc swap2|list | (see dedicated page) |
| cpp/container/dsc erase seq|list | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <list>

int main()
{
    // Create a list containing integers
    std::list<int> l = {7, 5, 16, 8};

    // Add an integer to the front of the list
    l.push_front(25);
    // Add an integer to the back of the list
    l.push_back(13);

    // Insert an integer before 16 by searching
    auto it = std::find(l.begin(), l.end(), 16);
    if (it != l.end())
        l.insert(it, 42);

    // Print out the list
    std::cout << "l = { ";
    for (int n : l)
        std::cout << n << ", ";
    std::cout << "};\n";
}
```


**Output:**
```
l = { 25, 7, 5, 42, 16, 8, 13, };
```


## Defect reports


## See also


| cpp/container/dsc forward_list | (see dedicated page) |

