---
title: std::iswgraph
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswgraph
---

ddcl|header=cwctype|
int iswgraph( std::wint_t ch );
Checks if the given wide character has a graphical representation, i.e. it is either a number (`0123456789`), an uppercase letter (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`), a lowercase letter (`abcdefghijklmnopqrstuvwxyz`), a punctuation character (}) or any graphical character specific to the current C locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character has a graphical representation character, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are include in POSIX graph category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u2602'; // the Unicode character Umbrella ('☂')

    std::cout << std::hex << std::showbase << std::boolalpha
              << "in the default locale, iswgraph("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswgraph(c)) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, iswgraph("
              << static_cast<std::wint_t>(c) << ") = "
              << static_cast<bool>(std::iswgraph(c)) << '\n';
}
```


**Output:**
```
in the default locale, iswgraph(0x2602) = false
in Unicode locale, iswgraph(0x2602) = true
```


## See also


| cpp/locale/dsc isgraph | (see dedicated page) |
| cpp/string/byte/dsc isgraph | (see dedicated page) |

