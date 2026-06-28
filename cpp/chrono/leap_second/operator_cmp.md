---
title: std::chrono::operators (std::chrono::leap_second)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/leap_second/operator_cmp
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|num=1|1=
constexpr bool operator==( const std::chrono::leap_second& x,
const std::chrono::leap_second& y ) noexcept;
dcl|since=c++20|num=2|1=
constexpr std::strong_ordering operator<=>( const std::chrono::leap_second& x,
const std::chrono::leap_second& y ) noexcept;
dcl|since=c++20|num=3|1=
template< class Duration >
constexpr bool operator==( const std::chrono::leap_second& x,
const std::chrono::sys_time<Duration>& y ) noexcept;
dcl|since=c++20|num=4|1=
template< class Duration >
constexpr bool operator< ( const std::chrono::leap_second& x,
const std::chrono::sys_time<Duration>& y ) noexcept;
dcl|since=c++20|num=5|1=
template< class Duration >
constexpr bool operator< ( const std::chrono::sys_time<Duration>& x,
const std::chrono::leap_second& y ) noexcept;
dcl|since=c++20|num=6|1=
template< class Duration >
constexpr bool operator> ( const std::chrono::leap_second& x,
const std::chrono::sys_time<Duration>& y ) noexcept;
dcl|since=c++20|num=7|1=
template< class Duration >
constexpr bool operator> ( const std::chrono::sys_time<Duration>& x,
const std::chrono::leap_second& y ) noexcept;
dcl|since=c++20|num=8|1=
template< class Duration >
constexpr bool operator<=( const std::chrono::leap_second& x,
const std::chrono::sys_time<Duration>& y ) noexcept;
dcl|since=c++20|num=9|1=
template< class Duration >
constexpr bool operator<=( const std::chrono::sys_time<Duration>& x,
const std::chrono::leap_second& y ) noexcept;
dcl|since=c++20|num=10|1=
template< class Duration >
constexpr bool operator>=( const std::chrono::leap_second& x,
const std::chrono::sys_time<Duration>& y ) noexcept;
dcl|since=c++20|num=11|1=
template< class Duration >
constexpr bool operator>=( const std::chrono::sys_time<Duration>& x,
const std::chrono::leap_second& y ) noexcept;
dcl|since=c++20|num=12|1=
template< class Duration >
requires std::three_way_comparable_with<
std::chrono::sys_seconds, std::chrono::sys_time<Duration>>
constexpr auto operator<=>( const std::chrono::leap_second& x,
const std::chrono::sys_time<Duration>& y ) noexcept;
```

Compares the date and time represented by the objects `x` and `y`.
Return type of  is deduced from `1=x.date() <=> y`, and hence the three-way comparison result type of `std::chrono::seconds` and `Duration`.

## Return value

1. `1=x.date() == y.date()`
2. `1=x.date() <=> y.date()`
3. `1=x.date() == y`
4. `1=x.date() < y`
5. `1=x < y.date()`
6. `1=x.date() > y`
7. `1=x > y.date()`
8. `1=x.date() <= y`
9. `1=x <= y.date()`
10. `1=x.date() >= y`
11. `1=x >= y.date()`
12. `1=x.date() <=> y`
