---
title: std::vector<bool>
type: Containers
source: https://en.cppreference.com/w/cpp/container/vector_bool
---

ddcl|header=vector|
template<
class Allocator
> class vector<bool, Allocator>;
is a possibly space-efficient specialization of `std::vector` for the type `bool`.
The manner in which  is made space efficient (as well as whether it is optimized at all) is implementation defined. One potential optimization involves coalescing vector elements such that each element occupies a single bit instead of `sizeof(bool)` bytes.
behaves similarly to `std::vector`, but in order to be space efficient, it:
* Does not necessarily store its elements as a contiguous array.
* Exposes class  as a method of accessing individual bits. In particular, objects of this class are returned by `cpp/container/vector/operator at|operator[]` by value.
* Does not use `std::allocator_traits::construct` to construct bit values.
* Does not guarantee that different elements in the same container can be modified concurrently by different threads.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| cpp/container/dsc value_type|vector_bool | (see dedicated page) |
| cpp/container/dsc allocator_type|vector_bool | (see dedicated page) |
| cpp/container/dsc size_type|vector_bool | (see dedicated page) |
| cpp/container/dsc difference_type|vector_bool | (see dedicated page) |
| cpp/container/vector_bool/reference|proxy class representing a reference to a single `bool` | |
| cpp/container/dsc const_reference|vector_bool | (see dedicated page) |
| cpp/container/dsc pointer|vector_bool | (see dedicated page) |
| cpp/container/dsc const_pointer|vector_bool | (see dedicated page) |
| cpp/container/dsc iterator|vector_bool | (see dedicated page) |
| cpp/container/dsc const_iterator|vector_bool | (see dedicated page) |
| cpp/container/dsc reverse_iterator|vector_bool | (see dedicated page) |
| cpp/container/dsc const_reverse_iterator|vector_bool | (see dedicated page) |


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

#### Modifiers

| cpp/container/dsc clear|vector | (see dedicated page) |
| cpp/container/dsc insert|vector | (see dedicated page) |
| cpp/container/dsc insert_range|vector | (see dedicated page) |
| cpp/container/dsc append_range|vector | (see dedicated page) |
| cpp/container/dsc emplace|vector | (see dedicated page) |
| cpp/container/dsc erase|vector | (see dedicated page) |
| cpp/container/dsc push_back|vector | (see dedicated page) |
| cpp/container/dsc emplace_back|vector | (see dedicated page) |
| cpp/container/dsc pop_back|vector | (see dedicated page) |
| cpp/container/dsc resize|vector | (see dedicated page) |
| cpp/container/dsc swap|vector | (see dedicated page) |

#### {{tt|vector<bool>

| cpp/container/vector_bool/dsc flip | (see dedicated page) |
| cpp/container/vector_bool/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/container/dsc operator_cmp|vector | (see dedicated page) |
| cpp/container/dsc swap2|vector | (see dedicated page) |
| cpp/container/dsc erase seq|vector | (see dedicated page) |


## Helper classes


| cpp/container/vector_bool/dsc hash | (see dedicated page) |


## Deduction guides


## Notes

If the size of the bitset is known at compile time, `std::bitset` may be used, which offers a richer set of member functions. In addition, [https://www.boost.org/doc/libs/release/libs/dynamic_bitset/dynamic_bitset.html `boost::dynamic_bitset`] exists as an alternative to .
Since its representation may be optimized,  does not necessarily meet all *Container* or *SequenceContainer* requirements. For example, because  is implementation-defined, it may not satisfy the *ForwardIterator* requirement. Use of algorithms such as `std::search` that require *ForwardIterator*s may result in [https://www.boost.org/doc/libs/release/libs/dynamic_bitset/dynamic_bitset.html#rationale either compile-time or run-time errors].
The [https://www.boost.org/doc/libs/release/doc/html/boost/container/vector.html Boost.Container version of `vector`] does not specialize for `bool`.

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_containers_ranges` | 202202L | C++23 | Ranges construction and insertion for containers |


## Example


### Example

```cpp
#include <cassert>
#include <initializer_list>
#include <iostream>
#include <vector>

void println(auto rem, const std::vector<bool>& vb)
{
    std::cout << rem << " = [";
    for (std::size_t t{}; t != vb.size(); ++t)
        std::cout << (t ? ", " : "") << vb[t];
    std::cout << "]\n";
}

int main()
{
    std::vector<bool> v1; // creates an empty vector of boolean values
    println("1) v1", v1);

    std::vector<bool> v2{0, 1, 1, 0, 1}; // creates filled vector
    println("2) v2", v2);

    v1 = v2; // copies v2 to v1
    println("3) v1", v1);

    assert(v1.size() == v2.size()); // checks that v1 and v2 sizes are equal
    assert(v1.front() == false); // accesses first element, equivalent to:
    assert(v1[0] == false);
    assert(v1.back() == true); // accesses last element, equivalent to:
    assert(v1[v1.size() - 1] == true);

    v1 = {true, true, false, false}; // assigns an initializer list
    println("4) v1", v1);

    v1.push_back(true); // adds one element to the end
    println("5) v1", v1);

    v1.pop_back(); // removes one element from the end
    println("6) v1", v1);

    v1.flip(); // flips all elements
    println("7) v1", v1);

    v1.resize(8, true); // resizes v1; new elements are set to “true”
    println("8) v1", v1);

    v1.clear(); // erases v1
    assert(v1.empty()); // checks that v1 is empty
}
```


**Output:**
```
1) v1 = []
2) v2 = [0, 1, 1, 0, 1]
3) v1 = [0, 1, 1, 0, 1]
4) v1 = [1, 1, 0, 0]
5) v1 = [1, 1, 0, 0, 1]
6) v1 = [1, 1, 0, 0]
7) v1 = [0, 0, 1, 1]
8) v1 = [0, 0, 1, 1, 1, 1, 1, 1]
```


## Defect reports

