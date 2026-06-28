---
title: std::regex_error
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_error
---

ddcl|header=regex|since=c++11|1=
class regex_error;
Defines the type of exception object thrown to report errors in the regular expressions library.

## Member functions


| cpp/regex/regex_error/dsc regex_error | (see dedicated page) |
| cpp/regex/regex_error/dsc operator{{= | (see dedicated page) |
| cpp/regex/regex_error/dsc code | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <regex>

int main()
{
    try
    {
        std::regex re("[a-b][a");
    }
    catch (const std::regex_error& e)
    {
        std::cout << "regex_error caught: " << e.what() << '\n';
        if (e.code() == std::regex_constants::error_brack)
            std::cout << "The code was error_brack\n";
    }
}
```


**Output:**
```
regex_error caught: The expression contained mismatched [ and ].
The code was error_brack
```

