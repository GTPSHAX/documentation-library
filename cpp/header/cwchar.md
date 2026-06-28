---
title: cwchar
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/cwchar
---

This header is part of the null-terminated wide and multibyte strings libraries.
It also provides some C-style I/O functions and conversion from C-style Date.

## Macros


| cpp/types/dsc NULL | (see dedicated page) |
| cpp/types/dsc WCHAR_WIDTH | (see dedicated page) |
| cpp/types/dsc WCHAR_MIN | (see dedicated page) |
| cpp/types/dsc WCHAR_MAX | (see dedicated page) |


## Types


| cpp/string/multibyte/dsc mbstate_t | (see dedicated page) |
| cpp/types/dsc size_t | (see dedicated page) |
| cpp/chrono/c/dsc tm | (see dedicated page) |


## Functions


#### String manipulation

| cpp/string/wide/dsc wcscpy | (see dedicated page) |
| cpp/string/wide/dsc wcsncpy | (see dedicated page) |
| cpp/string/wide/dsc wcscat | (see dedicated page) |
| cpp/string/wide/dsc wcsncat | (see dedicated page) |
| cpp/string/wide/dsc wcsxfrm | (see dedicated page) |

#### String examination

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

| cpp/string/wide/dsc wmemcpy | (see dedicated page) |
| cpp/string/wide/dsc wmemmove | (see dedicated page) |
| cpp/string/wide/dsc wmemcmp | (see dedicated page) |
| cpp/string/wide/dsc wmemchr | (see dedicated page) |
| cpp/string/wide/dsc wmemset | (see dedicated page) |

#### Multibyte/wide character conversion 

| cpp/string/multibyte/dsc mbsinit | (see dedicated page) |
| cpp/string/multibyte/dsc btowc | (see dedicated page) |
| cpp/string/multibyte/dsc wctob | (see dedicated page) |
| cpp/string/multibyte/dsc mbrlen | (see dedicated page) |
| cpp/string/multibyte/dsc mbrtowc | (see dedicated page) |
| cpp/string/multibyte/dsc wcrtomb | (see dedicated page) |
| cpp/string/multibyte/dsc mbsrtowcs | (see dedicated page) |
| cpp/string/multibyte/dsc wcsrtombs | (see dedicated page) |

#### Input/Output 

| cpp/io/c/dsc fgetwc | (see dedicated page) |
| cpp/io/c/dsc fgetws | (see dedicated page) |
| cpp/io/c/dsc fputwc | (see dedicated page) |
| cpp/io/c/dsc fputws | (see dedicated page) |
| cpp/io/c/dsc getwchar | (see dedicated page) |
| cpp/io/c/dsc putwchar | (see dedicated page) |
| cpp/io/c/dsc ungetwc | (see dedicated page) |
| cpp/io/c/dsc fwide | (see dedicated page) |
| cpp/io/c/dsc fwscanf | (see dedicated page) |
| cpp/io/c/dsc vfwscanf | (see dedicated page) |
| cpp/io/c/dsc fwprintf | (see dedicated page) |
| cpp/io/c/dsc vfwprintf | (see dedicated page) |

#### String conversions

| cpp/chrono/c/dsc wcsftime | (see dedicated page) |
| cpp/string/wide/dsc wcstol | (see dedicated page) |
| cpp/string/wide/dsc wcstoul | (see dedicated page) |
| cpp/string/wide/dsc wcstof | (see dedicated page) |


## Notes

* `NULL` is also defined in the following headers:
**
**
**
**
**
* `std::size_t` is also defined in the following headers:
**
**
**
* `std::wint_t` is also defined in the following headers:
**
* `std::tm` is also defined in the following headers:
**

## Synopsis


## Defect reports

