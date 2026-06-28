---
title: std::format_to
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/format_to
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class OutputIt, class... Args >
OutputIt format_to( OutputIt out,
std::format_string<Args...> fmt, Args&&... args );
dcl|num=2|since=c++20|1=
template< class OutputIt, class... Args >
OutputIt format_to( OutputIt out,
std::wformat_string<Args...> fmt, Args&&... args );
dcl|num=3|since=c++20|1=
template< class OutputIt, class... Args >
OutputIt format_to( OutputIt out, const std::locale& loc,
std::format_string<Args...> fmt, Args&&... args );
dcl|num=4|since=c++20|1=
template< class OutputIt, class... Args >
OutputIt format_to( OutputIt out, const std::locale& loc,
std::wformat_string<Args...> fmt, Args&&... args );
```

Format `args` according to the format string `fmt`, and write the result to the output iterator `out`. If present, `loc` is used for locale-specific formatting.
Equivalent to:
1. `return std::vformat_to(std::move(out), fmt.str, std::make_format_args(args...));`
2. `return std::vformat_to(std::move(out), fmt.str, std::make_wformat_args(args...));`
3. `return std::vformat_to(std::move(out), loc, fmt.str, std::make_format_args(args...));`
4. `return std::vformat_to(std::move(out), loc, fmt.str, std::make_wformat_args(args...));`.
Let `CharT` be `char` for overloads , `wchar_t` for overloads .
If any of the following conditions is satisfied, the behavior is undefined:
* `OutputIt` does not model `std::output_iterator<const CharT&>`.
* `std::formatter<Ti, CharT>` does not meet the *BasicFormatter* requirements (as required by `std::make_format_args` and `std::make_wformat_args`) for some `Ti` in `Args`.

## Parameters


### Parameters

- `out` - iterator to the output buffer
- `fmt` - 
- `args...` - arguments to be formatted
- `loc` - `std::locale` used for locale-specific formatting

## Return value

Iterator past the end of the output range.

## Exceptions

Propagates any exception thrown by formatter or iterator operations.

## Notes

As of `P2216R3`, it is an error if the format string is not a constant expression. `std::vformat_to` <sup>(since C++26)</sup> or `std::runtime_format` can be used in this case.

## Example


### Example

```cpp
#include <format>
#include <iostream>
#include <iterator>
#include <string>

int main()
{
    std::string buffer;

    std::format_to
    (
        std::back_inserter(buffer), // < OutputIt
        "Hello, C++{}!\n",          // < fmt
        "20"                        // < arg
    );
    std::cout << buffer;
    buffer.clear();

    std::format_to
    (
        std::back_inserter(buffer), // < OutputIt
        "Hello, {0}::{1}!{2}",      // < fmt
        "std",                      // < arg {0}
        "format_to()",              // < arg {1}
        "\n",                       // < arg {2}
        "extra param(s)..."         // < unused
    );
    std::cout << buffer << std::flush;

    std::wstring wbuffer;
    std::format_to
    (
        std::back_inserter(wbuffer),// < OutputIt
        L"Hello, {2}::{1}!{0}",     // < fmt
        L"\n",                      // < arg {0}
        L"format_to()",             // < arg {1}
        L"std",                     // < arg {2}
        L"...is not..."             // < unused
        L"...an error!"             // < unused
    );
    std::wcout << wbuffer;
}
```


**Output:**
```
Hello, C++20!
Hello, std::format_to()!
Hello, std::format_to()!
```


## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/utility/format/dsc format_to_n | (see dedicated page) |

