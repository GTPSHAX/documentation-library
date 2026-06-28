---
title: std::wstring_convert::from_bytes
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/wstring_convert/from_bytes
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|
wide_string from_bytes( char byte );
dcl|num=2|
wide_string from_bytes( const char* ptr );
dcl|num=3|
wide_string from_bytes( const byte_string& str );
dcl|num=4|
wide_string from_bytes( const char* first, const char* last );
```

Converts a byte sequence to a wide string using the facet pointed to by .
1. The byte sequence only consists of one element `byte`.
2. The byte sequence is the null-terminated sequence beginning at `ptr`.
3. The byte sequence is the sequence contained in `str`.
4. The byte sequence is the range [first, last).
Before the conversion begins, if `*this` was '''not''' constructed with constructor overload `(3)`,  will be set to its default value (the initial conversion state).
The number of input elements successfully converted will be stored in .

## Return value

If the conversion succeeds, returns the conversion result. Otherwise, if `*this` is constructed with constructor overload `(4)`, returns .

## Exceptions

If the conversion fails and `*this` was '''not''' constructed with constructor overload `(4)`, throws `std::range_error`.

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
    std::string utf8 = "z\u00df\u6c34\U0001d10b"; // or u8"zß水𝄋"
                 // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b";

    // the UTF-8 / UTF-16 standard conversion facet
    std::u16string utf16 = 
        std::wstring_convert<std::codecvt_utf8_utf16<char16_t>,
                             char16_t>{}.from_bytes(utf8.data());
    std::cout << "UTF-16 conversion produced " << utf16.size()
              << " code units: " << std::showbase;
    for (char16_t c : utf16)
        std::cout << std::hex << static_cast<std::uint16_t>(c) << ' ';

    // the UTF-8 / UTF-32 standard conversion facet
    std::u32string utf32 =
        std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t>{}.from_bytes(utf8);
    std::cout << "\nUTF-32 conversion produced " << std::dec
              << utf32.size() << " code units: ";
    for (char32_t c : utf32)
        std::cout << std::hex << static_cast<std::uint32_t>(c) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
UTF-16 conversion produced 5 code units: 0x7a 0xdf 0x6c34 0xd834 0xdd0b
UTF-32 conversion produced 4 code units: 0x7a 0xdf 0x6c34 0x1d10b
```


## See also


| cpp/locale/wstring_convert/dsc to_bytes | (see dedicated page) |
| cpp/string/multibyte/dsc mbsrtowcs | (see dedicated page) |
| cpp/locale/codecvt/dsc do_in | (see dedicated page) |

