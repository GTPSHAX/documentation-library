---
title: std::range-default-formatter<std::range_format::sequence>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/ranges_formatter/range_default_formatter_sequence
---


# ''range-default-formatter''small|<std::range_format::sequence>

ddcl|header=format|since=c++23|notes=|
template< ranges::input_range R, class CharT >
struct /*range-default-formatter*/<range_format::sequence, R, CharT>;
The class template `/*range-default-formatter*/` for range types is specialized for formatting range as a sequence of elements if `std::format_kind<R>` is `std::range_format::sequence`.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| dsc expos mem obj|private=yes|underlying_|the underlying formatter|spec= | |


## Member functions

member|1=set_separator|2=
ddcl|1=
constexpr void set_separator( std::basic_string_view<CharT> sep ) noexcept;
Equivalent to a call to `underlying_.set_separator(sep)`.
member|1=set_brackets|2=
ddcl|1=
constexpr void set_brackets( std::basic_string_view<CharT> opening,
std::basic_string_view<CharT> closing ) noexcept;
Equivalent to a call to `underlying_.set_brackets(opening, closing)`.
member|1=parse|2=
ddcl|1=
template< class ParseContext >
constexpr auto parse( ParseContext& ctx ) -> ParseContext::iterator;
Equivalent to `return underlying_.parse(ctx);`.
Returns an iterator past the end of the ''range-format-spec''.
member|1=format|2=
ddcl|1=
template< class FormatContext >
auto format( /*maybe-const-r*/& elems, FormatContext& ctx ) const -> FormatContext::iterator;
Equivalent to `return underlying_.format(elems, ctx);`.
Returns an iterator past the end of the output range.

## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |

