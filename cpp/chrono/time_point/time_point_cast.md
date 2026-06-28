---
title: std::chrono::time_point_cast
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/time_point_cast
---


```cpp
**Header:** `<`chrono`>`
dcl rev multi
|since1=c++11|dcl1=
template< class ToDuration, class Clock, class Duration >
std::chrono::time_point<Clock, ToDuration>
time_point_cast( const std::chrono::time_point<Clock, Duration> &t );
|since2=c++14|dcl2=
template< class ToDuration, class Clock, class Duration >
constexpr std::chrono::time_point<Clock, ToDuration>
time_point_cast( const std::chrono::time_point<Clock, Duration> &t );
```

Converts a `std::chrono::time_point` from one duration to another.
`time_point_cast` participates in overload resolution only if `ToDuration` is a specialization of `std::chrono::duration`.

## Parameters


### Parameters

- `t` - `time_point` to convert from

## Return value

c|std::chrono::time_point<Clock, ToDuration>(
std::chrono::duration_cast<ToDuration>(t.time_since_epoch())).

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono_literals;

using Clock = std::chrono::high_resolution_clock;
using Ms = std::chrono::milliseconds;
using Sec = std::chrono::seconds;

template<class Duration>
using TimePoint = std::chrono::time_point<Clock, Duration>;

inline void print_ms(const TimePoint<Ms>& time_point)
{
    std::cout << time_point.time_since_epoch().count() << " ms\n";
}

int main()
{
    TimePoint<Sec> time_point_sec{4s};

    // implicit conversion, no precision loss
    TimePoint<Ms> time_point_ms = time_point_sec;
    print_ms(time_point_ms); // 4000 ms

    time_point_ms = TimePoint<Ms>{5756ms};
    print_ms(time_point_ms); // 5756 ms

    // explicit cast, need when precision loss may happen
    // 5756 truncated to 5000
    time_point_sec = std::chrono::time_point_cast<Sec>(time_point_ms);
    print_ms(time_point_sec); // 5000 ms
}
```


**Output:**
```
4000 ms
5756 ms
5000 ms
```


## See also


| cpp/chrono/time_point/dsc floor | (see dedicated page) |
| cpp/chrono/time_point/dsc ceil | (see dedicated page) |
| cpp/chrono/time_point/dsc round | (see dedicated page) |
| cpp/chrono/duration/dsc duration_cast | (see dedicated page) |

