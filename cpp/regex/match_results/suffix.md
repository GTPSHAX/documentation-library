---
title: std::match_results::suffix
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/suffix
---

ddcl|since=c++11|
const_reference suffix() const;
Obtains a reference to the `std::sub_match` object representing the target sequence between the end of the entire match of the regular expression and the end of the target sequence.

## Parameters

(none)

## Return value

Reference to the unmatched suffix.

## Example


### Example

```cpp
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::regex re("a(a)*by");
    std::string target("baaaby123");
    std::smatch sm;

    std::regex_search(target, sm, re);
    std::cout << sm.suffix() << '\n';
}
```


**Output:**
```
123
```


## See also


| cpp/regex/match_results/dsc prefix | (see dedicated page) |

