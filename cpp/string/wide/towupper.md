---
title: std::towupper
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/towupper
---

ddcl|header=cwctype|
std::wint_t towupper( std::wint_t ch );
Converts the given wide character to uppercase, if possible.

## Parameters


### Parameters

- `ch` - wide character to be converted

## Return value

Uppercase version of `ch` or unmodified `ch` if no uppercase version is listed in the current C locale.

## Notes

Only 1:1 character mapping can be performed by this function, e.g. the uppercase form of `'ß'` is (with some exceptions) the two-character string `"SS"`, which cannot be obtained by `std::towupper`.
[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which pairs of Unicode characters are included in this mapping.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

int main()
{
    wchar_t c = L'\u017f'; // Latin small letter Long S ('ſ')

    std::cout << std::hex << std::showbase;
    std::cout << "in the default locale, towupper("
              << static_cast<std::wint_t>(c) << ") = "
              << std::towupper(c) << '\n';

    std::setlocale(LC_ALL, "en_US.utf8");
    std::cout << "in Unicode locale, towupper("
              << static_cast<std::wint_t>(c) << ") = "
              << std::towupper(c) << '\n';
}
```


**Output:**
```
in the default locale, towupper(0x17f) = 0x17f
in Unicode locale, towupper(0x17f) = 0x53
```


## See also


| cpp/string/wide/dsc towlower | (see dedicated page) |
| cpp/locale/dsc toupper | (see dedicated page) |
| cpp/string/byte/dsc toupper | (see dedicated page) |

