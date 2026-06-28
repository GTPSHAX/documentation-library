---
title: std::formatter
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/formatter
---

ddcl|header=format|since=c++20|1=
template< class T, class CharT = char >
struct formatter;
The enabled specializations of `std::formatter` define formatting rules for a given type. Enabled specializations meet the *BasicFormatter* requirements, and, unless otherwise specified, also meet the *Formatter* requirements.
For all types `T` and `CharT` for which no specialization `std::formatter<T, CharT>` is enabled, that specialization is a complete type and is disabled.
Disabled specializations do not meet the *Formatter* requirements, and the following are all `false`:
* `std::is_default_constructible_v`
* `std::is_copy_constructible_v`
* `std::is_move_constructible_v`
* `std::is_copy_assignable_v`
* `std::is_move_assignable_v`.

## Basic standard specializations

In the following list, `CharT` is either `char` or `wchar_t`, `ArithmeticT` is any cv-unqualified arithmetic type other than `char`, `wchar_t`, `char8_t`, `char16_t`, or `char32_t`:

```cpp
dcl|num=1|1=
template<>
struct formatter<char, char>;
dcl|num=2|1=
template<>
struct formatter<char, wchar_t>;
dcl|num=3|1=
template<>
struct formatter<wchar_t, wchar_t>;
dcl|num=4|1=
template<>
struct formatter<CharT*, CharT>;
dcl|num=5|1=
template<>
struct formatter<const CharT*, CharT>;
dcl|num=6|1=
template< std::size_t N >
struct formatter<CharT[N], CharT>;
dcl|num=7|1=
template< class Traits, class Alloc >
struct formatter<std::basic_string<CharT, Traits, Alloc>, CharT>;
dcl|num=8|1=
template< class Traits >
struct formatter<std::basic_string_view<CharT, Traits>, CharT>;
dcl|num=9|1=
template<>
struct formatter<ArithmeticT, CharT>;
dcl|num=10|1=
template<>
struct formatter<std::nullptr_t, CharT>;
dcl|num=11|1=
template<>
struct formatter<void*, CharT>;
dcl|num=12|1=
template<>
struct formatter<const void*, CharT>;
```

Formatters for other pointers and pointers to members are disabled.
Specializations such as `std::formatter<wchar_t, char>` and `std::formatter<const char*, wchar_t>` that would require encoding conversions are disabled.
rrev|since=c++23|
The following specialization are still disabled in C++23 to avoid formatting some `char` sequences as ranges of `wchar_t`:

```cpp
dcl|num=1|
template<>
struct formatter<char*, wchar_t>;
dcl|num=2|
template<>
struct formatter<const char*, wchar_t>;
dcl|num=3|
template< std::size_t N >
struct formatter<char[N], wchar_t>;
dcl|num=4|
template< class Traits, class Allocator >
struct formatter<std::basic_string<char, Traits, Allocator>, wchar_t>;
dcl|num=5|
template< class Traits >
struct formatter<std::basic_string_view<char, Traits>, wchar_t>;
```

A ''debug-enabled'' formatter specialization additionally provides a public non-static member function `constexpr void set_debug_format();` which modifies the state of the formatter object so that it will format the values as escaped and quoted, as if the *type* of the format specifier parsed by the last call to `parse` were **`?`**.
Each formatter specialization for string or character type is ''debug-enabled''.

## Standard format specification

> **TODO:** The standard format specification is moved to a separate `page`. The section title is temporarily preserved for links to this section. This section will be removed after all those links are settled.

## Standard specializations for library types


| cpp/chrono/dsc formatter|duration | (see dedicated page) |
| cpp/chrono/dsc formatter|sys_time|system_clock | (see dedicated page) |
| cpp/chrono/dsc formatter|utc_time|utc_clock | (see dedicated page) |
| cpp/chrono/dsc formatter|tai_time|tai_clock | (see dedicated page) |
| cpp/chrono/dsc formatter|gps_time|gps_clock | (see dedicated page) |
| cpp/chrono/dsc formatter|file_time|file_clock | (see dedicated page) |
| cpp/chrono/dsc formatter|local_time|local_t | (see dedicated page) |
| cpp/chrono/dsc formatter|day | (see dedicated page) |
| cpp/chrono/dsc formatter|month | (see dedicated page) |
| cpp/chrono/dsc formatter|year | (see dedicated page) |
| cpp/chrono/dsc formatter|weekday | (see dedicated page) |
| cpp/chrono/dsc formatter|weekday_indexed | (see dedicated page) |
| cpp/chrono/dsc formatter|weekday_last | (see dedicated page) |
| cpp/chrono/dsc formatter|month_day | (see dedicated page) |
| cpp/chrono/dsc formatter|month_day_last | (see dedicated page) |
| cpp/chrono/dsc formatter|month_weekday | (see dedicated page) |
| cpp/chrono/dsc formatter|month_weekday_last | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month_day | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month_day_last | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month_weekday | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month_weekday_last | (see dedicated page) |
| cpp/chrono/dsc formatter|hh_mm_ss | (see dedicated page) |
| cpp/chrono/dsc formatter|sys_info | (see dedicated page) |
| cpp/chrono/dsc formatter|local_info | (see dedicated page) |
| cpp/chrono/dsc formatter|zoned_time | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc formatter | (see dedicated page) |
| cpp/utility/stacktrace_entry/dsc formatter | (see dedicated page) |
| cpp/thread/thread/id/dsc formatter | (see dedicated page) |
| cpp/container/vector_bool/reference/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc tuple_formatter | (see dedicated page) |
| cpp/utility/format/dsc ranges_formatter | (see dedicated page) |
| cpp/container/dsc adaptor_formatter|stack | (see dedicated page) |
| cpp/container/dsc adaptor_formatter|queue | (see dedicated page) |
| cpp/container/dsc adaptor_formatter|priority_queue | (see dedicated page) |
| cpp/filesystem/path/dsc formatter | (see dedicated page) |


## Example


### Example

```cpp
#include <algorithm>
#include <format>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string_view>

struct QuotableString : std::string_view
{};

template<>
struct std::formatter<QuotableString, char>
{
    bool quoted = false;

    template<class ParseContext>
    constexpr ParseContext::iterator parse(ParseContext& ctx)
    {
        auto it = ctx.begin();
        if (it == ctx.end())
            return it;

        if (*it == '#')
        {
            quoted = true;
            ++it;
        }
        if (it != ctx.end() && *it != '}')
            throw std::format_error("Invalid format args for QuotableString.");

        return it;
    }

    template<class FmtContext>
    FmtContext::iterator format(QuotableString s, FmtContext& ctx) const
    {
        std::ostringstream out;
        if (quoted)
            out << std::quoted(s);
        else
            out << s;

        return std::ranges::copy(std::move(out).str(), ctx.out()).out;
    }
};

int main()
{
    QuotableString a("be"), a2(R"( " be " )");
    QuotableString b("a question");
    std::cout << std::format("To {0} or not to {0}, that is {1}.\n", a, b);
    std::cout << std::format("To {0:} or not to {0:}, that is {1:}.\n", a, b);
    std::cout << std::format("To {0:#} or not to {0:#}, that is {1:#}.\n", a2, b);
}
```


**Output:**
```
To be or not to be, that is a question.
To be or not to be, that is a question.
To " \" be \" " or not to " \" be \" ", that is "a question".
```


## Defect reports


## See also


| cpp/utility/format/dsc basic_format_context | (see dedicated page) |
| cpp/utility/format/dsc formattable | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |

