---
title: std::basic_ios::widen
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/widen
---

ddcl|
char_type widen( char c ) const;
Converts a character `c` to its equivalent in the current locale. The result is converted from `char` to character type used within the stream if needed.
Effectively calls `std::use_facet< std::ctype<char_type> >(getloc()).widen(c)`.

## Parameters


### Parameters

- `c` - character to convert

## Return value

Character converted to `char_type`

## See also


| cpp/io/basic_ios/dsc narrow | (see dedicated page) |
| cpp/locale/ctype/dsc do_widen | (see dedicated page) |
| cpp/string/multibyte/dsc btowc | (see dedicated page) |

