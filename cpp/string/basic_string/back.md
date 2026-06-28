---
title: std::basic_string::back
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/back
---


```cpp
dcla|num=1|constexpr=c++20|
CharT& back();
dcla|num=2|constexpr=c++20|
const CharT& back() const;
```

Returns reference to the last character in the string.

## Return value

`operator[](size() - 1)`

## Complexity

Constant.

## Notes

In libstdc++, `back()` is [https://gcc.gnu.org/onlinedocs/libstdc++/manual/strings.html#strings.string.shrink not available] in C++98 mode.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string s("Exemplary");
    char& back1 = s.back();
    back1 = 's';
    std::cout << s << '\n'; // "Exemplars"

    std::string const c("Exemplary");
    char const& back2 = c.back();
    std::cout << back2 << '\n'; // 'y'
}
```


**Output:**
```
Exemplars
y
```


## Defect reports


## See also


| cpp/string/basic_string/dsc front | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |

