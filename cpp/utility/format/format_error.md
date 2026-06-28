---
title: std::format_error
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/format_error
---

ddcl|header=format|since=c++20|1=
class format_error;
Defines the type of exception object thrown to report errors in the formatting library.

## Member functions


## Example


### Example

```cpp
#include <format>
#include <print>
#include <string_view>
#include <utility>

int main()
{
    try
    {
        auto x13{37};
        auto args{std::make_format_args(x13)};
        std::ignore = std::vformat("{:()}", args); // throws
    }
    catch(const std::format_error& ex)
    {
        std::println("{}", ex.what());
    }
}
```


**Output:**
```
format error: failed to parse format-spec
```


## See also

