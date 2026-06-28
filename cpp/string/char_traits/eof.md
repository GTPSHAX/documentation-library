---
title: std::char_traits::eof
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/eof
---

ddcl|notes=<sup>(constexpr C++11)</sup><br>|
static int_type eof();
Returns a value not equivalent to any valid value of type `char_type`.
See *CharTraits* for the general requirements on character traits for `X::eof`.

## Parameters

(none)

## Return value


| tt | char_type |
| c | eof() |
| - |
| c/core | char |
| c | EOF |
| - |
| c/core | wchar_t |
| c | WEOF |
| - |
| c/core | char8_t |
| an implementation-defined constant that<br>cannot appear as a valid UTF-8 code unit |
| - |
| c/core | char16_t |
| an implementation-defined constant that<br>cannot appear as a valid UTF-16 code unit |
| - |
| c/core | char32_t |
| an implementation-defined constant that<br>cannot appear as a Unicode code point |


## Complexity

Constant.

## See also


| cpp/string/char_traits/dsc not_eof | (see dedicated page) |

