---
title: std::array
type: Containers
source: https://en.cppreference.com/w/cpp/container/array
---

ddcl|header=array|since=c++11|
template<
class T,
std::size_t N
> struct array;
`std::array` is a container that encapsulates fixed size arrays.
This container is an aggregate type with the same semantics as a struct holding a C-style array `T[N]` as its only non-static data member. Unlike a C-style array, it doesn't decay to `T*` automatically. As an aggregate type, it can be initialized with aggregate-initialization given at most `N` initializers that are convertible to `T`: }.
The struct combines the performance and accessibility of a C-style array with the benefits of a standard container, such as knowing its own size, supporting assignment, random access iterators, etc.
`std::array` satisfies the requirements of *Container* and *ReversibleContainer* except that default-constructed array is not empty and that the complexity of swapping is linear, <sup>(since C++17)</sup> satisfies the requirements of *ContiguousContainer,* and partially satisfies the requirements of *SequenceContainer*.
There is a special case for a zero-length array (`1=N == 0`). In that case, c|
1=array.begin() == array.end(), which is some unique value. The effect of calling `front()` or `back()` on a zero-sized array is undefined.
An array can also be used as a tuple of `N` elements of the same type.

## Iterator invalidation

As a rule, iterators to an array are never invalidated throughout the lifetime of the array. One should take note, however, that during , the iterator will continue to point to the same array element, and will thus change its value.

## Template parameters


### Parameters

- `T` - the element type. The requirements that are imposed on the elements depend on the actual operations performed on the container. Generally, it is required that element type is a complete type and meets the requirements of *Erasable*, but some member functions impose stricter requirements
- `N` - the number of elements in the array (might be `0`)

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc value_type|array | (see dedicated page) |
| cpp/container/dsc size_type|array | (see dedicated page) |
| cpp/container/dsc difference_type|array | (see dedicated page) |
| cpp/container/dsc reference|array | (see dedicated page) |
| cpp/container/dsc const_reference|array | (see dedicated page) |
| cpp/container/dsc pointer|array | (see dedicated page) |
| cpp/container/dsc const_pointer|array | (see dedicated page) |
| cpp/container/dsc iterator|array | (see dedicated page) |
| cpp/container/dsc const_iterator|array | (see dedicated page) |
| cpp/container/dsc reverse_iterator|array | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|array | (see dedicated page) |


## Member functions


#### Implicitly-defined member functions


#### Element access

| cpp/container/dsc at|array | (see dedicated page) |
| cpp/container/dsc operator_at|array | (see dedicated page) |
| cpp/container/dsc front|array | (see dedicated page) |
| cpp/container/dsc back|array | (see dedicated page) |
| cpp/container/dsc data|array | (see dedicated page) |

#### Iterators

| cpp/container/dsc begin|array | (see dedicated page) |
| cpp/container/dsc end|array | (see dedicated page) |
| cpp/container/dsc rbegin|array | (see dedicated page) |
| cpp/container/dsc rend|array | (see dedicated page) |

#### Capacity

| cpp/container/dsc empty|array | (see dedicated page) |
| cpp/container/dsc size|array | (see dedicated page) |
| cpp/container/dsc max_size|array | (see dedicated page) |

#### Operations

| cpp/container/dsc fill|array | (see dedicated page) |
| cpp/container/dsc swap|array | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|array | (see dedicated page) |
| cpp/container/array/dsc get | (see dedicated page) |
| cpp/container/dsc swap2|array | (see dedicated page) |
| cpp/container/array/dsc to_array | (see dedicated page) |


## Helper classes


| cpp/container/array/dsc tuple_size | (see dedicated page) |
| cpp/container/array/dsc tuple_element | (see dedicated page) |

rrev|since=c++17|

## 


## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    // Construction uses aggregate initialization
    std::array<int, 3> a1{<!---->{1, 2, 3}<!---->}; // Double-braces required in C++11 prior to
                                      // the CWG 1270 revision (not needed in C++11
                                      // after the revision and in C++14 and beyond)

    std::array<int, 3> a2 = {1, 2, 3}; // Double braces never required after =

    // Container operations are supported
    std::sort(a1.begin(), a1.end());
    std::ranges::reverse_copy(a2, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    // Ranged for loop is supported
    std::array<std::string, 2> a3{"E", "\u018E"};
    for (const auto& s : a3)
        std::cout << s << ' ';
    std::cout << '\n';

    // Deduction guide for array creation (since C++17)
    [[maybe_unused]] std::array a4{3.0, 1.0, 4.0}; // std::array<double, 3>

    // Behavior of unspecified elements is the same as with built-in arrays
    [[maybe_unused]] std::array<int, 2> a5; // No list init, a5[0] and a5[1]
                                            // are default initialized
    [[maybe_unused]] std::array<int, 2> a6{}; // List init, both elements are value
                                              // initialized, a6[0] = a6[1] = 0
    [[maybe_unused]] std::array<int, 2> a7{1}; // List init, unspecified element is value
                                               // initialized, a7[0] = 1, a7[1] = 0
}
```


**Output:**
```
3 2 1
E Ǝ
```


## See also


| cpp/container/dsc inplace_vector | (see dedicated page) |
| cpp/container/dsc vector | (see dedicated page) |
| cpp/container/dsc deque | (see dedicated page) |
| cpp/experimental/dsc make_array | (see dedicated page) |

