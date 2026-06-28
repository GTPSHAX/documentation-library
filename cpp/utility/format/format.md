---
title: std::format
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/format
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class... Args >
std::string format( std::format_string<Args...> fmt, Args&&... args );
dcl|num=2|since=c++20|1=
template< class... Args >
std::wstring format( std::wformat_string<Args...> fmt, Args&&... args );
dcl|num=3|since=c++20|1=
template< class... Args >
std::string format( const std::locale& loc,
std::format_string<Args...> fmt, Args&&... args );
dcl|num=4|since=c++20|1=
template< class... Args >
std::wstring format( const std::locale& loc,
std::wformat_string<Args...> fmt, Args&&... args );
```

Format `args` according to the format string `fmt`, and return the result as a string. If present, `loc` is used for locale-specific formatting.
1. Equivalent to `return std::vformat(fmt.get(), std::make_format_args(args...));`.
2. Equivalent to `return std::vformat(fmt.get(), std::make_wformat_args(args...));`.
3. Equivalent to `return std::vformat(loc, fmt.get(), std::make_format_args(args...));`.
4. Equivalent to `return std::vformat(loc, fmt.get(), std::make_wformat_args(args...));`.
Since `P2216R3`, `std::format` does a compile-time check on the format string (via the helper type `std::format_string` or `std::wformat_string`). If it is found to be invalid for the types of the arguments to be formatted, a compilation error will be emitted. If the format string cannot be a compile-time constant, or the compile-time check needs to be avoided, use `std::vformat` <sup>(since C++26)</sup> or `std::dynamic_format on `fmt`` instead.
The following requirements apply to each type `T` in `Args`, where `CharT` is `char` for overloads , `wchar_t` for overloads :
* `std::formatter<T, CharT>` must satisfy *BasicFormatter*
* `std::formatter<T, CharT>::parse()` must be `constexpr` since `P2216R3` (`std::vformat` does not have this requirement)

## Parameters


### Parameters

- `fmt` - 
- `args...` - arguments to be formatted
- `loc` - `std::locale` used for locale-specific formatting

## Return value

A string object holding the formatted result.

## Exceptions

Throws `std::bad_alloc` on allocation failure. Also propagates exception thrown by any formatter.

## Notes

It is not an error to provide more arguments than the format string requires:

```cpp
std::format("{} {}!", "Hello", "world", "something"); // OK, produces "Hello world!"
```

As of `P2216R3`, it is an error if the format string is not a constant expression. `std::vformat` can be used in this case.

```cpp
std::string f(std::string_view runtime_format_string)
{
    // return std::format(runtime_format_string, "foo", "bar"); // error
    return std::vformat(runtime_format_string, std::make_format_args("foo", "bar")); // OK
}
```

rrev|since=c++26|`std::dynamic_format` can be used directly on `std::format` instead of `std::vformat` which requires `std::basic_format_args` as an argument.

```cpp
std::string f(std::string_view runtime_format_string)
{
    return std::format(std::dynamic_format(runtime_format_string), "foo", "bar");
}
```


## Example


### Example

```cpp
#include <format>
#include <iostream>
#include <string>
#include <string_view>

template<typename... Args>
std::string dyna_print(std::string_view rt_fmt_str, Args&&... args)
{
    return std::vformat(rt_fmt_str, std::make_format_args(args...));
}

int main()
{
    std::cout << std::format("Hello {}!\n", "world");

    std::string fmt;
    for (int i{}; i != 3; ++i)
    {
        fmt += "{} "; // constructs the formatting string
        std::cout << fmt << " : ";
        std::cout << dyna_print(fmt, "alpha", 'Z', 3.14, "unused");
        std::cout << '\n';
    }
}
```


**Output:**
```
Hello world!
{}  : alpha
{} {}  : alpha Z
{} {} {}  : alpha Z 3.14
```


## Defect reports


## See also


| cpp/utility/format/dsc format_to | (see dedicated page) |
| cpp/utility/format/dsc format_to_n | (see dedicated page) |

