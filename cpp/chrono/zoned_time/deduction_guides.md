---
title: Deduction guides for std::chrono::zoned_time
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/zoned_time/deduction_guides
---


# Deduction guides for tt|std::chrono::zoned_time


```cpp
dcl|since=c++20|num=1|
zoned_time() -> zoned_time<std::chrono::seconds>;
dcl|since=c++20|num=2|
template< class Duration >
zoned_time( std::chrono::sys_time<Duration> )
-> zoned_time<std::common_type_t<Duration, std::chrono::seconds>>;
dcl|since=c++20|num=3|
template< class TimeZonePtrOrName >
zoned_time( TimeZonePtrOrName&& ) -> zoned_time<std::chrono::seconds, /* see below */>;
dcl|since=c++20|num=4|
template< class TimeZonePtrOrName, class Duration >
zoned_time( TimeZonePtrOrName&&, std::chrono::sys_time<Duration> )
-> zoned_time<std::common_type_t<Duration, std::chrono::seconds>, /* see below */>;
dcl|since=c++20|num=5|1=
template< class TimeZonePtrOrName, class Duration >
zoned_time( TimeZonePtrOrName&&, std::chrono::local_time<Duration>,
std::chrono::choose = std::chrono::choose::earliest )
-> zoned_time<std::common_type_t<Duration, std::chrono::seconds>, /* see below */>;
dcl|since=c++20|num=6|1=
template< class TimeZonePtrOrName, class Duration, class TimeZonePtr2 >
zoned_time( TimeZonePtrOrName&&, std::chrono::zoned_time<Duration, TimeZonePtr2>,
std::chrono::choose = std::chrono::choose::earliest )
-> zoned_time<std::common_type_t<Duration, std::chrono::seconds>, /* see below */>;
```

These deduction guides normalize `Duration` to a minimum resolution of `std::chrono::seconds`, and provide correct handling for time zone names specified using types convertible to `std::string_view`.
@3-6@ If `std::is_convertible_v<TimeZonePtrOrName, std::string_view>` is `true`, the deduced second template argument is `const std::chrono::time_zone*`. Otherwise it is `std::remove_cvref_t<TimeZonePtrOrName>`.
