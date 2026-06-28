---
title: std::filesystem::path::generic_wstring
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/generic_string
---


```cpp
dcl|num=1|since=c++17|1=
template< class CharT, class Traits = std::char_traits<CharT>,
class Alloc = std::allocator<CharT> >
std::basic_string<CharT,Traits,Alloc>
generic_string( const Alloc& a = Alloc() ) const;
dcl|num=2|since=c++17|
std::string generic_string() const;
dcl|num=3|since=c++17|
std::wstring generic_wstring() const;
dcl|num=4|since=c++17|
std::u16string generic_u16string() const;
dcl|num=5|since=c++17|
std::u32string generic_u32string() const;
dcl rev multi|num=6|since1=c++17|until1=c++20|dcl1=
std::string generic_u8string() const;
|dcl2=
std::u8string generic_u8string() const;
```

Returns the internal pathname in generic pathname format, converted to specific string type. Conversion, if any, is specified as follows:
The `/` character is used as the directory separator.
1. All memory allocations are performed by `a`.
6. The result encoding in the case of `u8string()` is always UTF-8.

## Parameters


### Parameters

- `a` - allocator to construct the string with

**Type requirements:**


## Return value

The internal pathname in generic pathname format, converted to specified string type.

## Example


### Example

```cpp
#include <cstddef>
#include <filesystem>
#include <iomanip>
#include <iostream>
#include <span>
#include <string_view>

void print(std::string_view rem, auto const& str)
{
    std::cout << rem << std::hex << std::uppercase << std::setfill('0');
    for (const auto b : std::as_bytes(std::span{str}))
        std::cout << std::setw(2) << std::to_integer<unsigned>(b) << ' ';
    std::cout << '\n';
}

int main()
{
    std::filesystem::path p{"/家/屋"};
    std::cout << p << '\n';

    print("string    : ", p.generic_string());
    print("u8string  : ", p.generic_u8string());
    print("u16string : ", p.generic_u16string());
    print("u32string : ", p.generic_u32string());
    print("wstring   : ", p.generic_wstring());
}
```


**Output:**
```
"/家/屋"
string    : 2F E5 AE B6 2F E5 B1 8B
u8string  : 2F E5 AE B6 2F E5 B1 8B
u16string : 2F 00 B6 5B 2F 00 4B 5C
u32string : 2F 00 00 00 B6 5B 00 00 2F 00 00 00 4B 5C 00 00
wstring   : 2F 00 00 00 B6 5B 00 00 2F 00 00 00 4B 5C 00 00
```


## See also


| cpp/filesystem/path/dsc string | (see dedicated page) |

