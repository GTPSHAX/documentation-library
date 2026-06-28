---
title: std::filesystem::path::path
type: Filesystem
source: https://en.cppreference.com/w/cpp/filesystem/path/path
---


```cpp
dcl|since=c++17|num=1|
path() noexcept;
dcl|since=c++17|num=2|
path( const path& p );
dcl|since=c++17|num=3|
path( path&& p ) noexcept;
dcl|since=c++17|num=4|1=
path( string_type&& source, format fmt = auto_format );
dcl|since=c++17|num=5|1=
template< class Source >
path( const Source& source, format fmt = auto_format );
dcl|since=c++17|num=6|1=
template< class InputIt >
path( InputIt first, InputIt last, format fmt = auto_format );
dcl|since=c++17|num=7|1=
template< class Source >
path( const Source& source, const std::locale& loc, format fmt = auto_format );
dcl|since=c++17|num=8|1=
template< class InputIt >
path( InputIt first, InputIt last, const std::locale& loc, format fmt = auto_format );
```

Constructs a new `path` object.
1. Constructs an empty path.
2. Copy constructor. Constructs a path whose pathname, in both native and generic formats, is the same as that of `p`.
3. Move constructor. Constructs a path whose pathname, in both native and generic formats, is the same as that of `p`, `p` is left in valid but unspecified state.
@4-6@ Constructs the path from a character sequence (format interpreted as specified by `fmt`) provided by `source` , which is a pointer or an input iterator to a null-terminated character/wide character sequence, an `std::basic_string` or an `std::basic_string_view`, or represented as a pair of input iterators [`first`, `last`) . Any of the character types `char`, <sup>(since C++20)</sup> `char8_t`, `char16_t`, `char32_t`, `wchar_t` is allowed, and the method of conversion to the native character set depends on the character type used by `source`.
:*If the source character type is `char`, the encoding of the source is assumed to be the native narrow encoding (so no conversion takes place on POSIX systems).
rrev|since=c++20|
:*If the source character type is `char8_t`, conversion from UTF-8 to native filesystem encoding is used.
:*If the source character type is `char16_t`, conversion from UTF-16 to native filesystem encoding is used.
:*If the source character type is `char32_t`, conversion from UTF-32 to native filesystem encoding is used.
:* If the source character type is `wchar_t`, the input is assumed to be the native wide encoding (so no conversion takes places on Windows).
@7,8@ Constructs the path from a character sequence (format interpreted as specified by `fmt`) provided by `source` , which is a pointer or an input iterator to a null-terminated character sequence, an `std::string`, an `std::string_view`, or represented as a pair of input iterators [`first`, `last`) . The only character type allowed is `char`. Uses `loc` to perform the character encoding conversion. If `value_type` is `wchar_t`, converts from to wide using the `std::codecvt<wchar_t, char, std::mbstate_t>` facet of `loc`. Otherwise, first converts to wide using the `std::codecvt<wchar_t, char, std::mbstate_t>` facet and then converts to filesystem native character type using `std::codecvt<wchar_t,value_type>` facet of `loc`.

## Parameters


### Parameters

- `p` - a path to copy
- `source` - `std::basic_string`, `std::basic_string_view`, pointer to a null-terminated character string, or input iterator with a character value type that points to a null-terminated character sequence (the character type must be `char` for overload )
- `first, last` - pair of *InputIterator*s that specify a character sequence
- `fmt` - enumerator of type `cpp/filesystem/path/format|path::format` which specifies how pathname format is to be interpreted
- `loc` - locale that defines encoding conversion to use

**Type requirements:**

- `InputIt`

## Exceptions

@2,4-8@

## Notes

rrev multi|until1=c++20|rev1=
For portable pathname generation from Unicode strings, see `u8path`.
|rev2=
`path` constructor supports creation from UTF-8 string when the source is a sequence of `char8_t`.

## Example


### Example

```cpp
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

int main()
{
    fs::path p1 = "/usr/lib/sendmail.cf"; // portable format
    fs::path p2 = "C:\\users\\abcdef\\AppData\\Local\\Temp\\"; // native format
    fs::path p3 = U"D:/猫.txt"; // UTF-32 string
    fs::path p4 = u8"~/狗.txt"; // UTF-8 string

    std::cout << "p1 = " << p1 << '\n'
              << "p2 = " << p2 << '\n'
              << "p3 = " << p3 << '\n'
              << "p4 = " << p4 << '\n';
}
```


**Output:**
```
p1 = "/usr/lib/sendmail.cf"
p2 = "C:\\users\\abcdef\\AppData\\Local\\Temp\\"
p3 = "D:/猫.txt"
p4 = "~/狗.txt"
```


## Defect reports


## See also


| cpp/filesystem/path/dsc u8path | (see dedicated page) |

