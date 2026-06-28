---
title: std::print
type: Input/output
source: https://en.cppreference.com/w/cpp/io/print
---


```cpp
**Header:** `<`print`>`
dcl|num=1|since=c++23|
template< class... Args >
void print( std::format_string<Args...> fmt, Args&&... args );
dcl|num=2|since=c++23|
template< class... Args >
void print( std::FILE* stream,
std::format_string<Args...> fmt, Args&&... args );
```

Format `args` according to the format string `fmt`, and print the result to an output stream.
1. Equivalent to `std::print(stdout, fmt, std::forward<Args>(args)...)`.

```cpp
(std::enable_nonlocking_formatter_optimization<std::remove_cvref_t<Args>> && ...)
    ? std::vprint_unicode(stream, fmt.str, std::make_format_args(args...))
    : std::vprint_unicode_buffered(stream, fmt.str, std::make_format_args(args...));
```


```cpp
(std::enable_nonlocking_formatter_optimization<std::remove_cvref_t<Args>> && ...)
    ? std::vprint_nonunicode(stream, fmt.str, std::make_format_args(args...))
    : std::vprint_nonunicode_buffered(stream, fmt.str, std::make_format_args(args...));
```

If `std::formatter<Ti, char>` does not meet the *BasicFormatter* requirements for any `Ti` in `Args` (as required by `std::make_format_args`), the behavior is undefined.

## Parameters


### Parameters

- `stream` - output file stream to write to
- `fmt` - 
- `args...` - arguments to be formatted

## Exceptions


## Notes


## Example


### Example

```cpp
#include <cstdio>
#include <filesystem>
#include <print>

int main()
{
    std::print("{2} {1}{0}!\n", 23, "C++", "Hello");  // overload (1)

    const auto tmp{std::filesystem::temp_directory_path() / "test.txt"};
    if (std::FILE* stream{std::fopen(tmp.c_str(), "w")})
    {
        std::print(stream, "File: {}", tmp.string()); // overload (2)
        std::fclose(stream);
    }
}
```


**Output:**
```
Hello C++23!
```


## Defect reports


## See also


| cpp/io/dsc println | (see dedicated page) |
| cpp/io/basic_ostream/dsc print | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/utility/format/dsc format_to | (see dedicated page) |
| cpp/io/c/dsc fprintf | (see dedicated page) |

