---
title: std::chrono::ceil(std::chrono::duration)
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/ceil
---

ddcl|since=c++17|header=chrono|
template< class ToDuration, class Rep, class Period >
constexpr ToDuration ceil( const std::chrono::duration<Rep, Period>& d );
Returns the smallest duration `t` representable in `ToDuration` that is greater or equal to `d`.
The function does not participate in the overload resolution unless `ToDuration` is a specialization of `std::chrono::duration`.

## Parameters


### Parameters

- `d` - duration to convert

## Return value

`d` rounded up to a duration of type `ToDuration`.

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
constexpr To ceil(const std::chrono::duration<Rep, Period>& d)
{
To t = std::chrono::duration_cast<To>(d);
if (t < d)
return t + To{1};
return t;
}

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono_literals;
    using Min = std::chrono::minutes;

    std::cout
        << std::showpos
        << "ceil(+2.4min) = " << std::chrono::ceil<Min>(+2.4min).count() << "min\n"
        << "ceil(-2.4min) = " << std::chrono::ceil<Min>(-2.4min).count() << "min\n"
        << "ceil(+0.0min) = " << std::chrono::ceil<Min>(+0.0min).count() << "min\n";
}
```


**Output:**
```
ceil(+2.4min) = +3min
ceil(-2.4min) = -2min
ceil(+0.0min) = +0min
```


## See also


| cpp/chrono/duration/dsc duration_cast | (see dedicated page) |
| cpp/chrono/duration/dsc floor | (see dedicated page) |
| cpp/chrono/duration/dsc round | (see dedicated page) |
| cpp/chrono/time_point/dsc ceil | (see dedicated page) |
| cpp/numeric/math/dsc ceil | (see dedicated page) |

