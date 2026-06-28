---
title: std::basic_string::empty
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/empty
---

ddcla|noexcept=c++11|constexpr=c++20|
bool empty() const;
Checks if the string has no characters, i.e. whether `1=begin() == end()`.

## Parameters

(none)

## Return value

`true` if the string is empty, `false` otherwise

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::boolalpha(std::cout);
    std::cout << "s.empty():" << s.empty() << "\t s:'" << s << "'\n";

    s = "Exemplar";
    std::cout << "s.empty():" << s.empty() << "\t s:'" << s << "'\n";

    s = "";
    std::cout << "s.empty():" << s.empty() << "\t s:'" << s << "'\n";
}
```


**Output:**
```
s.empty():true   s:''
s.empty():false  s:'Exemplar'
s.empty():true   s:''
```


## See also


| cpp/string/basic_string/dsc size | (see dedicated page) |
| cpp/string/basic_string/dsc max_size | (see dedicated page) |
| cpp/string/basic_string/dsc capacity | (see dedicated page) |
| cpp/iterator/dsc size | (see dedicated page) |
| cpp/iterator/dsc empty | (see dedicated page) |
| cpp/string/basic_string_view/dsc empty | (see dedicated page) |

