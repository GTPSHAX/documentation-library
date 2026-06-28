---
title: std::basic_string::pop_back
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/pop_back
---

ddcla|constexpr=c++20|
void pop_back();
Removes the last character from the string.
Equivalent to `erase(end() - 1)`.

## Complexity

Constant.

## Exceptions

Throws nothing.

## Notes

In libstdc++, `pop_back()` is [https://gcc.gnu.org/onlinedocs/libstdc++/manual/strings.html#strings.string.shrink not available] in C++98 mode.

## Example


### Example

```cpp
#include <cassert>
#include <iomanip>
#include <iostream>
#include <string>

int main()
{
    std::string str("Short string!");
    std::cout << "Before: " << std::quoted(str) << '\n';
    assert(str.size() == 13);

    str.pop_back();
    std::cout << "After:  " << std::quoted(str) << '\n';
    assert(str.size() == 12);

    str.clear();
//  str.pop_back(); // undefined behavior
}
```


**Output:**
```
Before: "Short string!"
After:  "Short string"
```


## Defect reports


## See also


| cpp/string/basic_string/dsc push_back | (see dedicated page) |
| cpp/string/basic_string/dsc erase | (see dedicated page) |

