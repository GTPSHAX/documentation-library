---
title: std::chrono::operator<<(std::chrono::hh_mm_ss)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/hh_mm_ss/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits, class Duration >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::hh_mm_ss<Duration>& t );
Outputs `t` into the stream `os`.
Equivalent to } where } is } if `CharT` is `char`, and } if `CharT` is `wchar_t`.

## Parameters


### Parameters

- `os` - the output stream
- `t` - the time of day to be output

## Return value

`os`

## Example


## See also


| cpp/utility/format/dsc format | (see dedicated page) |
| cpp/chrono/dsc formatter|hh_mm_ss | (see dedicated page) |

