---
title: std::range-default-formatter<std::range_format::set>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/ranges_formatter/range_default_formatter_set
---


# ''range-default-formatter''small|<std::range_format::set>

ddcl|header=format|since=c++23|notes=|
template< ranges::input_range R, class CharT >
struct /*range-default-formatter*/<range_format::set, R, CharT>;
The class template `/*range-default-formatter*/` for range types is specialized for formatting range as a set of keys if `std::format_kind<R>` is `std::range_format::set`.

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc expos mem obj|private=yes|underlying_|the underlying formatter of type: | |


## Member functions

member|1=''range-default-formatter''|2=
ddcl|1=
constexpr /*range-default-formatter*/();
Equivalent to a call to }
where `STATICALLY_WIDEN<CharT>("...")` is `"..."` if `CharT` is `char`, and `L"..."` if `CharT` is `wchar_t`.
member|1=parse|2=
ddcl|1=
template< class ParseContext >
constexpr auto parse( ParseContext& ctx ) -> ParseContext::iterator;
Equivalent to `return underlying_.parse(ctx);`.
Returns an iterator past the end of the ''range-format-spec''.
member|1=format|2=
ddcl|1=
template< class FormatContext >
auto format( maybe-const-set& r, FormatContext& ctx ) const -> FormatContext::iterator;
Equivalent to `return underlying_.format(r, ctx);`.
Returns an iterator past the end of the output range.

## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |
| cpp/utility/format/dsc range_formatter | (see dedicated page) |

