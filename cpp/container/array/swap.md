---
title: std::array::swap
type: Containers
source: https://en.cppreference.com/w/cpp/container/array/swap
---

ddcl|since=c++11|notes=<sup>(constexpr C++20)</sup>|
void swap( array& other ) noexcept(/* see below */);
Exchanges the contents of the container with those of `other`. Does not cause iterators and references to associate with the other container.

## Parameters


### Parameters

- `other` - container to exchange the contents with

## Return value

(none)

## Exceptions

rrev multi|until1=c++17|rev1=
In the expression above, the identifier `swap` is looked up in the same manner as the one used by the C++17 `std::is_nothrow_swappable` trait.
|rev2=
For zero-sized arrays,

## Complexity

Linear in size of the container.

## Example


### Example

```cpp
#include <array>
#include <iostream>

template<class Os, class V> Os& operator<<(Os& os, const V& v)
{
    os << '{';
    for (auto i : v)
        os << ' ' << i;
    return os << " } ";
}

int main()
{
    std::array<int, 3> a1{1, 2, 3}, a2{4, 5, 6};

    auto it1 = a1.begin();
    auto it2 = a2.begin();
    int& ref1 = a1[1];
    int& ref2 = a2[1];

    std::cout << a1 << a2 << *it1 << ' ' << *it2 << ' ' << ref1 << ' ' << ref2 << '\n';
    a1.swap(a2);
    std::cout << a1 << a2 << *it1 << ' ' << *it2 << ' ' << ref1 << ' ' << ref2 << '\n';

    // Note that after swap iterators and references stay associated with their original
    // array, e.g. `it1` still points to element a1[0], `ref1` still refers to a1[1].
}
```


**Output:**
```
{ 1 2 3 } { 4 5 6 } 1 4 2 5
{ 4 5 6 } { 1 2 3 } 4 1 5 2
```


## Defect reports


## See also


| cpp/container/dsc swap2|array | (see dedicated page) |

