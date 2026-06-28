---
title: std::basic_string::reserve
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/reserve
---


```cpp
dcl rev multi|num=1|until1=c++20
|dcl1=
void reserve( size_type new_cap = 0 );
|dcl2=
constexpr void reserve( size_type new_cap );
dcl|num=2|since=c++20|deprecated=c++20|removed=c++26|
void reserve();
```

1. Informs a `std::basic_string` object of a planned change in size, so that it can manage the storage allocation appropriately.
* If `new_cap` is greater than the current `capacity()`, new storage is allocated, and `capacity()` is made equal or greater than `new_cap`.
rrev multi|until1=c++20|rev1=
* If `new_cap` is less than the current `capacity()`, this is a non-binding shrink request.
* If `new_cap` is less than the current `size()`, this is a non-binding shrink-to-fit request<sup>(since C++11)</sup>  equivalent to `shrink_to_fit()`.
|rev2=
* If `new_cap` is less than or equal to the current `capacity()`, there is no effect.
@@ If a capacity change takes place, all iterators and references, including the past-the-end iterator, are invalidated.
2. A non-binding shrink-to-fit request. After this call, `capacity()` has an unspecified value greater than or equal to `size()`.

## Parameters


### Parameters

- `new_cap` - new capacity of the string

## Return value

(none)

## Exceptions

Throws `std::length_error` if `new_cap` is greater than `max_size()`.
May throw any exceptions thrown by `std::allocator_traits<Allocator>::allocate()`, such as `std::bad_alloc`.

## Complexity

At most linear in the `size()` of the string.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::cout << "1) Initially: " << s.capacity() << '\n';

    const std::string::size_type new_cap{101u};
    s.reserve(new_cap);
    assert(s.capacity() >= new_cap);
    std::cout << "2) After reserve(" << new_cap << "): " << s.capacity() << '\n';

    // observing the capacity growth factor
    auto cap{s.capacity()};
    for (int check{}; check != 4; ++check)
    {
        while (cap == s.capacity())
            s += '$';
        cap = s.capacity();
        std::cout << (3) + check << ") Capacity: " << cap << '\n';
    }

//  s.reserve(); // deprecated/removed in C++20/26, use:
    s.shrink_to_fit();
    std::cout << "7) After shrink_to_fit: " << s.capacity() << '\n';
}
```


**Output:**
```
1) Initially: 15
2) After reserve(101): 101
3) Capacity: 202
4) Capacity: 404
5) Capacity: 808
6) Capacity: 1616
7) After shrink_to_fit: 809
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc capacity | (see dedicated page) |
| cpp/string/basic_string/dsc resize | (see dedicated page) |

