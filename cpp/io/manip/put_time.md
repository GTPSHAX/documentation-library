---
title: std::put_time
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/put_time
---

ddcl|header=iomanip|since=c++11|
template< class CharT >
/*unspecified*/ put_time( const std::tm* tmb, const CharT* fmt );
When used in an expression `out << put_time(tmb, fmt)`, converts the date and time information from a given calendar time `tmb` to a character string according to format string `fmt`, as if by calling `std::strftime`, `std::wcsftime`, or analog (depending on `CharT`), according to the `std::time_put` facet of the locale currently imbued in the output stream `out`.

## Parameters


### Parameters

- `tmb` - pointer to the calendar time structure as obtained from `std::localtime` or `std::gmtime`
- `fmt` - pointer to a null-terminated `CharT` string specifying the format of conversion

## Format string


## Return value


## Example


### Example

```cpp
#include <ctime>
#include <iomanip>
#include <iostream>

int main()
{
    std::time_t t = std::time(nullptr);
    std::tm tm = *std::localtime(&t);

    std::cout.imbue(std::locale("ru_RU.utf8"));
    std::cout << "ru_RU: " << std::put_time(&tm, "%c %Z") << '\n';

    std::cout.imbue(std::locale("ja_JP.utf8"));
    std::cout << "ja_JP: " << std::put_time(&tm, "%c %Z") << '\n';
}
```


**Output:**
```
ru_RU: Ср. 28 дек. 2011 10:21:16 EST
ja_JP: 2011年12月28日 10時21分16秒 EST
```


## See also


| cpp/locale/dsc time_put | (see dedicated page) |
| cpp/io/manip/dsc get_time | (see dedicated page) |
| cpp/chrono/c/dsc strftime | (see dedicated page) |
| cpp/chrono/c/dsc wcsftime | (see dedicated page) |

