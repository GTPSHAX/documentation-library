---
title: std::from_chars
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/from_chars
---


```cpp
**Header:** `<`charconv`>`
|1=
std::from_chars_result
from_chars( const char* first, const char* last,
/* integer-type */& value, int base = 10 );
dcl|num=2|since=c++17|1=
std::from_chars_result
from_chars( const char* first, const char* last,
/* floating-point-type */& value,
std::chars_format fmt = std::chars_format::general );
```

Analyzes the character sequence [first, last) for a pattern described below. If no characters match the pattern or if the value obtained by parsing the matched characters is not representable in the type of `value`, `value` is unmodified, otherwise the characters matching the pattern are interpreted as a text representation of an arithmetic value, which is stored in `value`.
1. Integer parsers: Expects the pattern identical to the one used by `std::strtol` in the default ("C") locale and the given non-zero numeric base, except that
* `"0x"` or `"0X"` prefixes are not recognized if `base` is 16
* only the minus sign is recognized (not the plus sign), and only for signed integer types of `value`
* leading whitespace is not ignored.
The library provides overloads for all<sup>(since C++23)</sup>  cv-unqualified signed and unsigned integer types and `char` as the referenced type of the parameter `value`.
2. Floating-point parsers: Expects the pattern identical to the one used by `std::strtod` in the default ("C") locale, except that
* the plus sign is not recognized outside of the exponent (only the minus sign is permitted at the beginning)
* if `fmt` has `cpp/utility/chars_format|std::chars_format::scientific` set but not `cpp/utility/chars_format|std::chars_format::fixed`, the exponent part is required (otherwise it is optional)
* if `fmt` has `cpp/utility/chars_format|std::chars_format::fixed` set but not `cpp/utility/chars_format|std::chars_format::scientific`, the optional exponent is not permitted
* if `fmt` is `cpp/utility/chars_format|std::chars_format::hex`, the prefix `"0x"` or `"0X"` is not permitted (the string `"0x123"` parses as the value `"0"` with unparsed remainder `"x123"`)
* leading whitespace is not ignored.
@@ In any case, the resulting value is one of at most two floating-point values closest to the value of the string matching the pattern, after rounding according to `std::round_to_nearest`.
@@ The library provides overloads for all cv-unqualified <sup>(until C++23)</sup> standard floating-point types as the referenced type of the parameter `value`.

## Parameters


### Parameters

- `first, last` - valid character range to parse
- `value` - the out-parameter where the parsed value is stored if successful
- `base` - integer base to use: a value between 2 and 36 (inclusive).
- `fmt` - floating-point formatting to use, a bitmask of type    

## Return value

On success, returns a value of type  such that `ptr` points at the first character not matching the pattern, or has the value equal to `last` if all characters match and `ec` is value-initialized.
If there is no pattern match, returns a value of type  such that `ptr` equals `first` and `ec` equals `std::errc::invalid_argument`. `value` is unmodified.
If the pattern was matched, but the parsed value is not in the range representable by the type of `value`, returns value of type  such that `ec` equals `std::errc::result_out_of_range` and `ptr` points at the first character not matching the pattern. `value` is unmodified.

## Exceptions

Throws nothing.

## Notes

Unlike other parsing functions in C++ and C libraries, `std::from_chars` is locale-independent, non-allocating, and non-throwing. Only a small subset of parsing policies used by other libraries (such as `std::sscanf`) is provided. This is intended to allow the fastest possible implementation that is useful in common high-throughput contexts such as text-based interchange ([JSON](https://en.wikipedia.org/wiki/JSON) or [XML](https://en.wikipedia.org/wiki/XML)).
The guarantee that `std::from_chars` can recover every floating-point value formatted by  exactly is only provided if both functions are from the same implementation.
A pattern consisting of a sign with no digits following it is treated as pattern that did not match anything.

## Example


## Defect reports


## See also


| cpp/utility/dsc from_chars_result | (see dedicated page) |
| cpp/utility/dsc to_chars | (see dedicated page) |
| cpp/string/basic_string/dsc stol | (see dedicated page) |
| cpp/string/basic_string/dsc stof | (see dedicated page) |
| cpp/string/byte/dsc strtol | (see dedicated page) |
| cpp/string/byte/dsc strtof | (see dedicated page) |
| cpp/io/c/dsc fscanf | (see dedicated page) |
| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |

