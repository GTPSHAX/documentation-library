---
title: std::chrono::weekday_indexed
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_indexed
---

ddcl|header=chrono|since=c++20|
class weekday_indexed;
The class `weekday_indexed` combines a `cpp/chrono/weekday`, representing a day of the week in the [proleptic Gregorian calendar](https://en.wikipedia.org/wiki/proleptic Gregorian calendar), with a small index  in the range . It represents the first, second, third, fourth, or fifth weekday of some month.
`weekday_indexed` is a *TriviallyCopyable* *StandardLayoutType*.

## Member functions


| cpp/chrono/weekday_indexed/dsc constructor | (see dedicated page) |
| cpp/chrono/weekday_indexed/dsc weekday | (see dedicated page) |
| cpp/chrono/weekday_indexed/dsc index | (see dedicated page) |
| cpp/chrono/weekday_indexed/dsc ok | (see dedicated page) |


## Nonmember functions


| cpp/chrono/weekday_indexed/dsc operator cmp | (see dedicated page) |
| cpp/chrono/weekday_indexed/dsc operator ltlt | (see dedicated page) |


## Helper classes


| cpp/chrono/dsc formatter|weekday_indexed | (see dedicated page) |
| cpp/chrono/weekday_indexed|nested=true|notes= | |


## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono;

    constexpr weekday_indexed wi = Friday[2];

    // Indexed weekday can be used at any place where chrono::day can be used:
    constexpr year_month_weekday ymwd = 2021y / August / wi;
    static_assert(ymwd == August / wi / 2021y &&
                  ymwd == wi / August / 2021y);
    std::cout << ymwd << '\n';

    constexpr year_month_day ymd{ymwd}; // a conversion
    static_assert(ymd == 2021y / 8 / 13);
    std::cout << ymd << '\n';
}
```


**Output:**
```
2021/Aug/Fri[2]
2021-08-13
```

