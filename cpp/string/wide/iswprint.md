---
title: std::iswprint
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/iswprint
---

ddcl|header=cwctype|
int iswprint( std::wint_t ch );
Checks if the given wide character can be printed, i.e. it is either a number (`0123456789`), an uppercase letter (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`), a lowercase letter (`abcdefghijklmnopqrstuvwxyz`), a punctuation character (}), space or any printable character specific to the current C locale.

## Parameters


### Parameters

- `ch` - wide character

## Return value

Non-zero value if the wide character can be printed, zero otherwise.

## Notes

[https://www.open-std.org/JTC1/SC35/WG5/docs/30112d10.pdf ISO 30112] specifies which Unicode characters are include in POSIX print category.

## Example


### Example

```cpp
#include <clocale>
#include <cwctype>
#include <iostream>

void demo_iswprint(std::string_view rem, const std::wint_t c)
{
    std::cout << std::boolalpha << std::hex << std::showbase
              << rem << "iswprint('" << c << "') = "
              << !!std::iswprint(c) << '\n';
}

int main()
{
    const wchar_t c1 = L'\u2002'; // en-space
    const wchar_t c2 = L'\u0082'; // break permitted

    demo_iswprint("In default locale:\n", c1);

    std::setlocale(LC_ALL, "en_US.utf8");
    demo_iswprint("In Unicode locale:\n", c1);
    demo_iswprint("", c2);
}
```


**Output:**
```
In default locale:
iswprint('0x2002') = false
In Unicode locale:
iswprint('0x2002') = true
iswprint('0x82') = false
```


## See also


| cpp/locale/dsc isprint | (see dedicated page) |
| cpp/string/byte/dsc isprint | (see dedicated page) |

