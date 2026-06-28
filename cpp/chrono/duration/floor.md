---
title: std::chrono::floor(std::chrono::duration)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/floor
---

ddcl|since=c++17|header=chrono|
template< class ToDuration, class Rep, class Period >
constexpr ToDuration floor( const std::chrono::duration<Rep, Period>& d );
Returns the greatest duration `t` representable in `ToDuration` that is less or equal to `d`.
The function does not participate in the overload resolution unless `ToDuration` is a specialization of `std::chrono::duration`.

## Parameters


### Parameters

- `d` - duration to convert

## Return value

`d` rounded down to a duration of type `ToDuration`.

## Possible implementation

eq fun|1=
namespace detail
{
template<class> inline constexpr bool is_duration_v = false;
template<class Rep, class Period> inline constexpr bool is_duration_v<
std::chrono::duration<Rep, Period>> = true;
}
template<class To, class Rep, class Period,
class = std::enable_if_t<detail::is_duration_v<To>>>
constexpr To floor(const duration<Rep, Period>& d)
{
To t = std::chrono::duration_cast<To>(d);
if (t > d)
return t - To{1};
return t;
}

## Example


## See also


| cpp/chrono/duration/dsc duration_cast | (see dedicated page) |
| cpp/chrono/duration/dsc ceil | (see dedicated page) |
| cpp/chrono/duration/dsc round | (see dedicated page) |
| cpp/chrono/time_point/dsc floor | (see dedicated page) |
| cpp/numeric/math/dsc floor | (see dedicated page) |

