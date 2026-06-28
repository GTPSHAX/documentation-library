---
title: std::chrono::duration
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration
---

ddcl|header=chrono|since=c++11|1=
template<
class Rep,
class Period = std::ratio<1>
> class duration;
Class template `std::chrono::duration` represents a time interval.
It consists of a count of ticks of type `Rep` and a tick period, where the tick period is a compile-time rational `cpp/numeric/ratio/ratio|fraction` representing the time in seconds from one tick to the next.
The only data stored in a `duration` is a tick count of type `Rep`. If `Rep` is floating point, then the `duration` can represent fractions of ticks. `Period` is included as part of the duration's type, and is only used when converting between different durations.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/chrono/duration/dsc constructor | (see dedicated page) |
| cpp/chrono/duration/dsc operator{{= | (see dedicated page) |
| cpp/chrono/duration/dsc count | (see dedicated page) |
| cpp/chrono/duration/dsc zero | (see dedicated page) |
| cpp/chrono/duration/dsc min | (see dedicated page) |
| cpp/chrono/duration/dsc max | (see dedicated page) |
| cpp/chrono/duration/dsc operator arith | (see dedicated page) |
| cpp/chrono/duration/dsc operator arith2 | (see dedicated page) |
| cpp/chrono/duration/dsc operator arith3 | (see dedicated page) |


## Non-member functions


| cpp/chrono/duration/dsc operator arith4 | (see dedicated page) |
| cpp/chrono/duration/dsc operator cmp | (see dedicated page) |
| cpp/chrono/duration/dsc duration cast | (see dedicated page) |
| cpp/chrono/duration/dsc floor | (see dedicated page) |
| cpp/chrono/duration/dsc ceil | (see dedicated page) |
| cpp/chrono/duration/dsc round | (see dedicated page) |
| cpp/chrono/duration/dsc abs | (see dedicated page) |
| cpp/chrono/duration/dsc operator ltlt | (see dedicated page) |
| cpp/chrono/duration/dsc from_stream | (see dedicated page) |


## Helper types

A type `/* intXX */` used in the table below means a signed integer type of at least XX bits.


| Item | Description |
|------|-------------|
| **Type** | Definition |

Note: each of the predefined duration types up to `hours` covers a range of at least ±292 years.
<sup>(since C++20)</sup> Each of the predefined duration types `days`, `weeks`, `months` and `years` covers a range of at least ±40000 years. `years` is equal to 365.2425 `days` (the average length of a Gregorian year). `months` is equal to 30.436875 `days` (exactly 1/12 of `years`).

## Helper classes


| cpp/chrono/duration/dsc common_type | (see dedicated page) |
| cpp/chrono/dsc treat_as_floating_point | (see dedicated page) |
| cpp/chrono/dsc duration_values | (see dedicated page) |
| cpp/chrono/dsc formatter|duration | (see dedicated page) |
| cpp/chrono/duration|nested=true|notes= | |


## Helper specializations


```cpp
dcl|since=c++23|1=
template< class Rep, class Period >
constexpr bool enable_nonlocking_formatter_optimization<chrono::duration<Rep, Period>>
= enable_nonlocking_formatter_optimization<Rep>;
```

This specialization of  enables efficient implementation of  and  for printing a `chrono::duration` object when the template parameter `Rep` enables it.

## Literals


| std::literals::chrono_literals|inline=true | |
| cpp/chrono/dsc operator""h | (see dedicated page) |
| cpp/chrono/dsc operator""min | (see dedicated page) |
| cpp/chrono/dsc operator""s | (see dedicated page) |
| cpp/chrono/dsc operator""ms | (see dedicated page) |
| cpp/chrono/dsc operator""us | (see dedicated page) |
| cpp/chrono/dsc operator""ns | (see dedicated page) |

rrev|since=c++20|
Note: the literal suffixes `d` and `y` do not refer to `days` and `years` but to `cpp/chrono/day` and `cpp/chrono/year`, respectively.

## Notes

The actual time interval (in seconds) that is held by a duration object `d` is roughly equal to `1=d.count() * D::period::num / D::period::den`, where `D` is of type `chrono::duration<>` and `d` is an object of such type.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

using namespace std::chrono_literals;

template<typename T1, typename T2>
using mul = std::ratio_multiply<T1, T2>;

int main()
{
    using microfortnights = std::chrono::duration<float,
        mul<mul<std::ratio<2>, std::chrono::weeks::period>, std::micro>>;
    using nanocenturies = std::chrono::duration<float,
        mul<mul<std::hecto, std::chrono::years::period>, std::nano>>;
    using fps_24 = std::chrono::duration<double, std::ratio<1, 24>>;

    std::cout << "1 second is:\n";

    // integer scale conversion with no precision loss: no cast
    std::cout << std::chrono::milliseconds(1s).count() << " milliseconds\n"
              << std::chrono::microseconds(1s).count() << " microseconds\n"
              << std::chrono::nanoseconds(1s).count() << " nanoseconds\n";

    // integer scale conversion with precision loss: requires a cast
    std::cout << std::chrono::duration_cast<std::chrono::minutes>(1s).count()
              << " minutes\n";
    // alternative to duration_cast:
    std::cout << 1s / 1min << " minutes\n";

    // floating-point scale conversion: no cast
    std::cout << microfortnights(1s).count() << " microfortnights\n"
              << nanocenturies(1s).count() << " nanocenturies\n"
              << fps_24(1s).count() << " frames at 24fps\n";
}
```


**Output:**
```
1 second is:
1000 milliseconds
1000000 microseconds
1000000000 nanoseconds
0 minutes
0 minutes
0.82672 microfortnights
0.316887 nanocenturies
24 frames at 24fps
```

