---
title: std::wbuffer_convert
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/wbuffer_convert
---

ddcl|header=locale|since=c++11|deprecated=c++17|removed=c++26|1=
template<
class Codecvt,
class Elem = wchar_t,
class Tr = std::char_traits<Elem>
> class wbuffer_convert : public std::basic_streambuf<Elem, Tr>
`std::wbuffer_convert` is a wrapper over stream buffer of type `std::basic_streambuf<char>` which gives it the appearance of `std::basic_streambuf<Elem>`. All I/O performed through `std::wbuffer_convert` undergoes character conversion as defined by the facet `Codecvt`. `std::wbuffer_convert` assumes ownership of the conversion facet, and cannot use a facet managed by a locale.
The standard facets suitable for use with `std::wbuffer_convert` are `std::codecvt_utf8` for UTF-8/UCS-2 and UTF-8/UCS-4 conversions and `std::codecvt_utf8_utf16` for UTF-8/UTF-16 conversions.
This class template makes the implicit character conversion functionality of `std::basic_filebuf` available for any `std::basic_streambuf`.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/locale/wbuffer_convert/dsc wbuffer_convert | (see dedicated page) |
| cpp/locale/wbuffer_convert/dsc ~wbuffer_convert | (see dedicated page) |
| cpp/locale/wbuffer_convert/dsc rdbuf | (see dedicated page) |
| cpp/locale/wbuffer_convert/dsc state | (see dedicated page) |


## See also


| cpp/locale/dsc wstring_convert | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8 | (see dedicated page) |
| cpp/locale/dsc codecvt_utf8_utf16 | (see dedicated page) |

