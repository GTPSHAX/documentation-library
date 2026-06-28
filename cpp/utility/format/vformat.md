---
title: std::vformat
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/vformat
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
std::string vformat( std::string_view fmt, std::format_args args );
dcl|num=2|since=c++20|1=
std::wstring vformat( std::wstring_view fmt, std::wformat_args args );
dcl|num=3|since=c++20|1=
std::string vformat( const std::locale& loc,
std::string_view fmt, std::format_args args );
dcl|num=4|since=c++20|1=
std::wstring vformat( const std::locale& loc,
std::wstring_view fmt, std::wformat_args args );
```

Format arguments held by `args` according to the format string `fmt`, and return the result as a string. If present, `loc` is used for locale-specific formatting.

## Parameters


### Parameters

- `fmt` - 
- `args` - arguments to be formatted
- `loc` - `std::locale` used for locale-specific formatting

## Return value

A string object holding the formatted result.

## Exceptions

Throws `std::format_error` if `fmt` is not a valid format string for the provided arguments, or `std::bad_alloc` on allocation failure. Also propagates any exception thrown by formatter or iterator operations.

## Example


### Example

```cpp
#include <format>
#include <iostream>

template<typename... Args>
inline void println(const std::format_string<Args...> fmt, Args&&... args)
{
    std::cout << std::vformat(fmt.get(), std::make_format_args(args...)) << '\n';
}

int main()
{
    println("{}{} {}{}", "Hello", ',', "C++", -1 + 2 * 3 * 4);
}
```


**Output:**
```
Hello, C++23
```


## See also

