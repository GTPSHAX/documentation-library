---
title: std::chrono::operator<<(std::chrono::zoned_time)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/operator_ltlt
---

ddcl|header=chrono|since=c++20|
template< class CharT, class Traits, class Duration, class TimeZonePtr >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::zoned_time<Duration, TimeZonePtr>& tp );
Outputs `tp` to the stream `os`, as if by `std::format(os.getloc(), fmt, tp)`, where `fmt` is } if `CharT` is `char`, or } if `CharT` is `wchar_t`.

## Parameters


### Parameters

- `os` - output stream
- `tp` - `zoned_time` to output

## Return value

`os`

## Example


## See also


| cpp/chrono/dsc formatter|zoned_time | (see dedicated page) |

