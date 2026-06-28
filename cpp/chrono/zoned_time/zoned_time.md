---
title: std::chrono::zoned_time::zoned_time
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/zoned_time
---


```cpp
dcl|since=c++20|num=1|
zoned_time();
dcl|since=c++20|num=2|
zoned_time( const std::chrono::sys_time<Duration>& st );
dcl|since=c++20|num=3|1=
zoned_time( const zoned_time& other ) = default;
dcl|since=c++20|num=4|
template< class Duration2 >
zoned_time( const std::chrono::zoned_time<Duration2, TimeZonePtr>& other );
dcl|since=c++20|num=5|
explicit zoned_time( TimeZonePtr z );
dcl|since=c++20|num=6|
explicit zoned_time( std::string_view name );
dcl|since=c++20|num=7|
zoned_time( TimeZonePtr z, const std::chrono::sys_time<Duration>& st );
dcl|since=c++20|num=8|
zoned_time( std::string_view name, const std::chrono::sys_time<Duration>& st );
dcl|since=c++20|num=9|
zoned_time( TimeZonePtr z, const std::chrono::local_time<Duration>& tp );
dcl|since=c++20|num=10|
zoned_time( std::string_view name, const std::chrono::local_time<Duration>& tp );
dcl|since=c++20|num=11|
zoned_time( TimeZonePtr z, const std::chrono::local_time<Duration>& tp,
std::chrono::choose c );
dcl|since=c++20|num=12|
zoned_time( std::string_view name,
const std::chrono::local_time<Duration>& tp, std::chrono::choose c );
dcl|since=c++20|num=13|
template< class Duration2, class TimeZonePtr2 >
zoned_time( TimeZonePtr z,
const std::chrono::zoned_time<Duration2, TimeZonePtr2>& zt );
dcl|since=c++20|num=14|
template< class Duration2, class TimeZonePtr2 >
zoned_time( TimeZonePtr z,
const std::chrono::zoned_time<Duration2, TimeZonePtr2>& zt,
std::chrono::choose );
dcl|since=c++20|num=15|
template< class Duration2, class TimeZonePtr2 >
zoned_time( std::string_view name,
const std::chrono::zoned_time<Duration2, TimeZonePtr2>& zt );
dcl|since=c++20|num=16|
template< class Duration2, class TimeZonePtr2 >
zoned_time( std::string_view name,
const std::chrono::zoned_time<Duration2, TimeZonePtr2>& zt,
std::chrono::choose );
```

Constructs a `zoned_time` object, initializing the stored time zone pointer and time point according to the following table, where `traits` is `std::chrono::zoned_traits<TimeZonePtr>`:


| - |
| Overload |
| Time zone pointer (denoted tt | zone) |
| Time point (a c | std::chrono::sys_time<duration>) |
| Notes |
| - |
| v | 1 |
| rowspan="2" | c | traits::default_zone() |
| default constructed |
| rowspan="2" | v | a |
| - |
| v | 2 |
| tt | st |
| - |
| v | 3 |
| c | other.get_time_zone() |
| c | other.get_sys_time() |
| v | b |
| - |
| v | 4 |
| c | other.get_time_zone() |
| c | other.get_sys_time() |
| v | e |
| - |
| v | 5 |
| c | std::move(z) |
| rowspan="2" | default constructed |
|  |
| - |
| v | 6 |
| c | traits::locate_zone(name) |
| v | c |
| - |
| v | 7 |
| c | std::move(z) |
| rowspan="2" | tt | st |
|  |
| - |
| v | 8 |
| c | traits::locate_zone(name) |
| v | c |
| - |
| v | 9 |
| c | std::move(z) |
| rowspan="2" | c | zone->to_sys(tp) |
| v | d |
| - |
| v | 10 |
| c | traits::locate_zone(name) |
| v | c,d |
| - |
| v | 11 |
| c | std::move(z) |
| rowspan="2" | c | zone->to_sys(tp, c) |
| v | d |
| - |
| v | 12 |
| c | traits::locate_zone(name) |
| v | c,d |
| - |
| v | 13,14 |
| c | std::move(z) |
| rowspan="2" | c | zt.get_sys_time() |
| v | e |
| - |
| v | 15,16 |
| c | traits::locate_zone(name) |
| v | c,e |

@a@ Constructors specified to call `traits::default_zone()`  do not participate in overload resolution if that expression is not well-formed.
@b@ The defaulted copy constructor  is defined as deleted if `std::is_copy_constructible_v<TimeZonePtr>` is false.
@c@ Constructors with a `std::string_view` parameter `name`  do not participate in overload resolution if `traits::locate_zone(name)` is not well-formed or if that expression is not convertible to `TimeZonePtr`.
@d@ Constructors specified to call `zone->to_sys`  do not participate in overload resolution if that call expression is not well-formed or if the result is not convertible to `std::chrono::sys_time<duration>`.
@e@ Constructors with a template parameter `Duration2`  do not participate in overload resolution if `Duration2` is not convertible to `Duration`.
The behavior is undefined if the time zone pointer (initialized as described above) does not refer to a time zone.

## Notes

`zoned_time` does not have a move constructor and attempting to move one will perform a copy instead using the defaulted copy constructor . Thus, when `TimeZonePtr` is a move-only type, `zoned_time` is immovable: it can be neither moved nor copied.
The constructors  accept a `std::chrono::choose` parameter, but that parameter has no effect.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <string_view>

int main()
{
    using std::chrono_literals::operator""y;
    using std::operator""sv;

    std::cout << std::chrono::zoned_time{} << " : default\n";

    constexpr std::string_view location1{"America/Phoenix"sv};
    std::cout << std::chrono::zoned_time{location1} << " : " << location1 << '\n';

    const std::chrono::time_zone* timeZonePtr = std::chrono::locate_zone("UTC");
    std::cout << std::chrono::zoned_time{timeZonePtr} << " : UTC time zone\n";

    constexpr auto location2{"Europe/Rome"sv};
    std::cout << std::chrono::zoned_time{location2, std::chrono::local_days{2021y/12/31}<!---->}
              << " : " << location2 << '\n';

    constexpr auto location3{"Europe/Rome"sv};
    constexpr auto some_date = std::chrono::sys_time<std::chrono::days>{2021y/12/31};
    std::cout << std::chrono::zoned_time{location3, some_date}
              << " : " << location3 << '\n';

    const auto now =
        std::chrono::floor<std::chrono::minutes>(std::chrono::system_clock::now());
    constexpr auto location4{"Europe/Rome"sv};
    std::cout << std::chrono::zoned_time{location4, now} << " : " << location4 << '\n';

    constexpr auto NewYork{"America/New_York"sv};
    constexpr auto Tokyo{"Asia/Tokyo"sv};
    const std::chrono::zoned_time tz_Tokyo{Tokyo, now};
    const std::chrono::zoned_time tz_NewYork{NewYork, now};
    std::cout << std::chrono::zoned_time{Tokyo, tz_NewYork} << " : " << Tokyo << '\n';
    std::cout << std::chrono::zoned_time{NewYork, tz_Tokyo} << " : " << NewYork << '\n';
}
```


**Output:**
```
1970-01-01 00:00:00 UTC : default
1969-12-31 17:00:00 MST : America/Phoenix
1970-01-01 00:00:00 UTC : UTC time zone
2021-12-31 00:00:00 CET : Europe/Rome
2021-12-31 01:00:00 CET : Europe/Rome
2021-09-20 23:04:00 CEST : Europe/Rome
2021-09-21 06:04:00 JST : Asia/Tokyo
2021-09-20 17:04:00 EDT : America/New_York
```

