---
title: std::chrono::operator<<(std::chrono::local_time)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/local_t/operator_ltlt
---


```cpp
dcl|since=c++20|
template< class CharT, class Traits, class Duration >
std::basic_ostream<CharT, Traits>&
operator<<( std::basic_ostream<CharT, Traits>& os,
const std::chrono::local_time<Duration>& tp );
```

Outputs `tp` into the stream `os`, as if by `os << std::chrono::sys_time<Duration>(tp.time_since_epoch());`.

## Return value

`os`

## See also


| cpp/chrono/time_point/dsc operator ltlt|sys_time|system_clock | (see dedicated page) |

