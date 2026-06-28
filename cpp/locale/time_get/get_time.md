---
title: std::time_get::get_time
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_get/get_time
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
iter_type get_time( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm* t ) const;
dcl|num=2|1=
protected:
virtual iter_type do_get_time( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm* t ) const;
```

1. Public member function, calls the protected virtual member function `do_get_time` of the most derived class.
2. Reads successive characters from the sequence [beg, end) and parses out the time value following the same rules as the format specifier `"%H:%M:%S"` as used by the functions `std::get_time`, , and the POSIX function `strptime()`.
:: The parsed time is stored in the corresponding fields of the `std::tm` structure pointed to by the argument `t`.
:: If the end iterator is reached before a valid time is read, the function sets `std::ios_base::eofbit` in `err`. If a parsing error is encountered, the function sets `std::ios_base::failbit` in `err`.

## Parameters


### Parameters

- `beg` - iterator designating the start of the sequence to parse
- `end` - one past the end iterator for the sequence to parse
- `str` - a stream object that this function uses to obtain locale facets when needed, e.g. `std::ctype` to skip whitespace
- `err` - stream error flags object that is modified by this function to indicate errors
- `t` - pointer to the `std::tm` object that will hold the result of this function call

## Return value

Iterator pointing one past the last character in [beg, end) that was recognized as a part of a valid date.

## Notes

For the alphabetic components of the default time format (if any), this function is usually case-insensitive.
If a parsing error is encountered, most implementations of this function leave `*t` unmodified.

## Example


### Example

```cpp
#include <iostream>
#include <iterator>
#include <locale>
#include <sstream>

void try_get_time(const std::string& s)
{
    std::cout << "Parsing the time out of '" << s
              << "' in the locale " << std::locale().name() << '\n';
    std::istringstream str(s);
    std::ios_base::iostate err = std::ios_base::goodbit;

    std::tm t;
    std::time_get<char> const& facet =
        std::use_facet<std::time_get<char>>(str.getloc());
    std::istreambuf_iterator<char> ret =
        facet.get_time({str}, {}, str, err, &t);
    str.setstate(err);

    if (str)
    {
        std::cout << "Hours: " << t.tm_hour << ", "
                     "Minutes: " << t.tm_min  << ", "
                     "Seconds: " << t.tm_sec  << '\n';
    }
    else
    {
        std::cout << "Parse failed. Unparsed string: ";
        std::copy(ret, {}, std::ostreambuf_iterator<char>(std::cout));
        std::cout << '\n';
    }
}

int main()
{
    std::locale::global(std::locale("ru_RU.utf8"));
    try_get_time("21:40:11");
    try_get_time("21-40-11");

    std::locale::global(std::locale("ja_JP.utf8"));
    try_get_time("21時37分58秒");
}
```


**Output:**
```
Parsing the time out of '21:40:11' in the locale ru_RU.utf8
Hours: 21, Minutes: 40, Seconds: 11
Parsing the time out of '21-40-11' in the locale ru_RU.utf8
Parse failed. Unparsed string: -40-11
Parsing the time out of '21時37分58秒' in the locale ja_JP.utf8
Hours: 21, Minutes: 37, Seconds: 58
```


## Defect reports


## See also


| cpp/io/manip/dsc get_time | (see dedicated page) |

