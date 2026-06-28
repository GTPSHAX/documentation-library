---
title: std::time_get::get
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_get/get
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|since=c++11|1=
public:
iter_type get( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm* t,
char format, char modifier = 0 ) const;
dcl|num=2|since=c++11|1=
public:
iter_type get( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm* t,
const char_type* fmtbeg, const char_type* fmtend ) const;
dcl|num=3|since=c++11|1=
protected:
virtual iter_type do_get( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm *t,
char format, char modifier ) const;
```

1. Public member function, calls the protected virtual member function `do_get` of the most derived class.
2. Parses the date and time from the input character sequence `[beg, end)` according to the format provided in the character sequence `[fmtbeg, fmtend)`. The format is expected to follow the format described below, although actual processing of each format specifier can be customized by overriding `do_get`. The `get` function performs the following:
First, clears the error bits in `err` by executing `1=err = std::ios_base::goodbit`. Then enters a loop, which terminates whenever any of the following conditions becomes true (checked in this order):
:@a@ All characters have been read from the format string (`fmtbeg ).
:@b@ There was a parsing error (`err !).
:@c@ All characters have been read from the input sequence (`beg . If this condition terminates the loop, the function sets both `eofbit` and `failbit` in `err`.
::In the body of the loop, the following steps take place:
:@a@ If the next character in the format string is `'%'`, followed by one or two characters that form a valid `std::get_time` conversion specifier (see below), these characters are used in the call `do_get(beg, end, str, err, t, format, modifier)`, where `format` is the primary conversion specifier character, and `modifier` is the optional modifier (which appears between `%` and the format character, if present). If there is no modifier, the value `'\0'` is used. If the format string is ambiguous or ends too early to determine the conversion specifier after `'%'`, `eofbit` is set in `err` and the loop is terminated. If, after the call to `do_get`, no error bits are set in `err`, the function increments `fmtbeg` to point right after the conversion specifier and continues the loop.
:@b@ If the next character is whitespace, as indicated by the locale provided in the stream `str` (i.e. `std::isspace(*fmtbeg, str.getloc()) , the function keeps incrementing `fmtbeg` until it either becomes equal to `fmtend` or points to a non-whitespace character.
:@c@ If the next character in the format string is equivalent to the next character in the input stream according to case-insensitive comparison, the function advances both sequences by one character `++fmtbeg, ++beg;` and continues the loop, Otherwise, it sets the `failbit` in `err`.
3. Parses one conversion specifier from the input sequence `[beg, end)` and updates the `std::tm` structure pointed to by `t` accordingly.
::First, clears the error bits in `err` by executing `1=err = std::ios_base::goodbit`. Then reads characters from the input sequence `[beg, end)` that are expected by the `std::time_get` format specifier formed by combining `'%'`, `modifier` (if not `'\0'`), and `format`. If the characters do not combine to form a valid conversion specifier, sets `failbit` in `err`. If the end of the input stream is reached after reading a character, sets `eofbit` in `err`. If the input string was parsed successfully, updates the corresponding fields of `*t`.
::For complex conversion specifiers, such as `'%x'` or `'%c'`, or the directives that use the modifiers `'E'` and `'O'`, the function may fail to determine some of the values to store in `*t`. In such case, it sets `eofbit` in `err` and leaves these fields in unspecified state.

## Parameters


### Parameters

- `beg` - iterator designating the start of the sequence to parse
- `end` - one past the end iterator for the sequence to parse
- `str` - a stream object that this function uses to obtain locale facets when needed, e.g. `std::ctype` to skip whitespace or `std::collate` to compare strings
- `err` - stream error flags object that is modified by this function to indicate errors
- `t` - pointer to the `std::tm` object that will hold the result of this function call
- `fmtbeg` - pointer to the first character of a sequence of `char_type` characters specifying the conversion format (see below)
- `fmtend` - pointer one past the last character of a sequence of `char_type` characters specifying the conversion format
- `format` - the character that names a conversion specifier
- `modifier` - the optional modifier that may appear between `%` and the conversion specifier
<br>

## Return value

Iterator pointing one past the last character in `[beg, end)` that was parsed successfully.

## Notes

The case-insensitive comparison for the non-whitespace non-`'%'` characters in the format string, the `std::collate` facet of the locale provided by `str` is typically, but not necessarily, used.
If a parsing error is encountered, many implementations of this function leave `*t` completely untouched.
It's unspecified if these functions zero out the fields in `*t` that they do not set directly: portable programs should initialize every field to zero before calling `get()`.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>
#include <sstream>

int main()
{
    std::istringstream ss("2026-März-12 23:45:56");
    ss.imbue(std::locale("de_DE.utf8"));

    auto& f = std::use_facet<std::time_get<char>>(ss.getloc());
    std::tm t{};
    std::string s = "%Y-%b-%d %H:%M:%S";
    std::ios_base::iostate err = std::ios_base::goodbit;
    auto ret = f.get({ss}, {}, ss, err, &t, &s[0], &s[0] + s.size());
    ss.setstate(err);
    std::istreambuf_iterator<char> last{};

    if (ss)
    {
        std::cout << "Successfully parsed as " << std::put_time(&t, "%c") << '\n';
        if (ret != last)
        {
            std::cout << "Remaining content: ";
            std::copy(ret, last, std::ostreambuf_iterator<char>(std::cout));
        }
        else
            std::cout << "The input was fully consumed.";
    }
    else
    {
        std::cout << "Parse failed.\nUnparsed string: ";
        std::copy(ret, last, std::ostreambuf_iterator<char>(std::cout));
    }
    std::cout << '\n';
}
```


**Output:**
```
Successfully parsed as Sun Mar 12 23:45:56 2026
The input was fully consumed.
```


## See also


| cpp/io/manip/dsc get_time | (see dedicated page) |

