---
title: std::chrono::time_point
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point
---

ddcl|header=chrono|since=c++11|1=
template<
class Clock,
class Duration = typename Clock::duration
> class time_point;
Class template `std::chrono::time_point` represents a point in time. It is implemented as if it stores a value of type `Duration` indicating the time interval from the start of the `Clock`'s epoch.
<sup>(since C++20)</sup> or be `std::chrono::local_t`.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Description |


## Member functions


| cpp/chrono/time_point/dsc constructor | (see dedicated page) |
| cpp/chrono/time_poind/dsc time_since_epoch | (see dedicated page) |
| cpp/chrono/time_point/dsc operator_arith | (see dedicated page) |
| cpp/chrono/time_point/dsc operator_inc_dec | (see dedicated page) |
| cpp/chrono/time_point/dsc min | (see dedicated page) |
| cpp/chrono/time_point/dsc max | (see dedicated page) |


## Non-member functions


| cpp/chrono/time_point/dsc operator_arith2 | (see dedicated page) |
| cpp/chrono/time_point/dsc operator_cmp | (see dedicated page) |
| cpp/chrono/time_point/dsc time_point_cast | (see dedicated page) |
| cpp/chrono/time_point/dsc floor | (see dedicated page) |
| cpp/chrono/time_point/dsc ceil | (see dedicated page) |
| cpp/chrono/time_point/dsc round | (see dedicated page) |


## Helper classes


| cpp/chrono/time_point/dsc common_type | (see dedicated page) |
| cpp/chrono/time_point|nested=true|notes= | |


## Example


### Example

```cpp
#include <algorithm>
#include <chrono>
#include <ctime>
#include <iomanip>
#include <iostream>

void slow_motion()
{
    static int a[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
    // Generate Γ(13) == 12! permutations:
    while (std::ranges::next_permutation(a).found) {}
}

int main()
{
    using namespace std::literals; // enables literal suffixes, e.g. 24h, 1ms, 1s.

    const std::chrono::time_point<std::chrono::system_clock> now =
        std::chrono::system_clock::now();

    const std::time_t t_c = std::chrono::system_clock::to_time_t(now - 24h);
    std::cout << "24 hours ago, the time was "
              << std::put_time(std::localtime(&t_c), "%F %T.\n") << std::flush;

    const std::chrono::time_point<std::chrono::steady_clock> start =
        std::chrono::steady_clock::now();

    std::cout << "Different clocks are not comparable: \n"
                 "  System time: " << now.time_since_epoch() << "\n"
                 "  Steady time: " << start.time_since_epoch() << '\n';

    slow_motion();

    const auto end = std::chrono::steady_clock::now();
    std::cout
        << "Slow calculations took "
        << std::chrono::duration_cast<std::chrono::microseconds>(end - start) << " ≈ "
        << (end - start) / 1ms << "ms ≈ " // almost equivalent form of the above, but
        << (end - start) / 1s << "s.\n";  // using milliseconds and seconds accordingly
}
```


**Output:**
```
24 hours ago, the time was 2021-02-15 18:28:52.
Different clocks are not comparable:
  System time: 1666497022681282572ns
  Steady time: 413668317434475ns
Slow calculations took 2090448µs ≈ 2090ms ≈ 2s.
```


## See also


| cpp/chrono/dsc duration | (see dedicated page) |
| cpp/chrono/dsc year_month_day | (see dedicated page) |

