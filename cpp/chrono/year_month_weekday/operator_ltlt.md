---
title: std::chrono::operator<<(std::chrono::year_month_weekday)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::year_month_weekday& ymwd );
Outputs a textual representation of `ymwd` into `os`, as if by
cc|
os << std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{}/{:L}/{:L}"),
ymwd.year(), ymwd.month(), ymwd.weekday_indexed());
where c|STATICALLY_WIDEN<CharT>("{}/{:L}/{:L}") is c|"{}/{:L}/{:L}" if `CharT` is `char`, and c|L"{}/{:L}/{:L}" if `CharT` is `wchar_t`.

## Return value

`os`

## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month_day | (see dedicated page) |

