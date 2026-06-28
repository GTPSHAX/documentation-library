---
title: std::basic_string::c_str
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/c_str
---

ddcla|noexcept=c++11|constexpr=c++20|
const CharT* c_str() const;
Returns a pointer to a null-terminated character array with data equivalent to those stored in the string.
The pointer is such that the range  is valid and the values in it correspond to the values stored in the string with an additional null character after the last position.
The pointer obtained from `c_str()` may be invalidated by:
* Passing a non-const reference to the string to any standard library function, or
* Calling non-const member functions on the string<sup>(since C++11)</sup> , excluding `operator[]`, `at()`, `front()`, `back()`, `begin()`, `rbegin()`, `end()` and `rend()`.
Writing to the character array accessed through `c_str()` is undefined behavior.
<sup>(since C++11)</sup> `c_str()` and `data()` perform the same function.

## Parameters

(none)

## Return value

Pointer to the underlying character storage.
rrev multi|until1=c++11
|rev1=
`1=c_str()[i] == operator[](i)` for every `i` in [0, size()).
|rev2=
`1=c_str() + i == std::addressof(operator[](i))` for every `i` in .

## Complexity

Constant.

## Notes

The pointer obtained from `c_str()` may only be treated as a pointer to a null-terminated character string if the string object does not contain other null characters.

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <cstring>
#include <string>

extern "C" void c_func(const char* c_str)
{
    printf("c_func called with '%s'\n", c_str);
}

int main()
{
    std::string const s("Emplary");
    const char* p = s.c_str();
    assert(s.size() == std::strlen(p));
    assert(std::equal(s.begin(), s.end(), p));
    assert(std::equal(p, p + s.size(), s.begin()));
    assert('\0' == *(p + s.size()));

    c_func(s.c_str());
}
```


**Output:**
```
c_func called with 'Emplary'
```


## See also


| cpp/string/basic_string/dsc front | (see dedicated page) |
| cpp/string/basic_string/dsc back | (see dedicated page) |
| cpp/string/basic_string/dsc data | (see dedicated page) |

