---
title: Null-terminated wide strings
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide
---


# Null-terminated wide strings

A null-terminated wide string is a sequence of valid wide characters, ending with a null character.

## Functions


#### Character classification

| cwctype | |
| cpp/string/wide/dsc iswalnum | (see dedicated page) |
| cpp/string/wide/dsc iswalpha | (see dedicated page) |
| cpp/string/wide/dsc iswlower | (see dedicated page) |
| cpp/string/wide/dsc iswupper | (see dedicated page) |
| cpp/string/wide/dsc iswdigit | (see dedicated page) |
| cpp/string/wide/dsc iswxdigit | (see dedicated page) |
| cpp/string/wide/dsc iswcntrl | (see dedicated page) |
| cpp/string/wide/dsc iswgraph | (see dedicated page) |
| cpp/string/wide/dsc iswspace | (see dedicated page) |
| cpp/string/wide/dsc iswblank | (see dedicated page) |
| cpp/string/wide/dsc iswprint | (see dedicated page) |
| cpp/string/wide/dsc iswpunct | (see dedicated page) |
| cpp/string/wide/dsc iswctype | (see dedicated page) |
| cpp/string/wide/dsc wctype | (see dedicated page) |

#### Character manipulation

| cwctype | |
| cpp/string/wide/dsc towlower | (see dedicated page) |
| cpp/string/wide/dsc towupper | (see dedicated page) |
| cpp/string/wide/dsc towctrans | (see dedicated page) |
| cpp/string/wide/dsc wctrans | (see dedicated page) |


#### Conversions to numeric formats

| cwchar | |
| cpp/string/wide/dsc wcstol | (see dedicated page) |
| cpp/string/wide/dsc wcstoul | (see dedicated page) |
| cpp/string/wide/dsc wcstof | (see dedicated page) |
| cinttypes | |
| cpp/string/wide/dsc wcstoimax | (see dedicated page) |


#### String manipulation

| cwchar | |
| cpp/string/wide/dsc wcscpy | (see dedicated page) |
| cpp/string/wide/dsc wcsncpy | (see dedicated page) |
| cpp/string/wide/dsc wcscat | (see dedicated page) |
| cpp/string/wide/dsc wcsncat | (see dedicated page) |
| cpp/string/wide/dsc wcsxfrm | (see dedicated page) |

#### String examination

| cwchar | |
| cpp/string/wide/dsc wcslen | (see dedicated page) |
| cpp/string/wide/dsc wcscmp | (see dedicated page) |
| cpp/string/wide/dsc wcsncmp | (see dedicated page) |
| cpp/string/wide/dsc wcscoll | (see dedicated page) |
| cpp/string/wide/dsc wcschr | (see dedicated page) |
| cpp/string/wide/dsc wcsrchr | (see dedicated page) |
| cpp/string/wide/dsc wcsspn | (see dedicated page) |
| cpp/string/wide/dsc wcscspn | (see dedicated page) |
| cpp/string/wide/dsc wcspbrk | (see dedicated page) |
| cpp/string/wide/dsc wcsstr | (see dedicated page) |
| cpp/string/wide/dsc wcstok | (see dedicated page) |


#### Wide character array manipulation

| cwchar | |
| cpp/string/wide/dsc wmemcpy | (see dedicated page) |
| cpp/string/wide/dsc wmemmove | (see dedicated page) |
| cpp/string/wide/dsc wmemcmp | (see dedicated page) |
| cpp/string/wide/dsc wmemchr | (see dedicated page) |
| cpp/string/wide/dsc wmemset | (see dedicated page) |


## Types


| cwctype | |
| nolink=true|wctrans_t|scalar type that holds locale-specific character mapping | |
| nolink=true|wctype_t|scalar type that holds locale-specific character classification | |
| cwctype | |
| cwchar | |
| nolink=true|wint_t|integer type that can hold any valid wide character and at least one more value | |


## Macros


| cwchar | |


## See also

