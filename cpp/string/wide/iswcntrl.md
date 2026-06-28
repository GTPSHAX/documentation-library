---
title: std::iswcntrl
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswcntrl
---

ddcl|header=cwctype|
int iswcntrl( std::wint_t ch );
Checks if the given wide character is a control character, i.e. codes `0x00-0x1F` and `0x7F` and any control characters specific to the current locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a control character, zero otherwise.

## Notes

ISO 30112 defines POSIX control characters as Unicode characters U+0000..U+001F, U+007F..U+009F, U+2028, and U+2029 (Unicode classes Cc, Zl, and Zp).

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u2028'; // the Unicode character "line separator" 

    std::cout << std::hex << std::showbase << std::boolalpha;
    std::cout << "in the default locale, iswcntrl(" << (std::wint_t)c << ") = "
              << (bool)std::iswcntrl(c) << '\n';
    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswcntrl(" << (std::wint_t)c << ") = "
              << (bool)std::iswcntrl(c) << '\n';
}
```


**Output:**
```
in the default locale, iswcntrl(0x2028) = false
in Unicode locale, iswcntrl(0x2028) = true
```


## See also


| cpp/locale/dsc iscntrl | (see dedicated page) |
| cpp/string/byte/dsc iscntrl | (see dedicated page) |

