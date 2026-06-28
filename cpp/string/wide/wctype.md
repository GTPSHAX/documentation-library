---
title: std::wctype
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wctype
---

ddcl|header=cwctype|
std::wctype_t wctype( const char* str );
Constructs a value of type `std::wctype_t` that describes a `LC_CTYPE` category of wide character classification. It may be one of the standard classification categories, or a locale-specific category, such as `"jkanji"`.

## Parameters


### Parameters

- `str` - C string holding the name of the desired category
The following values of `str` are supported in all C locales:


| Item | Description |
|------|-------------|
| **value of {{tt** | str |


## Return value

`std::wctype_t` object suitable for use with `std::iswctype` to classify wide characters according to the named category of the current C locale or zero if `str` does not name a category supported by the current C locale.

## See also


| cpp/string/wide/dsc iswctype | (see dedicated page) |

