---
title: println(std::ostream)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/println
---


# printlnsmall|(std::ostream)


```cpp
**Header:** `<`ostream`>`
dcla|num=1|since=c++23|
template< class... Args >
void println( std::ostream& os, std::format_string<Args...> fmt, Args&&... args );
dcla|num=2|since=c++26|
void println( std::ostream& os );
```

Formats `args` according to the format string `fmt` with appended `'\n'` (which means that each output ends with a new-line), and inserts the result into `os` stream.
1. Equivalent to:
box|`cpp/io/basic_ostream/print|std::print`}
2. Equivalent to:
The behavior is undefined if `std::formatter<Ti, char>` does not meet the *BasicFormatter* requirements for any `Ti` in `Args` (as required by `std::make_format_args`).

## Parameters


### Parameters

- `os` - output stream to insert data into
- `fmt` - 
- `args...` - arguments to be formatted

## Exceptions


## Notes

Although overload  is added in C++26, all known implementations make it available in C++23 mode.

## Example


## Defect reports


## See also


| cpp/io/basic_ostream/dsc print | (see dedicated page) |
| cpp/io/dsc println | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |

