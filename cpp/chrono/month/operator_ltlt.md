---
title: std::chrono::operator<<(std::chrono::month)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os, const std::chrono::month& m );
If `!m.ok()`, inserts `unsigned(m)` followed by `" is not a valid month"` to `os`. Otherwise, forms a `std::basic_string<CharT>` `s` consisting of the abbreviated month name for the month represented by `m`, determined using the locale associated with `os`, and inserts `s` into `os`.
Equivalent to
cc|
return os << (m.ok() ?
std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{:L%b}"), m) :
std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{} is not a valid month"), unsigned(m)));
where `STATICALLY_WIDEN<CharT>("...")` is `"..."` if `CharT` is `char`, and `L"..."` if `CharT` is `wchar_t`.

## Return value

`os`

## Notes

This `operator<<` is primarily intended for debugging use. For control over formatting, use `std::format`.

## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|month | (see dedicated page) |

