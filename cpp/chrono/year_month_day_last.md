---
title: std::chrono::year_month_day_last
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_day_last
---

ddcl|header=chrono|since=c++20|
class year_month_day_last;
The class `year_month_day_last` represents the last day of a specific year and month. It is a field-based time point, with a resolution of `std::chrono::days`, subject to the limit that it can only represent the last day of a month.
`std::chrono::years`- and `std::chrono::months`-oriented arithmetic are supported directly. An implicit conversion to `std::chrono::sys_days` allows `std::chrono::days`-oriented arithmetic to be performed efficiently.
`year_month_day_last` is a *TriviallyCopyable* *StandardLayoutType*.

## Member functions


| cpp/chrono/year_month_day_last/dsc constructor | (see dedicated page) |
| cpp/chrono/year_month_day_last/dsc operator arith | (see dedicated page) |
| cpp/chrono/year_month_day_last/dsc accessors | (see dedicated page) |
| cpp/chrono/year_month_day_last/dsc operator days | (see dedicated page) |
| cpp/chrono/year_month_day_last/dsc ok | (see dedicated page) |


## Nonmember functions


| cpp/chrono/year_month_day_last/dsc operator cmp | (see dedicated page) |
| cpp/chrono/year_month_day_last/dsc operator arith 2 | (see dedicated page) |
| cpp/chrono/year_month_day_last/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|year_month_day_last | (see dedicated page) |
| cpp/chrono/year_month_day_last|nested=true|notes= | |


## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    const auto ymd = std::chrono::year_month_day
    {
        std::chrono::floor<std::chrono::days>(std::chrono::system_clock::now())
    };

    const std::chrono::year_month_day_last ymdl
    {
        ymd.year(), ymd.month() / std::chrono::last
    };

    std::cout << "The last day of present month (" << ymdl << ") is: "
              << std::chrono::year_month_day{ymdl}.day() << '\n';

    // The 'last' object can be placed wherever it is legal to place a 'day':
    using namespace std::chrono;
    constexpr std::chrono::year_month_day_last
        ymdl1 = 2023y / February / last,
        ymdl2 = last / February / 2023y,
        ymdl3 = February / last / 2023y;
    static_assert(ymdl1 == ymdl2 && ymdl2 == ymdl3);
}
```


**Output:**
```
The last day of present month (2023/Aug/last) is: 31
```


## See also


| cpp/chrono/dsc year_month_day | (see dedicated page) |

