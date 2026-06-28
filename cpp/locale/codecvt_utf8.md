---
title: std::codecvt_utf8
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt_utf8
---

ddcl|header=codecvt|since=c++11|deprecated=c++17|removed=c++26|1=
template<
class Elem,
unsigned long Maxcode = 0x10ffff,
std::codecvt_mode Mode = (std::codecvt_mode)0 >
class codecvt_utf8
: public std::codecvt<Elem, char, std::mbstate_t>;
`std::codecvt_utf8` is a `std::codecvt` facet which encapsulates conversion between a UTF-8 encoded byte string and UCS-2 or UTF-32 character string (depending on the type of `Elem`). This `std::codecvt` facet can be used to read and write UTF-8 files, both text and binary.
UCS-2 is an archaic encoding that is a subset of UTF-16, which encodes scalar values in the range U+0000-U+FFFF (Basic Multilingual Plane) only.

## Template Parameters


### Parameters

- `Elem` - either `char16_t`, `char32_t`, or `wchar_t`
- `Maxcode` - the largest value of `Elem` that this facet will read or write without error 
- `Mode` - a constant of type `std::codecvt_mode`

## Member functions

member|codecvt_utf8|

```cpp
dcl|1=
explicit codecvt_utf8( std::size_t refs = 0 );
```

Constructs a new `std::codecvt_utf8` facet, passes the initial reference counter `refs` to the base class.

## Parameters


### Parameters

- `refs` - the number of references that link to the facet
member|~codecvt_utf8|

```cpp
dcl|1=
~codecvt_utf8();
```

Destroys the facet. Unlike the locale-managed facets, this facet's destructor is public.

## Notes

Although the standard requires that this facet works with UCS-2 when the size of `Elem` is 16 bits, some implementations use UTF-16 instead. The term "UCS-2" was deprecated and removed from ISO 10646.

## Example


### Example

```cpp
#include <codecvt>
#include <cstdint>
#include <iostream>
#include <locale>
#include <string>

int main()
{
    // UTF-8 data. The character U+1d10b, musical sign segno, does not fit in UCS-2
    std::string utf8 = "z\u6c34\U0001d10b";

    // the UTF-8 / UTF-16 standard conversion facet
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> utf16conv;
    std::u16string utf16 = utf16conv.from_bytes(utf8);
    std::cout << "UTF-16 conversion produced " << utf16.size() << " code units:\n"
              << std::showbase << std::hex;
    for (char16_t c : utf16)
        std::cout << static_cast<std::uint16_t>(c) << ' ';

    // the UTF-8 / UCS-2 standard conversion facet
    std::wstring_convert<std::codecvt_utf8<char16_t>, char16_t> ucs2conv;
    try
    {
        std::u16string ucs2 = ucs2conv.from_bytes(utf8);
    }
    catch(const std::range_error& e)
    {
        std::u16string ucs2 = ucs2conv.from_bytes(utf8.substr(0, ucs2conv.converted()));
        std::cout << "\nUCS-2 failed after producing " << std::dec << ucs2.size()
                  << " characters:\n" << std::showbase << std::hex;
        for (char16_t c : ucs2)
            std::cout << static_cast<std::uint16_t>(c) << ' ';
        std::cout << '\n';
    }
}
```


**Output:**
```
UTF-16 conversion produced 4 code units:
0x7a 0x6c34 0xd834 0xdd0b
UCS-2 failed after producing 2 characters:
0x7a 0x6c34
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2229 | C++98 | the constructor and destructor were not specified | specifies them |


## See also


| cpp/locale/dsc codecvt | (see dedicated page) |
| cpp/locale/dsc codecvt_mode | (see dedicated page) |
| cpp/locale/dsc codecvt_utf16 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |

