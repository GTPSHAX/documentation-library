---
title: std::chrono::round(std::chrono::time_point)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/round
---

ddcl|since=c++17|header=chrono|
template< class ToDuration, class Clock, class Duration >
constexpr std::chrono::time_point<Clock, ToDuration>
round( const std::chrono::time_point<Clock, Duration>& tp );
Returns the nearest time point to `tp` representable in `ToDuration`, rounding to even in halfway cases.
The function does not participate in the overload resolution unless `ToDuration` is a specialization of `std::chrono::duration` and `std::chrono::treat_as_floating_point_v<typename ToDuration::rep>` is `false`.

## Parameters


### Parameters

- `tp` - time point to round to nearest

## Return value

`tp` rounded to nearest time point using duration of type `ToDuration`, rounding to even in halfway cases.

## Possible implementation

eq fun|1=
namespace detail
{
template<class> inline constexpr bool is_duration_v = false;
template<class Rep, class Period> inline constexpr bool is_duration_v<
std::chrono::duration<Rep, Period>> = true;
}
template<class To, class Clock, class FromDuration,
class = std::enable_if_t<detail::is_duration_v<To> &&
!std::chrono::treat_as_floating_point_v<typename To::rep>>>
constexpr std::chrono::time_point<Clock, To> round(
const std::chrono::time_point<Clock, FromDuration>& tp)
{
return std::chrono::time_point<Clock, To>{
std::chrono::round<To>(tp.time_since_epoch())};
}

## Example


## See also


| cpp/chrono/time_point/dsc time_point_cast | (see dedicated page) |
| cpp/chrono/time_point/dsc ceil | (see dedicated page) |
| cpp/chrono/time_point/dsc floor | (see dedicated page) |
| cpp/chrono/duration/dsc round | (see dedicated page) |
| cpp/numeric/math/dsc round | (see dedicated page) |

