---
title: std::time_put::put
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_put/put
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
iter_type put( iter_type out, std::ios_base& str,
char_type fill, const std::tm* t,
const CharT* fmtbeg, const CharT* fmtend ) const;
dcl|num=2|1=
public:
iter_type put( iter_type out, std::ios_base& str,
char_type fill, const std::tm* t,
char format, char modifier = 0 ) const;
dcl|num=3|1=
protected:
virtual iter_type do_put( iter_type out, std::ios_base& str,
char_type fill, const std::tm* t,
char format, char modifier ) const;
```

Converts the calendar date and time stored in the `std::tm` object pointed to by `t` into a character string, according to the format string `[fmtbeg, fmtend)`. The format string is the same as used by `std::strftime`, but each format specifier is processed by an individual call to `do_put()`, which can be customized by extending this facet.
1. Steps through the character sequence `[fmtbeg, fmtend)`, examining the characters. Every character that is not a part of a format sequence is written to the output iterator `out` immediately. To identify format sequences, this function narrows the next character `c` in `[fmtbeg, fmtend)` as if by `std::ctype<char_type>(str.getloc()).narrow(c, 0)` and if it equals `'%'`, the next one or two characters are compared to the list of format sequences recognized by `std::strftime` plus any additional implementation-defined formats supported by this locale. For each valid format sequence, a call to `do_put(out, str, fill, t, format, modifier)` is made, where `format` is the format sequence character, and `modifier` is the optional format sequence modifier (`'E'` or `'O'`). A value of `'\0'` is used if the modifier is absent.
2. Calls the `do_put` member function of the most derived class.
3. Converts the calendar date and time stored in the `std::tm` object pointed to by `t` into a character string, according to the format conversion sequence formed by concatenating `'%'`, the value of `modifier` if not `'\0'`, and the value of `format`. The format is interpreted the same way as the function `std::strftime`, except that the formats that are described as locale-dependent are defined by this locale, and additional format specifiers may be supported (the `fill` argument is provided for these implementation-defined format specifiers to use). The string is written to the output iterator `out`.

## Parameters


### Parameters

- `out` - output iterator where the result of the conversion is written
- `str` - a stream object that this function uses to obtain locale facets when needed, e.g. `std::ctype` to narrow characters
- `t` - pointer to the `std::tm` object from which the date/time values are obtained
- `fmtbeg` - pointer to the first character of a sequence of `char_type` characters specifying the conversion format
- `fmtend` - pointer one past the last character of a sequence of `char_type` characters specifying the conversion format
- `fill` - fill character (usually space)
- `format` - the character that names a conversion specifier
- `modifier` - the optional modifier that may appear between `%` and the conversion specifier

## Format string


## Return value

Iterator pointing one past the last character that was produced.

## Notes

No error handling is provided.
The `fill` character is provided for those implementation-defined format specifiers and for the user-defined overrides of `do_put()` that use padding and filling logic. Such implementations typically make use of the formatting flags from `str`.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <iomanip>
#include <ctime>

void try_time_put(const std::tm* t, const std::string& fmt)
{
    std::cout.imbue(std::locale());
    std::cout << "In the locale '" << std::cout.getloc().name() << "' : '";

    std::use_facet<std::time_put<char>>(std::cout.getloc()).put(
        {std::cout}, std::cout, ' ', t, &fmt[0], &fmt[0] + fmt.size());

    std::cout << "'\n";
}

int main()
{
    std::time_t t = std::time(NULL);
    std::tm tm = *std::localtime(&t);

    std::string fmt = "%c";
    std::cout << "Using the format string '" << fmt
              << "' to format the time: " << std::ctime(&t) << '\n';

    std::locale::global(std::locale("de_DE.utf8"));
    try_time_put(&tm, fmt);

    std::locale::global(std::locale("el_GR.utf8"));
    try_time_put(&tm, fmt);

    std::locale::global(std::locale("ja_JP.utf8"));
    try_time_put(&tm, fmt);
}
```


**Output:**
```
Using the format string '%c' to format the time: Mon Feb 11 22:58:50 2013

In the locale 'de_DE.utf8' : 'Mo 11 Feb 2013 23:02:38 EST'
In the locale 'el_GR.utf8' : 'Δευ 11 Φεβ 2013 11:02:38 μμ EST'
In the locale 'ja_JP.utf8' : '2013年02月11日 23時02分38秒'
```


## Defect reports


## See also


| cpp/io/manip/dsc put_time | (see dedicated page) |
| cpp/locale/time_get/dsc do_get | (see dedicated page) |

