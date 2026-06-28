---
title: std::codecvt_utf8_utf16
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt_utf8_utf16
---

ddcl|header=codecvt|since=c++11|deprecated=c++17|removed=c++26|1=
template<
class Elem,
unsigned long Maxcode = 0x10ffff,
std::codecvt_mode Mode = (std::codecvt_mode)0 >
class codecvt_utf8_utf16
: public std::codecvt<Elem, char, std::mbstate_t>;
`std::codecvt_utf8_utf16` is a `std::codecvt` facet which encapsulates conversion between a UTF-8 encoded byte string and UTF-16 encoded character string. If `Elem` is a 32-bit type, one UTF-16 code unit will be stored in each 32-bit character of the output sequence.
This is an N:M conversion facet, and cannot be used with `std::basic_filebuf` (which only permits 1:N conversions, such as UTF-32/UTF-8, between the internal and the external encodings). This facet can be used with `std::wstring_convert`.

## Template Parameters


### Parameters

- `Elem` - either `char16_t`, `char32_t`, or `wchar_t`
- `Maxcode` - the largest value of `Elem` that this facet will read or write without error
- `Mode` - a constant of type `std::codecvt_mode`

## Member functions

member|codecvt_utf8_utf16|

```cpp
dcl|1=
explicit codecvt_utf8_utf16( std::size_t refs = 0 );
```

Constructs a new `std::codecvt_utf8_utf16` facet, passes the initial reference counter `refs` to the base class.

## Parameters


### Parameters

- `refs` - the number of references that link to the facet
member|~codecvt_utf8_utf16|

```cpp
dcl|1=
~codecvt_utf8_utf16();
```

Destroys the facet. Unlike the locale-managed facets, this facet's destructor is public.

## Example


### Example

```cpp
#include <cassert>
#include <codecvt>
#include <cstdint>
#include <iostream>
#include <locale>
#include <string>

int main()
{
    std::string u8 = "z\u00df\u6c34\U0001f34c";
    std::u16string u16 = u"z\u00df\u6c34\U0001f34c";

    // UTF-8 to UTF-16/char16_t
    std::u16string u16_conv = std::wstring_convert<
        std::codecvt_utf8_utf16<char16_t>, char16_t>{}.from_bytes(u8);
    assert(u16 == u16_conv);
    std::cout << "UTF-8 to UTF-16 conversion produced " << u16_conv.size()
              << " code units:\n" << std::showbase << std::hex;
    for (char16_t c : u16_conv)
        std::cout << static_cast<std::uint16_t>(c) << ' ';

    // UTF-16/char16_t to UTF-8
    std::string u8_conv = std::wstring_convert<
        std::codecvt_utf8_utf16<char16_t>, char16_t>{}.to_bytes(u16);
    assert(u8 == u8_conv);
    std::cout << "\nUTF-16 to UTF-8 conversion produced "
              << std::dec << u8_conv.size() << " bytes:\n" << std::hex;
    for (char c : u8_conv)
        std::cout << +static_cast<unsigned char>(c) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
UTF-8 to UTF-16 conversion produced 5 code units:
0x7a 0xdf 0x6c34 0xd83c 0xdf4c
UTF-16 to UTF-8 conversion produced 10 bytes:
0x7a 0xc3 0x9f 0xe6 0xb0 0xb4 0xf0 0x9f 0x8d 0x8c
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2229 | C++98 | the constructor and destructor were not specified | specifies them |


## See also


| cpp/locale/dsc codecvt | (see dedicated page) |
| cpp/locale/dsc codecvt_mode | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf16 | (see dedicated page) |

