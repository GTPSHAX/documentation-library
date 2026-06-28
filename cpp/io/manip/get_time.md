---
title: std::get_time
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/get_time
---

ddcl|header=iomanip|since=c++11|
template< class CharT >
/*unspecified*/ get_time( std::tm* tmb, const CharT* fmt );
When used in an expression `in >> get_time(tmb, fmt)`, parses the character input as a date/time value according to format string `fmt` according to the `std::time_get` facet of the locale currently imbued in the input stream `in`. The resultant value is stored in a `std::tm` object pointed to by `tmb`.

## Parameters


### Parameters

- `tmb` - valid pointer to the `std::tm` object where the result will be stored
- `fmt` - pointer to a null-terminated `CharT` string specifying the conversion format

## Return value


## Notes

As specified in `std::time_get::do_get`, which this function calls, it's unspecified if this function zero out the fields in `*tmb` that are not set directly by the conversion specifiers that appear in `fmt`: portable programs should initialize every field of `*tmb` to zero before calling `std::get_time`.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>
#include <sstream>

int main()
{
    std::tm t = {};
    std::istringstream ss("2011-Februar-18 23:12:34");
    ss.imbue(std::locale("de_DE.utf-8"));
    ss >> std::get_time(&t, "%Y-%b-%d %H:%M:%S");

    if (ss.fail())
        std::cout << "Parse failed\n";
    else
        std::cout << std::put_time(&t, "%c") << '\n';
}
```


**Output:**
```
Sun Feb 18 23:12:34 2011
```


## See also


| cpp/locale/dsc time_get | (see dedicated page) |
| cpp/io/manip/dsc put_time | (see dedicated page) |
| cpp/chrono/dsc parse | (see dedicated page) |

