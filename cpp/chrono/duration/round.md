---
title: std::chrono::round(std::chrono::duration)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/round
---

ddcl|since=c++17|header=chrono|
template< class ToDuration, class Rep, class Period >
constexpr ToDuration round( const std::chrono::duration<Rep, Period>& d );
Returns the value `t` representable in `ToDuration` that is the closest to `d`. If there are two such values, returns the even value (that is, the value `t` such that `1=t % 2 == 0`).
The function does not participate in the overload resolution unless `ToDuration` is a specialization of `std::chrono::duration` and `std::chrono::treat_as_floating_point_v<typename ToDuration::rep>` is `false`.

## Parameters


### Parameters

- `d` - duration to convert

## Return value

`d` rounded to the nearest duration of type `ToDuration`, rounding to even in halfway cases.

## Possible implementation

eq fun|1=
namespace detail
{
template<class> inline constexpr bool is_duration_v = false;
template<class Rep, class Period> inline constexpr bool is_duration_v<
std::chrono::duration<Rep, Period>> = true;
}
template<class To, class Rep, class Period,
class = std::enable_if_t<detail::is_duration_v<To> &&
!std::chrono::treat_as_floating_point_v<typename To::rep>>>
constexpr To round(const std::chrono::duration<Rep, Period>& d)
{
To t0 = std::chrono::floor<To>(d);
To t1 = t0 + To{1};
auto diff0 = d - t0;
auto diff1 = t1 - d;
if (diff0 == diff1)
{
if (t0.count() & 1)
return t1;
return t0;
}
else if (diff0 < diff1)
return t0;
return t1;
}

## Example


## See also


| cpp/chrono/duration/dsc duration_cast | (see dedicated page) |
| cpp/chrono/duration/dsc floor | (see dedicated page) |
| cpp/chrono/duration/dsc ceil | (see dedicated page) |
| cpp/chrono/time_point/dsc round | (see dedicated page) |
| cpp/numeric/math/dsc round | (see dedicated page) |

