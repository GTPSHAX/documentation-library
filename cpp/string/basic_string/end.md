---
title: std::basic_string::cend
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/end
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|
iterator end();
dcla|anchor=no|num=2|noexcept=c++11|constexpr=c++20|
const_iterator end() const;
dcla|anchor=no|num=3|constexpr=c++20|since=c++11|
const_iterator cend() const noexcept;
```

Returns an iterator to the character following the last character of the string. This character acts as a placeholder, attempting to access it results in undefined behavior.

## Parameters

(none)

## Return value

Iterator to the character following the last character.

## Complexity

Constant.

## Notes

libc++ backports `cend()` to C++98 mode.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::string s("Exemparl");
    std::next_permutation(s.begin(), s.end());

    std::string c;
    std::copy(s.cbegin(), s.cend(), std::back_inserter(c));
    std::cout << c << '\n'; // "Exemplar"
}
```


**Output:**
```
Exemplar
```


## See also


| cpp/string/basic_string/dsc begin | (see dedicated page) |
| cpp/string/basic_string_view/dsc end | (see dedicated page) |

