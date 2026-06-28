---
title: std::match_results::position
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/position
---

ddcl|since=c++11|
difference_type position( size_type n  0 ) const;
Returns the position of the first character of the specified sub-match.
If `1=n == 0`, the position of the first character of the entire matched expression is returned.
If `n > 0 && n < size()`, the position of the first character of the `n` sub-match is returned.
if `1=n >= size()`, a position of the first character of the unmatched match is returned.

## Parameters


### Parameters

- `n` - integral number specifying which match to examine

## Return value

The position of the first character of the specified match or sub-match.

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

    std::regex_match(target, sm, re);
    std::cout << sm.position(1) << '\n';
}
```


**Output:**
```
2
```


## See also


| cpp/regex/match_results/dsc operator_at | (see dedicated page) |

