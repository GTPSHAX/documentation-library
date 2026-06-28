---
title: std::chrono::operator<<(std::chrono::year_month)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os, const std::chrono::year_month& ym );
Outputs a textual representation of `ym` into the stream `os`, as if by
cc|os << std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{}/{:L}"), ym.year(), ym.month())
where c|STATICALLY_WIDEN<CharT>("{}/{:L}") is c|"{}/{:L}" if `CharT` is `char`, and c|L"{}/{:L}" if `CharT` is `wchar_t`.

## Return value

`os`

## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|year_month | (see dedicated page) |

