---
title: std::iswupper
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswupper
---

ddcl|header=cwctype|
int iswupper( std::wint_t ch );
Checks if the given wide character is an uppercase letter, i.e. one of `ABCDEFGHIJKLMNOPQRSTUVWXYZ` or any uppercase letter specific to the current locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character is an uppercase letter, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are include in POSIX upper category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    const wchar_t c = L'\u053d'; // Armenian capital letter xeh ('Խ')

    std::cout << std::hex << std::showbase << std::boolalpha;
    std::cout << "in the default locale, iswupper("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswupper(c)) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswupper("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswupper(c)) << '\n';
}
```


**Output:**
```
in the default locale, iswupper(0x53d) = false
in Unicode locale, iswupper(0x53d) = true
```


## See also


| cpp/locale/dsc isupper | (see dedicated page) |
| cpp/string/byte/dsc isupper | (see dedicated page) |

