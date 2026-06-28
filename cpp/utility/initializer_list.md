---
title: std::initializer_list
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/initializer_list
---

ddcl|header=initializer_list|since=c++11|
template< class T >
class initializer_list;
An object of type `std::initializer_list<T>` is a lightweight proxy object that provides access to an array of objects of type `const T` (that may be allocated in read-only memory).
A `std::initializer_list` object is automatically constructed when:
* a brace-enclosed initializer list is used to list-initialize an object, where the corresponding constructor accepts an `std::initializer_list` parameter,
* a brace-enclosed initializer list is used as the right operand of assignment or as a function call argument, and the corresponding assignment operator/function accepts an `std::initializer_list` parameter,
* a brace-enclosed initializer list is bound to `cpp/language/auto`, including in a ranged for loop.
`std::initializer_list` may be implemented as a pair of pointers or pointer and length. Copying a `std::initializer_list` does not copy the backing array of the corresponding initializer list.
The program is ill-formed if an explicit or partial specialization of `std::initializer_list` is declared.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Member functions


| cpp/utility/initializer_list/dsc constructor | (see dedicated page) |

#### Capacity

| cpp/utility/initializer_list/dsc size | (see dedicated page) |
| cpp/utility/initializer_list/dsc empty | (see dedicated page) |

#### Iterators

| cpp/utility/initializer_list/dsc begin | (see dedicated page) |
| cpp/utility/initializer_list/dsc end | (see dedicated page) |
| cpp/utility/initializer_list/dsc data | (see dedicated page) |


## Non-member functions


#### Free function templates overloaded for {{tt|std::initializer_list

| cpp/iterator/dsc rbegin | (see dedicated page) |
| cpp/iterator/dsc rend | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <cassert>
#include <initializer_list>
#include <iostream>
#include <vector>

template<class T>
struct S
{
    std::vector<T> v;

    S(std::initializer_list<T> l) : v(l)
    {
         std::cout << "constructed with a " << l.size() << "-element list\n";
    }

    void append(std::initializer_list<T> l)
    {
        v.insert(v.end(), l.begin(), l.end());
    }

    std::pair<const T*, std::size_t> c_arr() const
    {
        return {&v[0], v.size()}; // copy list-initialization in return statement
                                  // this is NOT a use of std::initializer_list
    }
};

template<typename T>
void templated_fn(T) {}

int main()
{
    S<int> s = {1, 2, 3, 4, 5}; // copy list-initialization
    s.append({6, 7, 8});        // list-initialization in function call

    std::cout << "The vector now has " << s.c_arr().second << " ints:\n";    
    for (auto n : s.v)
        std::cout << n << ' ';
    std::cout << '\n';

    std::cout << "Range-for over brace-init-list: \n";
    for (int x : {-1, -2, -3}) // the rule for auto makes this ranged-for work
        std::cout << x << ' ';
    std::cout << '\n';

    auto al = {10, 11, 12}; // special rule for auto
    std::cout << "The list bound to auto has size() = " << al.size() << '\n';
    auto la = al; // a shallow-copy of top-level proxy object
    assert(la.begin() == al.begin()); // guaranteed: backing array is the same

    std::initializer_list<int> il{-3, -2, -1};
    assert(il.begin()[2] == -1); // note the replacement for absent operator[]
    il = al; // shallow-copy
    assert(il.begin() == al.begin()); // guaranteed

//  templated_fn({1, 2, 3}); // compiler error! "{1, 2, 3}" is not an expression,
                             // it has no type, and so T cannot be deduced
    templated_fn<std::initializer_list<int>>({1, 2, 3}); // OK
    templated_fn<std::vector<int>>({1, 2, 3});           // also OK
}
```


**Output:**
```
constructed with a 5-element list
The vector now has 8 ints:
1 2 3 4 5 6 7 8
Range-for over brace-init-list:
-1 -2 -3
The list bound to auto has size() = 3
```


## Defect reports


## See also


| cpp/container/dsc span | (see dedicated page) |
| cpp/string/dsc basic_string_view | (see dedicated page) |

