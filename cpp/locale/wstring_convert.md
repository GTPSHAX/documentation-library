---
title: std::wstring_convert
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/wstring_convert
---

ddcl|header=locale|since=c++11|deprecated=c++17|removed=c++26|1=
template<
class Codecvt,
class Elem = wchar_t,
class Wide_alloc = std::allocator<Elem>,
class Byte_alloc = std::allocator<char>
> class wstring_convert;
Class template `std::wstring_convert` performs conversions between byte string `std::string` and wide string `std::basic_string<Elem>`, using an individual code conversion facet `Codecvt`. `std::wstring_convert` assumes ownership of the conversion facet, and cannot use a facet managed by a locale.
The standard facets suitable for use with `std::wstring_convert` are `std::codecvt_utf8` for UTF-8/UCS-2 and UTF-8/UCS-4 conversions and `std::codecvt_utf8_utf16` for UTF-8/UTF-16 conversions.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/locale/wstring_convert/dsc wstring_convert | (see dedicated page) |
| cpp/locale/wstring_convert/dsc ~wstring_convert | (see dedicated page) |
| cpp/locale/wstring_convert/dsc from_bytes | (see dedicated page) |
| cpp/locale/wstring_convert/dsc to_bytes | (see dedicated page) |
| cpp/locale/wstring_convert/dsc converted | (see dedicated page) |
| cpp/locale/wstring_convert/dsc state | (see dedicated page) |


## See also


| cpp/locale/dsc wbuffer_convert | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |

