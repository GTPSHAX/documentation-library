---
title: std::chrono::operator<<(std::chrono::weekday_last)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_last/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os, const std::chrono::weekday_last& wdl );
Outputs a textual representation of `wdl` into the stream `os`, as if by
}
where } is } if `CharT` is `char`, and } if `CharT` is `wchar_t`.

## Return value

`os`

## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|weekday | (see dedicated page) |

