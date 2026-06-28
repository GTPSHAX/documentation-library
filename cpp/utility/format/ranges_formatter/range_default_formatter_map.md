---
title: std::range-default-formatter<std::range_format::map>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/ranges_formatter/range_default_formatter_map
---


# ''range-default-formatter''small|<std::range_format::map>

ddcl|header=format|since=c++23|notes=|1=
template< ranges::input_range R, class CharT >
struct /*range-default-formatter*/<range_format::map, R, CharT>;
The class template `/*range-default-formatter*/` for range types is specialized for formatting range as a map of keys to values if `std::format_kind<R>` is `std::range_format::map`.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions

member|1=''range-default-formatter''|2=
ddcl|1=
constexpr /*range-default-formatter*/();
Equivalent to:<br>
c multi
|underlying_.set_brackets(STATICALLY_WIDEN<CharT>("{"), STATICALLY_WIDEN<CharT>("}"));
|underlying_.underlying().set_brackets({}, {});
|underlying_.underlying().set_separator(STATICALLY_WIDEN<charT>(": "));
where `STATICALLY_WIDEN<CharT>("...")` is `"..."` if `CharT` is `char`, and `L"..."` if `CharT` is `wchar_t`.
The program is ill-formed unless:
*  is a specialization of `std::pair`, or
*  is a specialization of `std::tuple` and `std::tuple_size_v<''element-type''>` is `2`.
member|1=parse|2=
ddcl|1=
template< class ParseContext >
constexpr auto parse( ParseContext& ctx ) -> ParseContext::iterator;
Equivalent to: .
Returns an iterator past the end of the ''range-format-spec''.
member|1=format|2=
ddcl|1=
template< class FormatContext >
auto format( maybe-const-map& r, FormatContext& ctx ) const -> FormatContext::iterator;
Equivalent to: .
Returns an iterator past the end of the output range.

## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |

