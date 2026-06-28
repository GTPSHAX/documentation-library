---
title: std::formatter<range>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/ranges_formatter
---


# formattersmall|<''range''>


```cpp
**Header:** `<`format`>`
dcl|since=c++23|1=
template< ranges::input_range R, class CharT >
requires (std::format_kind<R> != std::range_format::disabled) &&
std::formattable<ranges::range_reference_t<R>, CharT>
struct formatter<R, CharT>;
dcla|expos=yes|
template< std::range_format K, ranges::input_range R, class CharT >
struct /*range-default-formatter*/;
```

The template specialization of `std::formatter` for the range types allows users to convert a range to its textual representation as a collection of elements or a string using formatting functions.
The specialization is derived from .
The specialization is enabled if `R` satisfies , `std::format_kind<R>` is not `std::range_format::disabled`, and `std::formattable<ranges::range_reference_t<R>, CharT>` is `true`.
This specialization meets the *Formatter* requirements if `const R` models  and `ranges::range_reference_t<const R>` models `std::formattable<CharT>`. It always meets the *BasicFormatter* requirements.

## Format specification

The syntax of *range-format-spec* is:

**Syntax:**

- `sdsc|`
- `*range-fill-and-align* (optional) *width* (optional) **`n`** *range-type* (optional) *range-underlying-spec* (optional)`
The syntax is fully described in .
For specializations of `std::formatter` where `std::format_kind<R>` is either `std::range_format::string` or `std::range_format::debug_string`, the *format-spec* is *std-format-spec* instead of *range-format-spec* (which uses `std::formatter<std::basic_string<CharT>, CharT>` as the underlying formatter).

## Specializations of


| cpp/utility/format/ranges_formatter/dsc range_default_formatter_sequence | (see dedicated page) |
| cpp/utility/format/ranges_formatter/dsc range_default_formatter_map | (see dedicated page) |
| cpp/utility/format/ranges_formatter/dsc range_default_formatter_set | (see dedicated page) |
| cpp/utility/format/ranges_formatter/dsc range_default_formatter_string | (see dedicated page) |


## Example


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |

