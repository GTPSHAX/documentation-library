---
title: std::queue
type: Containers
source: https://en.cppreference.com/w/cpp/container/queue
---

ddcl|header=queue|1=
template<
class T,
class Container = std::deque<T>
> class queue;
The `std::queue` class template is a container adaptor that gives the functionality of a [Queue (abstract data type)|queue](https://en.wikipedia.org/wiki/Queue (abstract data type)|queue) - specifically, a FIFO (first-in, first-out) data structure.
The class template acts as a wrapper to the underlying container - only a specific set of functions is provided. The queue pushes the elements on the back of the underlying container and pops them from the front.

## Template parameters


### Parameters

- `T` - The type of the stored elements. The program is ill-formed if `T` is not the same type as `Container::value_type`.
- `Container` - The type of the underlying container to use to store the elements. The container must satisfy the requirements of *SequenceContainer*. Additionally, it must provide the following functions with the usual semantics:
- * `back()`, e.g., `std::deque::back()`,
- * `front()`, e.g. `std::list::front()`,
- * `push_back()`, e.g., `std::deque::push_back()`,
- * `pop_front()`, e.g., `std::list::pop_front()`.
- The standard containers `std::deque` and `std::list` satisfy these requirements.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc container_type|queue | (see dedicated page) |
| cpp/container/dsc value_type|queue | (see dedicated page) |
| cpp/container/dsc size_type|queue | (see dedicated page) |
| cpp/container/dsc reference|queue | (see dedicated page) |
| cpp/container/dsc const_reference|queue | (see dedicated page) |


## Member objects


| Item | Description |
|------|-------------|
| **Member** | Description |
| cpp/container/dsc c|queue | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|queue | (see dedicated page) |
| cpp/container/dsc destructor|queue | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |

#### Element access

| cpp/container/dsc front|queue | (see dedicated page) |
| cpp/container/dsc back|queue | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|queue | (see dedicated page) |
| cpp/container/dsc size|queue | (see dedicated page) |

#### Modifiers

| cpp/container/dsc push|queue | (see dedicated page) |
| cpp/container/dsc push_range|queue | (see dedicated page) |
| cpp/container/dsc emplace|queue | (see dedicated page) |
| cpp/container/dsc pop|queue | (see dedicated page) |
| cpp/container/dsc swap|queue | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|queue | (see dedicated page) |
| cpp/container/dsc swap2|queue | (see dedicated page) |


## Helper classes


| cpp/container/dsc uses_allocator|queue | (see dedicated page) |
| cpp/container/dsc adaptor_formatter|queue | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |
| `__cpp_lib_constexpr_queue` | 202502L | C++26 | Constexpr `std::queue` |


## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <queue>

int main()
{
    std::queue<int> q;

    q.push(0); // back pushes 0
    q.push(1); // q = 0 1
    q.push(2); // q = 0 1 2
    q.push(3); // q = 0 1 2 3

    assert(q.front() == 0);
    assert(q.back() == 3);
    assert(q.size() == 4);

    q.pop(); // removes the front element, 0
    assert(q.size() == 3);

    // Print and remove all elements. Note that std::queue does not
    // support begin()/end(), so a range-for-loop cannot be used.
    std::cout << "q: ";
    for (; !q.empty(); q.pop())
        std::cout << q.front() << ' ';
    std::cout << '\n';
    assert(q.size() == 0);
}
```


**Output:**
```
q: 1 2 3
```


## Defect reports


## See also


| cpp/container/dsc priority_queue | (see dedicated page) |
| cpp/container/dsc deque | (see dedicated page) |
| cpp/container/dsc list | (see dedicated page) |

