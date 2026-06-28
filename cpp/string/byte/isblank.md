---
title: std::isblank
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/isblank
---

ddcl|header=cctype|since=c++11|
int isblank( int ch );
Checks if the given character is a blank character as classified by the currently installed C locale. Blank characters are whitespace characters used to separate words within a sentence. In the default C locale, only space (`0x20`) and horizontal tab (`0x09`) are classified as blank characters.
The behavior is undefined if the value of `ch` is not representable as `unsigned char` and is not equal to `EOF`.

## Parameters


### Parameters

- `ch` - character to classify

## Return value

Non-zero value if the character is a blank character, zero otherwise.

## Notes


## See also


| cpp/locale/dsc isblank | (see dedicated page) |
| cpp/string/wide/dsc iswblank | (see dedicated page) |

