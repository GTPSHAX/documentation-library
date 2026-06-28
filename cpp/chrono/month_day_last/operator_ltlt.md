---
title: std::chrono::operator<<(std::chrono::month_day_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/month_day_last/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::month_day_last& mdl );
Outputs a textual representation of `mdl` into `os`, as if by
}
where } is } if `CharT` is `char`, and } if `CharT` is `wchar_t`.

## Return value

`os`

## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|month_day | (see dedicated page) |

