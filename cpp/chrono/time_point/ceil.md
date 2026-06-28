---
title: std::chrono::ceil(std::chrono::time_point)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/ceil
---

ddcl|since=c++17|header=chrono|
template< class ToDuration, class Clock, class Duration >
constexpr std::chrono::time_point<Clock, ToDuration>
ceil( const std::chrono::time_point<Clock, Duration>& tp );
Returns the smallest time point `t` representable in `ToDuration` that is greater or equal to `tp`.
The function does not participate in the overload resolution unless `ToDuration` is a specialization of `std::chrono::duration`.

## Parameters


### Parameters

- `tp` - time point to round up

## Return value

`tp` rounded up to the next time point using duration of type `ToDuration`.

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
ceil(const std::chrono::time_point<Clock, FromDuration>& tp)
{
return std::chrono::time_point<Clock, To>{
std::chrono::ceil<To>(tp.time_since_epoch())};
}

## Example


## See also


| cpp/chrono/time_point/dsc time_point_cast | (see dedicated page) |
| cpp/chrono/time_point/dsc floor | (see dedicated page) |
| cpp/chrono/time_point/dsc round | (see dedicated page) |
| cpp/chrono/duration/dsc ceil | (see dedicated page) |
| cpp/numeric/math/dsc ceil | (see dedicated page) |

