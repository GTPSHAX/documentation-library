---
title: std::basic_string::operator[]
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/operator_at
---


```cpp
dcla|num=1|constexpr=c++20|
CharT& operator[]( size_type pos );
dcla|anchor=no|num=2|constexpr=c++20|
const CharT& operator[]( size_type pos ) const;
```

Returns a reference to the character at specified location `pos` if `pos < size()`, or if `1=pos == size()`:
1. rel|
rrev multi|until1=c++11|rev1=
The behavior is undefined.
|rev2=
Returns a reference to `CharT()`, if the object referred by the returned reference is modified to any value other than `CharT()`, the behavior is undefined.
2. Returns a reference to `CharT()`.

## Parameters


### Parameters

- `pos` - position of the character to return

## Return value

1. `*(begin() + pos)` if `pos < size()`<sup>(since C++11)</sup> , or a reference to `CharT()` if `1=pos == size()`.
2. `*(begin() + pos)` if `pos < size()`, or a reference to `CharT()` if `1=pos == size()`.

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    const std::string e("Exemplar");
    for (unsigned i = e.length() - 1; i != 0; i /= 2)
        std::cout << e[i];
    std::cout << '\n';

    const char* c = &e[0];
    std::cout << c << '\n'; // print as a C string

    // Change the last character of s into a 'y'
    std::string s("Exemplar ");
    s[s.size() - 1] = 'y'; // equivalent to s.back() = 'y';
    std::cout << s << '\n';
}
```


**Output:**
```
rmx
Exemplar
Exemplary
```


## Defect reports


## See also


| cpp/string/basic_string/dsc at | (see dedicated page) |
| cpp/string/basic_string/dsc front | (see dedicated page) |
| cpp/string/basic_string/dsc back | (see dedicated page) |
| cpp/string/basic_string_view/dsc operator at | (see dedicated page) |

