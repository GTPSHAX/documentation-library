---
title: std::priority_queue
type: Containers
source: https://en.cppreference.com/w/cpp/container/priority_queue
---

ddcl|header=queue|1=
template<
class T,
class Container = std::vector<T>,
class Compare = std::less<typename Container::value_type>
> class priority_queue;
The [Queue (abstract data type)|priority queue](https://en.wikipedia.org/wiki/Queue (abstract data type)|priority queue) is a container adaptor that provides constant time lookup of the largest (by default) element, at the expense of logarithmic insertion and extraction.
A user-provided `Compare` can be supplied to change the ordering, e.g. using `std::greater<T>` would cause the smallest element to appear as the `top()`.
Working with a `priority_queue` is similar to managing a heap in some random access container, with the benefit of not being able to accidentally invalidate the heap.

## Template parameters


### Parameters

- `T` - The type of the stored elements. The program is ill-formed if `T` is not the same type as `Container::value_type`.
- `Container` - The type of the underlying container to use to store the elements. The container must satisfy the requirements of *SequenceContainer*, and its iterators must satisfy the requirements of *RandomAccessIterator*. Additionally, it must provide the following functions with the usual semantics:
- * `front()`, e.g., `std::vector::front()`,
- * `push_back()`, e.g., `std::deque::push_back()`,
- * `pop_back()`, e.g., `std::vector::pop_back()`.
- The standard containers `std::vector` (not including `std::vector<bool>`) and `std::deque` satisfy these requirements.
- `Compare` - A *Compare* type providing a strict weak ordering.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| cpp/container/dsc container_type|priority_queue | (see dedicated page) |
| cpp/container/dsc value_type|priority_queue | (see dedicated page) |
| cpp/container/dsc size_type|priority_queue | (see dedicated page) |
| cpp/container/dsc reference|priority_queue | (see dedicated page) |
| cpp/container/dsc const_reference|priority_queue | (see dedicated page) |


## Member objects


| Item | Description |
|------|-------------|
| **Member** | Description |
| cpp/container/dsc c|priority_queue | (see dedicated page) |


## Member functions


| cpp/container/dsc constructor|priority_queue | (see dedicated page) |
| cpp/container/dsc destructor|priority_queue | (see dedicated page) |
| cpp/container/dsc operator{{= | (see dedicated page) |

#### Element access

| cpp/container/dsc top|priority_queue | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|priority_queue | (see dedicated page) |
| cpp/container/dsc size|priority_queue | (see dedicated page) |

#### Modifiers

| cpp/container/dsc push|priority_queue | (see dedicated page) |
| cpp/container/dsc push_range|priority_queue | (see dedicated page) |
| cpp/container/dsc emplace|priority_queue | (see dedicated page) |
| cpp/container/dsc pop|priority_queue | (see dedicated page) |
| cpp/container/dsc swap|priority_queue | (see dedicated page) |


## Non-member functions


| cpp/container/dsc swap2|priority_queue | (see dedicated page) |


## Helper classes


| cpp/container/dsc uses_allocator|priority_queue | (see dedicated page) |
| cpp/container/dsc adaptor_formatter|priority_queue | (see dedicated page) |

rrev|since=c++17|

## 


## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges-aware construction and insertion for containers |
| `__cpp_lib_constexpr_queue` | 202502L | C++26 | Constexpr `std::priority_queue` |


## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <queue>
#include <string_view>
#include <vector>

template<typename T>
void pop_println(std::string_view rem, T& pq)
{
    std::cout << rem << ": ";
    for (; !pq.empty(); pq.pop())
        std::cout << pq.top() << ' ';
    std::cout << '\n';
}

template<typename T>
void println(std::string_view rem, const T& v)
{
    std::cout << rem << ": ";
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    const auto data = {1, 8, 5, 6, 3, 4, 0, 9, 7, 2};
    println("data", data);

    std::priority_queue<int> max_priority_queue;

    // Fill the priority queue.
    for (int n : data)
        max_priority_queue.push(n);

    pop_println("max_priority_queue", max_priority_queue);

    // std::greater<int> makes the max priority queue act as a min priority queue.
    std::priority_queue<int, std::vector<int>, std::greater<int>>
        min_priority_queue1(data.begin(), data.end());

    pop_println("min_priority_queue1", min_priority_queue1);

    // Second way to define a min priority queue.
    std::priority_queue min_priority_queue2(data.begin(), data.end(), std::greater<int>());

    pop_println("min_priority_queue2", min_priority_queue2);

    // Using a custom function object to compare elements.
    struct
    {
        bool operator()(const int l, const int r) const { return l > r; }
    } customLess;

    std::priority_queue custom_priority_queue(data.begin(), data.end(), customLess);

    pop_println("custom_priority_queue", custom_priority_queue);

    // Using lambda to compare elements.
    auto cmp = [](int left, int right) { return (left ^ 1) < (right ^ 1); };
    std::priority_queue<int, std::vector<int>, decltype(cmp)> lambda_priority_queue(cmp);

    for (int n : data)
        lambda_priority_queue.push(n);

    pop_println("lambda_priority_queue", lambda_priority_queue);
}
```


**Output:**
```
data: 1 8 5 6 3 4 0 9 7 2
max_priority_queue: 9 8 7 6 5 4 3 2 1 0
min_priority_queue1: 0 1 2 3 4 5 6 7 8 9
min_priority_queue2: 0 1 2 3 4 5 6 7 8 9
custom_priority_queue: 0 1 2 3 4 5 6 7 8 9
lambda_priority_queue: 8 9 6 7 4 5 2 3 0 1
```


## Defect reports


## See also


| cpp/container/dsc vector | (see dedicated page) |
| cpp/container/dsc vector bool | (see dedicated page) |
| cpp/container/dsc deque | (see dedicated page) |

