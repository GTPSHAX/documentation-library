---
title: std::basic_string::shrink_to_fit
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/shrink_to_fit
---

ddcla|constexpr=c++20|
void shrink_to_fit();
Requests the removal of unused capacity.
It is a non-binding request to reduce `capacity()` to `size()`. It depends on the implementation if the request is fulfilled.
If (and only if) reallocation takes place, all pointers, references, and iterators are invalidated.

## Complexity

Linear in the size of the string.

## Notes

In libstdc++, `shrink_to_fit()` is [https://gcc.gnu.org/onlinedocs/libstdc++/manual/strings.html#strings.string.shrink not available] in C++98 mode.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::cout << "Size of std::string is " << sizeof s << " bytes\n"
        << "Default-constructed capacity is " << s.capacity() 
        << " and size is " << s.size() << '\n';

    for (int i = 0; i < 42; i++)
        s.append(" 42 ");
    std::cout << "Capacity after 42 appends is " << s.capacity() 
        << " and size is " << s.size() << '\n';

    s.clear();
    std::cout << "Capacity after clear() is " << s.capacity() 
        << " and size is " << s.size() << '\n';

    s.shrink_to_fit();
    std::cout << "Capacity after shrink_to_fit() is " << s.capacity() 
        << " and size is " << s.size() << '\n';
}
```


**Output:**
```
GCC output:
Size of std::string is 32 bytes
Default-constructed capacity is 15 and size 0
Capacity after 42 appends is 240 and size 168
Capacity after clear() is 240 and size 0
Capacity after shrink_to_fit() is 15 and size 0

clang output (with -stdlib=libc++):
Size of std::string is 24 bytes
Default-constructed capacity is 22 and size is 0
Capacity after 42 appends is 191 and size is 168
Capacity after clear() is 191 and size is 0
Capacity after shrink_to_fit() is 22 and size is 0
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2223 | C++98 | 1. references, pointers, and iterators were not invalidated<br>2. there was no complexity requirement | 1. they may be invalidated<br>2. required to be linear |


## See also


| cpp/string/basic_string/dsc size | (see dedicated page) |
| cpp/string/basic_string/dsc capacity | (see dedicated page) |
| cpp/string/basic_string/dsc resize | (see dedicated page) |

