---
title: std::match_results::prefix
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/prefix
---

ddcl|since=c++11|
const_reference prefix() const;
Obtains a reference to the `std::sub_match` object representing the target sequence between the start of the beginning of the target sequence and the start of the entire match of the regular expression.

## Return value

Reference to the unmatched prefix.

## Example


### Example

```cpp
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::regex re("a(a)*b");
    std::string target("baaaby");
    std::smatch sm;

    std::regex_search(target, sm, re);
    std::cout << sm.prefix().str() << '\n';
}
```


**Output:**
```
b
```


## See also


| cpp/regex/match_results/dsc suffix | (see dedicated page) |

