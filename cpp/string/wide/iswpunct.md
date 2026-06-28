---
title: std::iswpunct
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswpunct
---

ddcl|header=cwctype|
int iswpunct( std::wint_t ch );
Checks if the given wide character is a punctuation character, i.e. it is one of } or any punctuation character specific to the current locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a punctuation character, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are include in POSIX punct category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u2051'; // Two asterisks ('⁑')

    std::cout << std::hex << std::showbase << std::boolalpha
              << "in the default locale, iswpunct("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswpunct(c)) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswpunct("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswpunct(c)) << '\n';
}
```


**Output:**
```
in the default locale, iswpunct(0x2051) = false
in Unicode locale, iswpunct(0x2051) = true
```


## See also


| cpp/locale/dsc ispunct | (see dedicated page) |
| cpp/string/byte/dsc ispunct | (see dedicated page) |

