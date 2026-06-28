---
title: std::codecvt_mode
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt_mode
---

ddcl|header=codecvt|since=c++11|deprecated=c++17|removed=c++26|1=
enum codecvt_mode
{
consume_header = 4,
generate_header = 2,
little_endian = 1
};
The facets `std::codecvt_utf8`, `std::codecvt_utf16`, and `std::codecvt_utf8_utf16` accept an optional value of type `std::codecvt_mode` as a template argument, which specifies optional features of the unicode string conversion.

## Constants


| Item | Description |
|------|-------------|
| locale | |
| **Enumerator** | Meaning |

The recognized byte order marks are:
If `std::consume_header` is not selected when reading a file beginning with byte order mark, the Unicode character U+FEFF (Zero width non-breaking space) will be read as the first character of the string content.

## Example


### Example

```cpp
#include <codecvt>
#include <cwchar>
#include <fstream>
#include <iostream>
#include <locale>
#include <string>

int main()
{
    // UTF-8 data with BOM
    std::ofstream{"text.txt"} << "\ufeffz\u6c34\U0001d10b";

    // read the UTF-8 file, skipping the BOM
    std::wifstream fin{"text.txt"};
    fin.imbue(std::locale(fin.getloc(),
                          new std::codecvt_utf8<wchar_t, 0x10ffff, std::consume_header>));

    for (wchar_t c; fin.get(c);)
        std::cout << std::hex << std::showbase << (std::wint_t)c << '\n';
}
```


**Output:**
```
0x7a
0x6c34
0x1d10b
```


## See also


| cpp/locale/dsc codecvt | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf16 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |

