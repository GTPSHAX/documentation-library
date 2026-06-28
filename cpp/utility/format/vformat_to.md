---
title: std::vformat_to
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/vformat_to
---


```cpp
**Header:** `<`format`>`
dcl|num=1|since=c++20|1=
template< class OutputIt >
OutputIt vformat_to( OutputIt out, std::string_view fmt, std::format_args args );
dcl|num=2|since=c++20|1=
template< class OutputIt >
OutputIt vformat_to( OutputIt out, std::wstring_view fmt, std::wformat_args args );
dcl|num=3|since=c++20|1=
template< class OutputIt >
OutputIt vformat_to( OutputIt out, const std::locale& loc,
std::string_view fmt, std::format_args args );
dcl|num=4|since=c++20|1=
template< class OutputIt >
OutputIt vformat_to( OutputIt out, const std::locale& loc,
std::wstring_view fmt, std::wformat_args args );
```

Format arguments held by `args` according to the format string `fmt`, and write the result to the output iterator `out`. If present, `loc` is used for locale-specific formatting.
Let `CharT` be `decltype(fmt)::char_type` (`char` for overloads , `wchar_t` for overloads ).
cpp/enable if|plural=true|
`OutputIt` satisfies the concept `std::output_iterator<const CharT&>`.
cpp/precondition|
`OutputIt` must model (meet the semantic requirements of) the concept `std::output_iterator<const CharT&>`, and `std::formatter<Ti, CharT>` must meet the *Formatter* requirements for any `Ti` in the type of arguments.

## Parameters


### Parameters

- `out` - iterator to the output buffer
- `fmt` - 
- `args` - arguments to be formatted
- `loc` - `std::locale` used for locale-specific formatting

## Return value

Iterator past the end of the output range.

## Exceptions

Throws `std::format_error` if `fmt` is not a valid format string for the provided arguments. Also propagates any exception thrown by formatter or iterator operations.

## Example


## Defect reports


## See also

