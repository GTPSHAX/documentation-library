---
title: std::chrono::operator<<(std::chrono::month_weekday_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_weekday_last/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::month_weekday_last& mwdl );
Outputs a textual representation of `mwdl` into `os`, as if by
cc|os << std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{:L}/{:L}"),
mwdl.month(), mwdl.weekday_last());
where c|STATICALLY_WIDEN<CharT>("{:L}/{:L}") is c|"{:L}/{:L}" if `CharT` is `char`, and c|L"{:L}/{:L}" if `CharT` is `wchar_t`.

## Return value

`os`

## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|month | (see dedicated page) |

