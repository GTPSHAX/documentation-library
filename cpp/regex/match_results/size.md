---
title: std::match_results::size
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/size
---

ddcl|since=c++11|
size_type size() const noexcept;
Returns the number of submatches, i.e. `std::distance(begin(), end())`.
Returns `0` if `*this` does not represent the result of a successful match.

## Parameters

(none)

## Return value

The number of submatches.

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <regex>
#include <string>

int main()
{
    std::regex re("a(a)*b");
    std::string target("aaab");
    std::smatch sm;

    std::cout << sm.size() << '\n';

    std::regex_match(target, sm, re);
    std::cout << sm.size() << '\n';
}
```


**Output:**
```
0
2
```


## See also


| cpp/regex/match_results/dsc begin | (see dedicated page) |
| cpp/regex/match_results/dsc end | (see dedicated page) |

