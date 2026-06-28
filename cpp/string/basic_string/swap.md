---
title: std::basic_string::swap
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/swap
---


```cpp
dcl rev multi
|until1=c++17|dcl1=
void swap( basic_string& other );
|notes2=<sup>(constexpr C++20)</sup>|dcl2=
void swap( basic_string& other ) noexcept(/* see below */);
```

Exchanges the contents of the string with those of `other`. All iterators and references may be invalidated.
rrev|since=c++11|
If `std::allocator_traits<allocator_type>::propagate_on_container_swap::value` is `true`, then the allocators are exchanged using an unqualified call to non-member `swap`. Otherwise, they are not swapped (and if `1=get_allocator() != other.get_allocator()`, the behavior is undefined).

## Parameters


### Parameters

- `other` - string to exchange the contents with

## Complexity

Constant.

## Exceptions

rev|until=c++11|
No exception is thrown.
rev|since=c++11|
No exception is thrown, unless the behavior is undefined.
rrev|since=c++17|
noexcept|std::allocator_traits<Allocator>::propagate_on_container_swap::value
std::allocator_traits<Allocator>::is_always_equal::value

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main() 
{
    std::string a = "AAA";
    std::string b = "BBBB";

    std::cout << "Before swap:\n"
                 "a = " << a << "\n"
                 "b = " << b << "\n\n";

    a.swap(b);

    std::cout << "After swap:\n"
                 "a = " << a << "\n"
                 "b = " << b << '\n';
}
```


**Output:**
```
Before swap:
a = AAA
b = BBBB

After swap:
a = BBBB
b = AAA
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-535 | C++98 | swapping strings did not preserve the character orders | orders are also preserved |


## See also


| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap_ranges | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |

