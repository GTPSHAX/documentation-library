---
title: std::chrono::floor(std::chrono::time_point)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/floor
---

ddcl|since=c++17|header=chrono|
template< class ToDuration, class Clock, class Duration >
constexpr std::chrono::time_point<Clock, ToDuration>
floor( const std::chrono::time_point<Clock, Duration>& tp );
Returns the largest time point `t` representable in `ToDuration` that is smaller or equal to `tp`.
The function does not participate in the overload resolution unless `ToDuration` is a specialization of `std::chrono::duration`.

## Parameters


### Parameters

- `tp` - time point to round down

## Return value

`tp` rounded down to the next time point using duration of type `ToDuration`.

## Possible implementation

eq fun|1=
namespace detail
{
template<class> inline constexpr bool is_duration_v = false;
template<class Rep, class Period> inline constexpr bool is_duration_v<
std::chrono::duration<Rep, Period>> = true;
}
template<class To, class Clock, class FromDuration,
class = std::enable_if_t<detail::is_duration_v<To>>>
constexpr std::chrono::time_point<Clock, To>
floor(const std::chrono::time_point<Clock, FromDuration>& tp)
{
return std::chrono::time_point<Clock, To>{
std::chrono::floor<To>(tp.time_since_epoch())};
}

## Example


## See also


| cpp/chrono/time_point/dsc time_point_cast | (see dedicated page) |
| cpp/chrono/time_point/dsc ceil | (see dedicated page) |
| cpp/chrono/time_point/dsc round | (see dedicated page) |
| cpp/chrono/duration/dsc floor | (see dedicated page) |
| cpp/numeric/math/dsc floor | (see dedicated page) |

