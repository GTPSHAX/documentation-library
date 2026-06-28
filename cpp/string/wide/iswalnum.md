---
title: std::iswalnum
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswalnum
---

ddcl|header=cwctype|
int iswalnum( std::wint_t ch );
Checks if the given wide character is an alphanumeric character, i.e. either a number (`0123456789`), an uppercase letter (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`), a lowercase letter (`abcdefghijklmnopqrstuvwxyz`) or any alphanumeric character specific to the current locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is an alphanumeric character, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are included in the POSIX alnum category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u13ad'; // the Cherokee letter HA ('Ꭽ')

    std::cout << std::hex << std::showbase << std::boolalpha;
    std::cout << "in the default locale, iswalnum(" << (std::wint_t)c << ") = "
              << (bool)std::iswalnum(c) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswalnum(" << (std::wint_t)c << ") = "
              << (bool)std::iswalnum(c) << '\n';
}
```


**Output:**
```
in the default locale, iswalnum(0x13ad) = false
in Unicode locale, iswalnum(0x13ad) = true
```


## See also


| cpp/locale/dsc isalnum | (see dedicated page) |
| cpp/string/byte/dsc isalnum | (see dedicated page) |

