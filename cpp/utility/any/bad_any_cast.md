---
title: std::bad_any_cast
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/any/bad_any_cast
---

ddcl | header=any | since=c++17 |
class bad_any_cast : public std::bad_cast;
Defines a type of object to be thrown by the value-returning forms of `std::any_cast` on failure.

## Member functions


## Example


### Example

```cpp
#include <any>
#include <cassert>
#include <print>

int main()
{
    auto x = std::any(42);
    assert(std::any_cast<int>(x) == 42); // OK

    try
    {
        [[maybe_unused]] auto s = std::any_cast<std::string>(x); // throws
    }
    catch (const std::bad_any_cast& ex)
    {
        std::println("{}", ex.what());
    }
}
```


**Output:**
```
bad any_cast
```

