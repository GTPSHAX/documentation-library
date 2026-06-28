---
title: std::basic_string::data
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/data
---


```cpp
<br><sup>(constexpr C++20)</sup>|
const CharT* data() const;
|since=c++17|
CharT* data() noexcept;
```

Returns a pointer to the first element of the underlying array serving as character storage. The pointer is such that the range
rrev multi|until1=c++11
|rev1=
[data(), data() + size())
|rev2=
is valid and the values in it correspond to the values stored in the string.
rrev multi|until1=c++11|rev1=
The returned array is not required to be null-terminated.
If `empty()` returns `true`, the pointer is a non-null pointer that should not be dereferenced.
|rev2=
The returned array is null-terminated, that is, `data()` and `c_str()` perform the same function.
If `empty()` returns `true`, the pointer points to a single null character.
The pointer obtained from `data()` may be invalidated by:
* Passing a non-const reference to the string to any standard library function, or
* Calling non-const member functions on the string, excluding `operator[]()`, `at()`, `front()`, `back()`, `begin()`, `end()`, `rbegin()`, `rend()`.
1. Modifying the character array accessed through the const overload of `data` has undefined behavior.
2. Modifying the past-the-end null terminator stored at `data() + ``size()` to any value other than `CharT()` has undefined behavior.

## Parameters

(none)

## Return value

A pointer to the underlying character storage.
rrev multi|until1=c++11|rev1=
`1=data()[i] == operator[](i)` for every `i` in [0, size()).
|rev2=
`1=data() + i == std::addressof(operator[](i))` for every `i` in .

## Complexity

Constant.

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <cstring>
#include <string>

int main()
{
    std::string const s("Emplary");
    assert(s.size() == std::strlen(s.data()));
    assert(std::equal(s.begin(), s.end(), s.data()));
    assert(std::equal(s.data(), s.data() + s.size(), s.begin()));
    assert('\0' == *(s.data() + s.size()));
}
```


## See also


| cpp/string/basic_string/dsc front | (see dedicated page) |
| cpp/string/basic_string/dsc back | (see dedicated page) |
| cpp/string/basic_string/dsc c_str | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |

