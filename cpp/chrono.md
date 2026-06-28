---
title: Date and time utilities
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono
---


# Date and time library

C++ includes support for two types of time manipulation:
* The , a flexible collection of types that track time with varying degrees of precision (e.g., `std::chrono::time_point`).
*  (e.g., `std::time`).

## Chrono library <sup>(C++11)</sup>

The `chrono` library defines several main types as well as utility functions and common typedefs:
*
* s
* s
rrev|since=c++20|
*  dates
*  information

### Clocks

A clock consists of a starting point (or epoch) and a tick rate. For example, a clock may have an epoch of January 1, 1970 and tick every second. C++ defines several clock types:


| chrono | |
| std::chrono | |
| cpp/chrono/dsc system_clock | (see dedicated page) |
| cpp/chrono/dsc steady_clock | (see dedicated page) |
| cpp/chrono/dsc high_resolution_clock | (see dedicated page) |
| cpp/chrono/dsc is_clock | (see dedicated page) |
| cpp/chrono/dsc utc_clock | (see dedicated page) |
| cpp/chrono/dsc tai_clock | (see dedicated page) |
| cpp/chrono/dsc gps_clock | (see dedicated page) |
| cpp/chrono/dsc file_clock | (see dedicated page) |
| cpp/chrono/dsc local_t | (see dedicated page) |


### Time point

A time point is a duration of time that has passed since the epoch of a specific clock.


| chrono | |
| std::chrono | |
| cpp/chrono/dsc time_point | (see dedicated page) |
| cpp/chrono/dsc clock_time_conversion | (see dedicated page) |
| cpp/chrono/dsc clock_cast | (see dedicated page) |


### Duration

A duration consists of a span of time, defined as some number of ticks of some time unit.  For example, "42 seconds" could be represented by a duration consisting of 42 ticks of a 1-second time unit.


| chrono | |
| std::chrono | |
| cpp/chrono/dsc duration | (see dedicated page) |


### Time of day <sup>(C++20)</sup>

`hh_mm_ss` splits a duration representing time elapsed since midnight into hours, minutes, seconds, and fractional seconds, as applicable. It is primarily a formatting tool.


| chrono | |
| std::chrono | |
| cpp/chrono/dsc hh_mm_ss | (see dedicated page) |
| cpp/chrono/dsc hour fun | (see dedicated page) |


### Calendar <sup>(C++20)</sup>


| chrono | |
| std::chrono | |
| cpp/chrono/dsc last_spec | (see dedicated page) |
| cpp/chrono/dsc day | (see dedicated page) |
| cpp/chrono/dsc month | (see dedicated page) |
| cpp/chrono/dsc year | (see dedicated page) |
| cpp/chrono/dsc weekday | (see dedicated page) |
| cpp/chrono/dsc weekday_indexed | (see dedicated page) |
| cpp/chrono/dsc weekday_last | (see dedicated page) |
| cpp/chrono/dsc month_day | (see dedicated page) |
| cpp/chrono/dsc month_day_last | (see dedicated page) |
| cpp/chrono/dsc month_weekday | (see dedicated page) |
| cpp/chrono/dsc month_weekday_last | (see dedicated page) |
| cpp/chrono/dsc year_month | (see dedicated page) |
| cpp/chrono/dsc year_month_day | (see dedicated page) |
| cpp/chrono/dsc year_month_day_last | (see dedicated page) |
| cpp/chrono/dsc year_month_weekday | (see dedicated page) |
| cpp/chrono/dsc year_month_weekday_last | (see dedicated page) |
| cpp/chrono/dsc operator/ | (see dedicated page) |


### Time zone <sup>(C++20)</sup>


| chrono | |
| std::chrono | |
| cpp/chrono/dsc tzdb | (see dedicated page) |
| cpp/chrono/dsc tzdb_list | (see dedicated page) |
| cpp/chrono/dsc tzdb functions | (see dedicated page) |
| cpp/chrono/dsc locate_zone | (see dedicated page) |
| cpp/chrono/dsc current_zone | (see dedicated page) |
| cpp/chrono/dsc time_zone | (see dedicated page) |
| cpp/chrono/dsc sys_info | (see dedicated page) |
| cpp/chrono/dsc local_info | (see dedicated page) |
| cpp/chrono/dsc choose | (see dedicated page) |
| cpp/chrono/dsc zoned_traits | (see dedicated page) |
| cpp/chrono/dsc zoned_time | (see dedicated page) |
| cpp/chrono/dsc leap_second | (see dedicated page) |
| cpp/chrono/utc_clock/dsc leap_second_info | (see dedicated page) |
| cpp/chrono/utc_clock/dsc get_leap_second_info | (see dedicated page) |
| cpp/chrono/dsc time_zone_link | (see dedicated page) |
| cpp/chrono/dsc nonexistent_local_time | (see dedicated page) |
| cpp/chrono/dsc ambiguous_local_time | (see dedicated page) |


### Literals <sup>(C++14)</sup>


| chrono | |
| std::literals::chrono_literals|inline=true | |
| cpp/chrono/dsc operator""y | (see dedicated page) |
| cpp/chrono/dsc operator""d | (see dedicated page) |
| cpp/chrono/dsc operator""h | (see dedicated page) |
| cpp/chrono/dsc operator""min | (see dedicated page) |
| cpp/chrono/dsc operator""s | (see dedicated page) |
| cpp/chrono/dsc operator""ms | (see dedicated page) |
| cpp/chrono/dsc operator""us | (see dedicated page) |
| cpp/chrono/dsc operator""ns | (see dedicated page) |


### Chrono I/O <sup>(C++20)</sup>


| chrono | |
| std::chrono | |
| cpp/chrono/dsc parse | (see dedicated page) |


## Notes


## C-style date and time library

Also provided are the C-style date and time functions, such as `std::time_t`, `std::difftime`, and `CLOCKS_PER_SEC`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

long Fibonacci(unsigned n)
{
    return n < 2 ? n : Fibonacci(n - 1) + Fibonacci(n - 2);
}

int main()
{
    // Measures and displays an execution time of a function call.
    const auto start{std::chrono::steady_clock::now()};
    const auto fb{Fibonacci(42)};
    const auto finish{std::chrono::steady_clock::now()};
    const std::chrono::duration<double> elapsed_seconds{finish - start};

    std::cout << "Fibonacci(42): " << fb << "\nElapsed time: ";
//  std::cout << elapsed_seconds.count() << "s\n"; // Before C++20
    std::cout << elapsed_seconds << '\n'; // C++20's chrono::duration operator<<

    // Prints UTC and local time.
    const auto tp_utc{std::chrono::system_clock::now()};
    std::cout << "Current time 'UTC' is: " << tp_utc << "\n"
                 "Current time 'Local' is: "
              << std::chrono::current_zone()->to_local(tp_utc) << '\n';
}
```


**Output:**
```
Fibonacci(42): 267914296
Elapsed time: 0.728532s
Current time 'UTC' is: 2025-02-10 06:22:39.420666960
Current time 'Local' is: 2025-02-10 09:22:39.420666960
```

