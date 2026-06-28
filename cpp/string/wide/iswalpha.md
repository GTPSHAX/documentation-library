---
title: std::iswalpha
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswalpha
---

ddcl|header=cwctype|
int iswalpha( std::wint_t ch );
Checks if the given wide character is an alphabetic character, i.e. either an uppercase letter (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`), a lowercase letter (`abcdefghijklmnopqrstuvwxyz`) or any alphabetic character specific to the current locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is an alphabetic character, `0` otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are include in POSIX alpha category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u0b83'; // Tamil sign Visarga ('ஃ')

    std::cout << std::hex << std::showbase << std::boolalpha;
    std::cout << "in the default locale, iswalpha(" << (std::wint_t)c << ") = "
              << (bool)std::iswalpha(c) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswalpha(" << (std::wint_t)c << ") = "
              << (bool)std::iswalpha(c) << '\n';
}
```


**Output:**
```
in the default locale, iswalpha(0xb83) = false
in Unicode locale, iswalpha(0xb83) = true
```


## See also


| cpp/locale/dsc isalpha | (see dedicated page) |
| cpp/string/byte/dsc isalpha | (see dedicated page) |

