---
title: std::basic_string::front
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/front
---


```cpp
dcla|num=1|constexpr=c++20|
CharT& front();
dcla|num=2|constexpr=c++20|
const CharT& front() const;
```

Returns reference to the first character in the string.

## Return value

`operator[](0)`

## Complexity

Constant.

## Notes

In libstdc++, `front()` is [https://gcc.gnu.org/onlinedocs/libstdc++/manual/strings.html#strings.string.shrink not available] in C++98 mode.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string s("Exemplary");
    char& f1 = s.front();
    f1 = 'e';
    std::cout << s << '\n'; // "exemplary"

    std::string const c("Exemplary");
    char const& f2 = c.front();
    std::cout << &f2 << '\n'; // "Exemplary"
}
```


**Output:**
```
exemplary
Exemplary
```


## Defect reports


## See also


| cpp/string/basic_string/dsc back | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |

