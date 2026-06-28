---
title: std::chrono::clock_time_conversion
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/clock_time_conversion
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|1=
template< class Dest, class Source >
struct clock_time_conversion {};
```

`std::chrono::clock_time_conversion` is a trait that specifies how to convert a `std::chrono::time_point` of the `Source` clock to that of the `Dest` clock. It does so by providing a const-callable `operator()` that accepts an argument of type `std::chrono::time_point<Source, Duration>` and returns a `std::chrono::time_point<Dest, OtherDuration>` that represents an equivalent point in time. The duration of the returned time point is computed from the source duration in a manner that varies for each specialization. `clock_time_conversion` is normally only used indirectly, via `std::chrono::clock_cast`.
A program may specialize `clock_time_conversion` if at least one of the template parameters is a user-defined clock type.
The primary template is an empty struct. The standard defines the following specializations:

```cpp
dcl|since=c++20|num=1|1=
template< class Clock >
struct clock_time_conversion<Clock, Clock>;
dcl|since=c++20|num=2|1=
template<>
struct clock_time_conversion<std::chrono::system_clock, std::chrono::system_clock>;
dcl|since=c++20|num=3|1=
template<>
struct clock_time_conversion<std::chrono::utc_clock, std::chrono::utc_clock>;
dcl|since=c++20|num=4|1=
template<>
struct clock_time_conversion<std::chrono::system_clock, std::chrono::utc_clock>;
dcl|since=c++20|num=5|1=
template<>
struct clock_time_conversion<std::chrono::utc_clock, std::chrono::system_clock>;
dcl|since=c++20|num=6|1=
template< class Clock >
struct clock_time_conversion<Clock, std::chrono::system_clock>;
dcl|since=c++20|num=7|1=
template< class Clock >
struct clock_time_conversion<std::chrono::system_clock, Clock>;
dcl|since=c++20|num=8|1=
template< class Clock >
struct clock_time_conversion<Clock, std::chrono::utc_clock>;
dcl|since=c++20|num=9|1=
template< class Clock >
struct clock_time_conversion<std::chrono::utc_clock, Clock>;
```

@1-3@ Identity conversion: `operator()` returns a copy of the argument.
@4,5@ Conversions between `std::chrono::sys_time` and `std::chrono::utc_time`: `operator()` calls `std::chrono::utc_clock::to_sys` and `std::chrono::utc_clock::from_sys`, respectively.
@6,7@ Conversions to and from `std::chrono::sys_time` when `Clock` supports `from_sys` and `to_sys`: `operator()` calls `Clock::to_sys` and `Clock::from_sys`, respectively.
@8,9@ Conversions to and from `std::chrono::utc_time` when `Clock` supports `from_utc` and `to_utc`: `operator()` calls `Clock::to_utc` and `Clock::from_utc`, respectively.

## Member functions

Each specialization has an implicitly-declared default constructor, copy constructor, move constructor, copy assignment operator, move assignment operator, and destructor.
member|operator()|2=

```cpp
|1=
template< class Duration >
std::chrono::time_point<Clock, Duration>
operator()( const std::chrono::time_point<Clock, Duration>& t ) const;
|1=
template< class Duration >
std::chrono::sys_time<Duration>
operator()( const std::chrono::sys_time<Duration> & t ) const;
|1=
template< class Duration >
std::chrono::utc_time<Duration>
operator()( const std::chrono::utc_time<Duration>& t ) const;
|1=
template< class Duration >
std::chrono::sys_time<Duration>
operator()( const std::chrono::utc_time<Duration>& t ) const;
|1=
template< class Duration >
std::chrono::utc_time<Duration>
operator()( const std::chrono::sys_time<Duration>& t ) const;
|1=
template< class Duration >
auto operator()( const std::chrono::sys_time<Duration>& t ) const
-> decltype(Clock::from_sys(t));
|1=
template< class Duration >
auto operator()( const std::chrono::time_point<SourceClock, Duration>& t ) const
-> decltype(Clock::to_sys(t));
|1=
template< class Duration >
auto operator()( const std::chrono::utc_time<Duration>& t ) const
-> decltype(Clock::from_utc(t));
|1=
template< class Duration >
auto operator()( const std::chrono::time_point<Clock, Duration>& t ) const
-> decltype(Clock::to_utc(t));
```

Converts the argument `std::chrono::time_point` to the destination clock.
@1-3@ Identity conversion. Returns `t` unchanged.
4. Returns `std::chrono::utc_clock::to_sys(t)`.
5. Returns `std::chrono::utc_clock::from_sys(t)`.
6. Returns `Clock::from_sys(t)`. . The program is ill-formed if `Clock::from_sys(t)` does not return `std::chrono::time_point<Clock, Duration>` where `Duration` is some valid specialization of `std::chrono::duration`.
7. Returns `Clock::to_sys(t)`. . The program is ill-formed if `Clock::to_sys(t)` does not return `std::chrono::sys_time<Duration>` where `Duration` is some valid specialization of `std::chrono::duration`.
8. Returns `Clock::from_utc(t)`. . The program is ill-formed if `Clock::from_utc(t)` does not return `std::chrono::time_point<Clock, Duration>` where `Duration` is some valid specialization of `std::chrono::duration`.
9. Returns `Clock::to_utc(t)`. . The program is ill-formed if `Clock::to_utc(t)` does not return `std::chrono::utc_time<Duration>` where `Duration` is some valid specialization of `std::chrono::duration`.

## Parameters


### Parameters

- `t` - time point to convert

## Return value

The result of the conversion as described above:
@1-3@ `t`.
4. `std::chrono::utc_clock::to_sys(t)`.
5. `std::chrono::utc_clock::from_sys(t)`.
6. `Clock::from_sys(t)`.
7. `Clock::to_sys(t)`.
8. `Clock::from_utc(t)`.
9. `Clock::to_utc(t)`.

## See also


| cpp/chrono/dsc clock_cast | (see dedicated page) |

