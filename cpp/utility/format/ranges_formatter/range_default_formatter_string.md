---
title: std::range-default-formatter<std::range_format::string>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/ranges_formatter/range_default_formatter_string
---


# ''range-default-formatter''small|<std::range_format::string>

|''range-default-formatter''
ddcl|header=format|since=c++23|notes=|1=
template< std::range_format K, ranges::input_range R, class CharT >
requires (K == std::range_format::string  K == std::range_format::debug_string)
struct /*range-default-formatter*/<K, R, CharT>;
The class template `/*range-default-formatter*/` for range types is specialized for formatting range as a string or an escaped string if `std::format_kind<R>` is either `std::range_format::string` or `std::range_format::debug_string`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions

member|1=parse<br>parse|2=
ddcl|1=
template< class ParseContext >
constexpr auto parse( ParseContext& ctx ) -> ParseContext::iterator;
Equivalent to:
c multi|
auto i  underlying_.parse(ctx);|
if constexpr (K  std::range_format::debug_string)|
underlying_.set_debug_format();|
return i;
Returns an iterator past the end of the ''std-format-spec''.
member|1=format<br>format|2=
ddcl|1=
template< class FormatContext >
auto format( /* see below */& r, FormatContext& ctx ) const -> FormatContext::iterator;
If `ranges::input_range<const R>` is `true`, the type of `r` is `const R&`. Otherwise, the type is `R&`.
Let `s` be a `std::basic_string<CharT>` as if by constructing `s` with `std::basic_string<CharT>(std::from_range, r)` such that `ranges::equal(s, r)` is `true`.
Equivalent to `return underlying_.format(s, ctx);`.
Returns an iterator past the end of the output range.

## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |

