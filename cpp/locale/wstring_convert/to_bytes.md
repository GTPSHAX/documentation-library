---
title: std::wstring_convert::to_bytes
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/wstring_convert/to_bytes
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|
byte_string to_bytes( Elem wchar );
dcl|num=2|
byte_string to_bytes( const Elem* wptr );
dcl|num=3|
byte_string to_bytes( const wide_string& wstr );
dcl|num=4|
byte_string to_bytes( const Elem* first, const Elem* last );
```

Converts a wide sequence to a byte string using the facet pointed to by .
1. The wide sequence only consists of one element `byte`.
2. The wide sequence is the null-terminated sequence beginning at `ptr`.
3. The wide sequence is the sequence contained in `str`.
4. The wide sequence is the range [first, last).
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
#include <iomanip>
#include <iostream>
#include <locale>
#include <string>

// utility function for output
void hex_print(const std::string& s)
{
    std::cout << std::hex << std::setfill('0');
    for (unsigned char c : s)
        std::cout << std::setw(2) << static_cast<int>(c) << ' ';
    std::cout << std::dec << '\n';
}

int main()
{
    // wide character data
    std::wstring wstr = L"z\u00df\u6c34\U0001f34c"; // or L"zß水🍌"

    // wide to UTF-8
    std::wstring_convert<std::codecvt_utf8<wchar_t>> conv1;
    std::string u8str = conv1.to_bytes(wstr);
    std::cout << "UTF-8 conversion produced " << u8str.size() << " bytes:\n";
    hex_print(u8str);

    // wide to UTF-16le
    std::wstring_convert<std::codecvt_utf16<wchar_t, 0x10ffff, std::little_endian>> conv2;
    std::string u16str = conv2.to_bytes(wstr);
    std::cout << "UTF-16le conversion produced " << u16str.size() << " bytes:\n";
    hex_print(u16str);
}
```


**Output:**
```
UTF-8 conversion produced 10 bytes:
7a c3 9f e6 b0 b4 f0 9f 8d 8c 
UTF-16le conversion produced 10 bytes:
7a 00 df 00 34 6c 3c d8 4c df
```


## See also


| cpp/locale/wstring_convert/dsc from_bytes | (see dedicated page) |
| cpp/string/multibyte/dsc wcsrtombs | (see dedicated page) |
| cpp/locale/codecvt/dsc do_out | (see dedicated page) |

