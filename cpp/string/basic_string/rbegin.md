---
title: std::basic_string::crbegin
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/rbegin
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|
reverse_iterator rbegin();
dcla|anchor=no|num=2|noexcept=c++11|constexpr=c++20|
const_reverse_iterator rbegin() const;
dcla|anchor=no|num=3|since=c++11|constexpr=c++20|
const_reverse_iterator crbegin() const noexcept;
```

Returns a reverse iterator to the first character of the reversed string. It corresponds to the last character of the non-reversed string.

## Parameters

(none)

## Return value

Reverse iterator to the first character.

## Complexity

Constant.

## Notes

libc++ backports `crbegin()` to C++98 mode.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::string s("Exemplar!");
    *s.rbegin() = 'y';
    std::cout << s << '\n'; // "Exemplary"

    std::string c;
    std::copy(s.crbegin(), s.crend(), std::back_inserter(c));
    std::cout << c << '\n'; // "yralpmexE"
}
```


**Output:**
```
Exemplary
yralpmexE
```


## See also


| cpp/string/basic_string/dsc rend | (see dedicated page) |
| cpp/string/basic_string_view/dsc rbegin | (see dedicated page) |

