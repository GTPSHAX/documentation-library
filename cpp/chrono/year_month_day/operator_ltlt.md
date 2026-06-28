---
title: std::chrono::operator<<(std::chrono::year_month_day)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_day/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::year_month_day& ymd );
Outputs a textual representation of `ymd` into the stream `os`. This first forms a `std::basic_string<CharT> s` consisting of a textual representation of the date in the format `yyyy-mm-dd` (same as the one output by `cpp/chrono/year_month_day/formatter` with the %F specifier). Then, if `!ymd.ok()`, appends `" is not a valid date"` to `s`. Inserts `s` into `os`.
Equivalent to
cc|
return os << (ymd.ok() ?
std::format(STATICALLY_WIDEN<CharT>("{:%F}"), ymd) :
std::format(STATICALLY_WIDEN<CharT>("{:%F} is not a valid date"), ymd));
where `STATICALLY_WIDEN<CharT>("...")` is `"..."` if `CharT` is `char`, and `L"..."` if `CharT` is `wchar_t`.

## Return value

`os`

## Example

