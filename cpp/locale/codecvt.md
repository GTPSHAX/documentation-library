---
title: std::codecvt
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt
---

ddcl|header=locale|
template<
class InternT,
class ExternT,
class StateT
> class codecvt;
Class template `std::codecvt` encapsulates conversion of character strings, including wide and multibyte, from one encoding to another. All file I/O operations performed through `std::basic_fstream<CharT>` use the `std::codecvt<CharT, char, std::mbstate_t>` facet of the locale imbued in the stream.

## Specializations

The standard library is guaranteed to provide the following specializations (they are `required to be implemented by any locale object`):


| locale | |


## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/locale/codecvt/dsc out | (see dedicated page) |
| cpp/locale/codecvt/dsc in | (see dedicated page) |
| cpp/locale/codecvt/dsc unshift | (see dedicated page) |
| cpp/locale/codecvt/dsc encoding | (see dedicated page) |
| cpp/locale/codecvt/dsc always_noconv | (see dedicated page) |
| cpp/locale/codecvt/dsc length | (see dedicated page) |
| cpp/locale/codecvt/dsc max_length | (see dedicated page) |


## Protected member functions


| cpp/locale/codecvt/dsc do_out | (see dedicated page) |
| cpp/locale/codecvt/dsc do_in | (see dedicated page) |
| cpp/locale/codecvt/dsc do_unshift | (see dedicated page) |
| cpp/locale/codecvt/dsc do_encoding | (see dedicated page) |
| cpp/locale/codecvt/dsc do_always_noconv | (see dedicated page) |
| cpp/locale/codecvt/dsc do_length | (see dedicated page) |
| cpp/locale/codecvt/dsc do_max_length | (see dedicated page) |


## Example


### Example

```cpp
#include <codecvt>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <locale>
#include <string>

// utility wrapper to adapt locale-bound facets for wstring/wbuffer convert
template<class Facet>
struct deletable_facet : Facet
{
    template<class... Args>
    deletable_facet(Args&&... args) : Facet(std::forward<Args>(args)...) {}
    ~deletable_facet() {}
};

int main()
{
    // UTF-8 narrow multibyte encoding
    std::string data = reinterpret_cast<const char*>(+u8"z\u00df\u6c34\U0001f34c");
                       // or reinterpret_cast<const char*>(+u8"zß水🍌")
                       // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9f\x8d\x8c"

    std::ofstream("text.txt") << data;

    // using system-supplied locale's codecvt facet
    std::wifstream fin("text.txt");
    // reading from wifstream will use codecvt<wchar_t, char, std::mbstate_t>
    // this locale's codecvt converts UTF-8 to UCS4 (on systems such as Linux)
    fin.imbue(std::locale("en_US.UTF-8"));
    std::cout << "The UTF-8 file contains the following UCS4 code units:\n" << std::hex;
    for (wchar_t c; fin >> c;)
        std::cout << "U+" << std::setw(4) << std::setfill('0')
                  << static_cast<uint32_t>(c) << ' ';

    // using standard (locale-independent) codecvt facet
    std::wstring_convert<
        deletable_facet<std::codecvt<char16_t, char, std::mbstate_t>>, char16_t> conv16;
    std::u16string str16 = conv16.from_bytes(data);

    std::cout << "\n\nThe UTF-8 file contains the following UTF-16 code units:\n"
              << std::hex;
    for (char16_t c : str16)
        std::cout << "U+" << std::setw(4) << std::setfill('0')
                  << static_cast<uint16_t>(c) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
The UTF-8 file contains the following UCS4 code units:
U+007a U+00df U+6c34 U+1f34c 

The UTF-8 file contains the following UTF-16 code units:
U+007a U+00df U+6c34 U+d83c U+df4c
```


## Defect reports


## See also


| cpp/locale/dsc codecvt_base | (see dedicated page) |
| cpp/locale/dsc codecvt_byname | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf16 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |

