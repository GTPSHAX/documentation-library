---
title: std::chrono::operator<<(std::chrono::weekday_indexed)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_indexed/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::weekday_indexed& wdi );
Outputs a textual representation of `wdi` into the stream `os`, as if by:
cc|1=
if (wdi.index() >=1 && wdi.index() <= 5)
os << std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{:L}[{}]"),
wdi.weekday(), wdi.index());
else
os << std::format(os.getloc(), STATICALLY_WIDEN<CharT>("{:L}[{} is not a valid index]"),
wdi.weekday(), wdi.index());
where `STATICALLY_WIDEN<CharT>("...")` is `"..."` if `CharT` is `char`, and `L"..."` if `CharT` is `wchar_t`.

## Return value

`os`

## Defect reports


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|weekday | (see dedicated page) |

