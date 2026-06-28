---
title: std::iswblank
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswblank
---

ddcl|header=cwctype|since=c++11|
int iswblank( std::wint_t ch );
Checks if the given wide character is classified as blank character (that is, a whitespace character used to separate words in a sentence) by the current C locale. In the default C locale, only space (`0x20`) and horizontal tab (`0x09`) are blank characters.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is a blank character, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] defines POSIX blank characters as Unicode characters U+0009, U+0020, U+1680, U+180E, U+2000..U+2006, U+2008, U+200A, U+205F, and U+3000.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u3000'; // Ideographic space ('　')

    std::cout << std::hex << std::showbase << std::boolalpha;
    std::cout << "in the default locale, iswblank(" << (std::wint_t)c << ") = "
              << (bool)std::iswblank(c) << '\n';
    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswblank(" << (std::wint_t)c << ") = "
              << (bool)std::iswblank(c) << '\n';
}
```


**Output:**
```
in the default locale, iswblank(0x3000) = false
in Unicode locale, iswblank(0x3000) = true
```


## See also


| cpp/locale/dsc isblank | (see dedicated page) |
| cpp/string/byte/dsc isblank | (see dedicated page) |

