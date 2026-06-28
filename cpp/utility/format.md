---
title: Formatting library
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format
---


# Formatting library mark since c++20

The text formatting library offers a safe and extensible alternative to the printf family of functions. It is intended to complement the existing C++ I/O streams library.

## Format specifications

Format specification specifies how objects are formatted with different kinds of options.
The formatting of objects of basic types and standard string types uses the . Other library components may also provide their own format specifications, see  for details.

## Formatting functions


| format | |
| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/utility/format/dsc format_to | (see dedicated page) |
| cpp/utility/format/dsc format_to_n | (see dedicated page) |
| cpp/utility/format/dsc formatted_size | (see dedicated page) |


## Format strings


| format | |
| cpp/utility/format/dsc basic_format_string | (see dedicated page) |
| cpp/utility/format/dsc dynamic_format | (see dedicated page) |


## Formatting concepts


| format | |
| cpp/utility/format/dsc formattable | (see dedicated page) |


## Extensibility support and implementation detail


| format | |
| cpp/utility/format/dsc vformat | (see dedicated page) |
| cpp/utility/format/dsc vformat_to | (see dedicated page) |
| cpp/utility/format/dsc make_format_args | (see dedicated page) |
| cpp/utility/format/dsc visit_format_arg | (see dedicated page) |
| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |
| cpp/utility/format/dsc enable_nonlocking_formatter_optimization | (see dedicated page) |
| cpp/utility/format/dsc range_format | (see dedicated page) |
| cpp/utility/format/dsc format_kind | (see dedicated page) |
| cpp/utility/format/dsc basic_format_arg | (see dedicated page) |
| cpp/utility/format/dsc basic_format_args | (see dedicated page) |
| cpp/utility/format/dsc basic_format_context | (see dedicated page) |
| cpp/utility/format/dsc basic_format_parse_context | (see dedicated page) |
| cpp/utility/format/dsc format_error | (see dedicated page) |


## Helper items <sup>(C++23)</sup>


```cpp
dcla|num=1|anchor=const-formattable-range|expos=yes|1=
template< class R, class CharT >
concept /*const-formattable-range*/ =
ranges::input_range<const R> &&
std::formattable<ranges::range_reference_t<const R>, CharT>;
dcla|num=2|anchor=fmt-maybe-const|expos=yes|1=
template< class R, class CharT >
using /*fmt-maybe-const*/ =
std::conditional_t</*const-formattable-range*/<R, CharT>, const R, R>;
```


## Notes

We intentionally treat the addition of `std::basic_format_string` (`P2508`) as a defect report because all known implementations make these components available in C++20 mode, although it is not so categorized officially.

## Example


## Defect reports


## See also


| cpp/io/dsc print | (see dedicated page) |
| cpp/io/dsc println | (see dedicated page) |
| cpp/io/basic_ostream/dsc print | (see dedicated page) |

