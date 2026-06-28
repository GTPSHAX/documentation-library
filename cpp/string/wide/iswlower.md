---
title: std::iswlower
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswlower
---

ddcl|header=cwctype|
int iswlower( std::wint_t ch );
Checks if the given wide character is a lowercase letter, i.e. one of `abcdefghijklmnopqrstuvwxyz` or any lowercase letter specific to the current locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a lowercase letter, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are include in POSIX lower category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u0444'; // Cyrillic small letter ef ('ф')

    std::cout << std::hex << std::showbase << std::boolalpha
              << "in the default locale, iswlower("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswlower(c)) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswlower("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswlower(c)) << '\n';
}
```


**Output:**
```
in the default locale, iswlower(0x444) = false
in Unicode locale, iswlower(0x444) = true
```


## See also


| cpp/locale/dsc islower | (see dedicated page) |
| cpp/string/byte/dsc islower | (see dedicated page) |

