---
title: std::codecvt_utf16
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt_utf16
---

ddcl|header=codecvt|since=c++11|deprecated=c++17|removed=c++26|1=
template<
class Elem,
unsigned long Maxcode = 0x10ffff,
std::codecvt_mode Mode = (std::codecvt_mode)0 >
class codecvt_utf16
: public std::codecvt<Elem, char, std::mbstate_t>;
`std::codecvt_utf16` is a `std::codecvt` facet which encapsulates conversion between a UTF-16 encoded byte string and UCS-2 or UTF-32 character string (depending on the type of `Elem`). This `std::codecvt` facet can be used to read and write UTF-16 files in binary mode.
UCS-2 is an archaic encoding that is a subset of UTF-16, which encodes scalar values in the range U+0000-U+FFFF (Basic Multilingual Plane) only.

## Template Parameters


### Parameters

- `Elem` - either `char16_t`, `char32_t`, or `wchar_t`
- `Maxcode` - the largest value of `Elem` that this facet will read or write without error 
- `Mode` - a constant of type `std::codecvt_mode`

## Member functions

member|codecvt_utf16|

```cpp
dcl|1=
explicit codecvt_utf16( std::size_t refs = 0 );
```

Constructs a new `std::codecvt_utf16` facet, passes the initial reference counter `refs` to the base class.

## Parameters


### Parameters

- `refs` - the number of references that link to the facet
member|~codecvt_utf16|

```cpp
dcl|1=
~codecvt_utf16();
```

Destroys the facet. Unlike the locale-managed facets, this facet's destructor is public.

## Notes

Although the standard requires that this facet works with UCS-2 when the size of `Elem` is 16 bits, some implementations use UTF-16 instead, making this a non-converting locale. The term "UCS-2" was deprecated and removed from ISO 10646.

## Example


### Example

```cpp
#include <codecvt>
#include <cwchar>
#include <fstream>
#include <iostream>
#include <locale>
#include <string>

void prepare_file()
{
    // UTF-16le data (if host system is little-endian)
    char16_t utf16le[4] = {0x007a,          // latin small letter 'z' U+007a
                           0x6c34,          // CJK ideograph "water"  U+6c34
                           0xd834, 0xdd0b}; // musical sign segno U+1d10b    

    // store in a file
    std::ofstream fout("text.txt");
    fout.write(reinterpret_cast<char*>(utf16le), sizeof utf16le);
}

int main()
{
    prepare_file();
    // open as a byte stream
    std::wifstream fin("text.txt", std::ios::binary);
    // apply facet
    fin.imbue(std::locale(fin.getloc(),
        new std::codecvt_utf16<wchar_t, 0x10ffff, std::little_endian>));

    wchar_t c = 0;
    for (std::cout << std::showbase << std::hex; fin.get(c);
         std::cout << static_cast<std::wint_t>(c) << '\n');
}
```


**Output:**
```
0x7a
0x6c34
0x1d10b
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
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |

