---
title: std::basic_ios::narrow
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/narrow
---

ddcl|
char narrow( char_type c, char dfault ) const;
Converts a current locale-specific character `c` to its standard equivalent. The result is converted from `char_type` to `char` if needed. If no conversion can be performed, the function returns `dfault`.
Effectively calls `std::use_facet< std::ctype<char_type> >(getloc()).narrow(c, dfault);`.

## Parameters


### Parameters

- `c` - character to convert
- `dfault` - character to return if the conversion was unsuccessful

## Return value

Character converted to its standard equivalent and then to `char`. `dfault` is returned if the conversion fails.

## See also


| cpp/io/basic_ios/dsc widen | (see dedicated page) |
| cpp/locale/ctype/dsc narrow | (see dedicated page) |
| cpp/string/multibyte/dsc wctob | (see dedicated page) |

