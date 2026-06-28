---
title: std::regex_traits
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_traits
---

ddcl|header=regex|since=c++11|1=
template< class CharT >
class regex_traits;
The type trait template `regex_traits` supplies `std::basic_regex` with the set of types and functions necessary to operate on the type `CharT`.
Since many of regex operations are locale-sensitive (when `std::regex_constants::collate` flag is set), the regex_traits class typically holds an instance of a `std::locale` as a private member.

## Standard specializations

Two specializations of `std::regex_traits` are defined by the standard library:
These specializations make it possible to use `std::basic_regex<char>` (aka `std::regex`) and `std::basic_regex<wchar_t>` (aka `std::wregex`). To use `std::basic_regex` with other character types (for example, `char32_t`), a user-provided trait class must be used.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/regex/regex_traits/dsc constructor | (see dedicated page) |
| cpp/regex/regex_traits/dsc length | (see dedicated page) |
| cpp/regex/regex_traits/dsc translate | (see dedicated page) |
| cpp/regex/regex_traits/dsc translate_nocase | (see dedicated page) |
| cpp/regex/regex_traits/dsc transform | (see dedicated page) |
| cpp/regex/regex_traits/dsc transform_primary | (see dedicated page) |
| cpp/regex/regex_traits/dsc lookup_collatename | (see dedicated page) |
| cpp/regex/regex_traits/dsc lookup_classname | (see dedicated page) |
| cpp/regex/regex_traits/dsc isctype | (see dedicated page) |
| cpp/regex/regex_traits/dsc value | (see dedicated page) |
| cpp/regex/regex_traits/dsc imbue | (see dedicated page) |
| cpp/regex/regex_traits/dsc getloc | (see dedicated page) |

