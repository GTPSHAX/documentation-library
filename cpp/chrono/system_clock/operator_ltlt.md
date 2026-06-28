---
title: std::chrono::operator<<(std::chrono::sys_time)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/system_clock/operator_ltlt
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|
template< class CharT, class Traits, class Duration >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::sys_time<Duration>& tp );
dcl|since=c++20|num=2|
template< class CharT, class Traits, class Duration >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::sys_days& tp );
```

Outputs `tp` into the stream `os`.
1. Equivalent to:

```cpp
return os << std::format(os.getloc(), STATICALLY-WIDEN<CharT>("{:L%F %T}"), tp);
```

where } is } if `CharT` is `char`, and } if `CharT` is `wchar_t`.<br>
.
2. Equivalent to `os << std::chrono::year_month_day(tp);`.

## Return value

`os`

## Defect reports


## See also


| cpp/chrono/dsc formatter|sys_time|system_clock | (see dedicated page) |
| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/year_month_day/dsc operator ltlt | (see dedicated page) |

