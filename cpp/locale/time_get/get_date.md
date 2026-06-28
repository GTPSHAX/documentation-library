---
title: std::time_get::get_date
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_get/get_date
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
iter_type get_date( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm* t ) const;
dcl|num=2|1=
protected:
virtual iter_type do_get_date( iter_type beg, iter_type end, std::ios_base& str,
std::ios_base::iostate& err, std::tm* t ) const;
```

1. Public member function, calls the protected virtual member function `do_get_date` of the most derived class.
2. Reads successive characters from the sequence [beg, end) and parses out the calendar date value using the default format expected by this locale, which is determined as


| -style="text-align:center;" |
| lc | date_order() |
| Format |
| - |
| tt | no_order |
| c | "%m/%d/%y" |
| - |
| tt | dmy |
| c | "%d/%m/%y" |
| - |
| tt | mdy |
| c | "%m/%d/%y" |
| - |
| tt | ymd |
| c | "%y/%m/%d" |
| - |
| tt | ydm |
| c | "%y/%d/%m" |

@@ as used by the functions `std::get_time()`, `get()`, and the POSIX function `strptime()`.
@@ The parsed date is stored in the corresponding fields of the `std::tm` structure pointed to by the argument `t`.
@@ If the end iterator is reached before a valid date is read, the function sets `std::ios_base::eofbit` in `err`. If a parsing error is encountered, the function sets `std::ios_base::failbit` in `err`.

## Parameters


### Parameters

- `beg` - iterator designating the start of the sequence to parse
- `end` - one past the end iterator for the sequence to parse
- `str` - a stream object that this function uses to obtain locale facets when needed, e.g. `std::ctype` to skip whitespace or `std::collate` to compare strings
- `err` -  stream error flags object that is modified by this function to indicate errors
- `t` - pointer to the `std::tm` object that will hold the result of this function call

## Return value

Iterator pointing one past the last character in [beg, end) that was recognized as a part of a valid date.

## Notes

For the alphabetic components of the default date format (if any), this function is usually case-insensitive.
If a parsing error is encountered, most implementations of this function leave `*t` unmodified.
The implementation may support other date formats besides the ones required by the standard.

## Example


### Example

```cpp
#include <ctime>
#include <iostream>
#include <iterator>
#include <locale>
#include <sstream>

void try_get_date(const std::string& s)
{
    std::cout << "Parsing the date out of '" << s
              << "' in the locale " << std::locale().name() << '\n';
    std::istringstream str(s);
    std::ios_base::iostate err = std::ios_base::goodbit;

    std::tm t;
    const std::time_get<char>& facet = std::use_facet<std::time_get<char>>(str.getloc());
    std::istreambuf_iterator<char> ret = facet.get_date({str}, {}, str, err, &t);
    str.setstate(err);

    if (str)
    {
        std::cout << "Day: " << t.tm_mday << ' '
                  << "Month: " << t.tm_mon + 1 << ' '
                  << "Year: " << t.tm_year + 1900 << '\n';
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
    std::locale::global(std::locale("en_US.utf8"));
    try_get_date("02/01/2013");
    try_get_date("02-01-2013");

    std::locale::global(std::locale("ja_JP.utf8"));
    try_get_date("2013年02月01日");
}
```


**Output:**
```
Parsing the date out of '02/01/2013' in the locale en_US.utf8
Day: 1 Month: 2 Year: 2013
Parsing the date out of '02-01-2013' in the locale en_US.utf8
Parse failed. Unparsed string: -01-2013
Parsing the date out of '2013年02月01日' in the locale ja_JP.utf8
Day: 1 Month: 2 Year: 2013
```


## Defect reports


## See also


| cpp/io/manip/dsc get_time | (see dedicated page) |

