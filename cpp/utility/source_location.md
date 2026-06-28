---
title: std::source_location
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/source_location
---


```cpp
**Header:** `<`source_location`>`
dcl|since=c++20|
struct source_location;
```

The `std::source_location` class represents certain information about the source code, such as file names, line numbers, and function names. Previously, functions that desire to obtain this information about the call site (for logging, testing, or debugging purposes) must use macros so that predefined macros like `__LINE__` and `__FILE__` are expanded in the context of the caller. The `std::source_location` class provides a better alternative.
`std::source_location` meets the *DefaultConstructible*, *CopyConstructible*, *CopyAssignable*, *Destructible* and *Swappable* requirements.
Additionally, the following conditions are `true`:
* `std::is_nothrow_move_constructible_v<std::source_location>`,
* `std::is_nothrow_move_assignable_v<std::source_location>`, and
* `std::is_nothrow_swappable_v<std::source_location>`.
It is intended that `std::source_location` has a small size and can be copied efficiently.
It is unspecified whether the copy/move constructors and the copy/move assignment operators of `std::source_location` are trivial and/or constexpr.

## Member functions


#### Creation

| cpp/utility/source_location/dsc constructor | (see dedicated page) |
| cpp/utility/source_location/dsc current | (see dedicated page) |

#### Field access

| cpp/utility/source_location/dsc line | (see dedicated page) |
| cpp/utility/source_location/dsc column | (see dedicated page) |
| cpp/utility/source_location/dsc file_name | (see dedicated page) |
| cpp/utility/source_location/dsc function_name | (see dedicated page) |


## Notes


## Example


### Example

```cpp
#include <iostream>
#include <source_location>
#include <string_view>

void log(const std::string_view message,
         const std::source_location location =
               std::source_location::current())
{
    std::clog << "file: "
              << location.file_name() << '('
              << location.line() << ':'
              << location.column() << ") `"
              << location.function_name() << "`: "
              << message << '\n';
}

template<typename T>
void fun(T x)
{
    log(x); // line 20
}

int main(int, char*[])
{
    log("Hello world!"); // line 25
    fun("Hello C++20!");
}
```


**Output:**
```
file: main.cpp(25:8) `int main(int, char**)`: Hello world!
file: main.cpp(20:8) `void fun(T) [with T = const char*]`: Hello C++20!
```


## See also


| cpp/preprocessor/dsc line | (see dedicated page) |
| cpp/utility/dsc stacktrace_entry | (see dedicated page) |

