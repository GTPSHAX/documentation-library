---
title: std::chrono::operator<<(std::chrono::year_month_day_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_day_last/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::year_month_day_last& ymdl );
Outputs a textual representation of `ymdl` into `os`, as if by
cc|os << std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{}/{:L}"),
ymdl.year(), ymdl.month_day_last());
where c|STATICALLY_WIDEN<CharT>("{}/{:L}") is c|"{}/{:L}" if `CharT` is `char`, and c|L"{}/{:L}" if `CharT` is `wchar_t`.

## Return value

`os`

## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month_day | (see dedicated page) |

