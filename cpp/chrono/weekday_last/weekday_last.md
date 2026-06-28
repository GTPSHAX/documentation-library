---
title: std::chrono::weekday_last::weekday_last
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday_last/weekday_last
---

ddcl|since=c++20|
constexpr explicit weekday_last( const std::chrono::weekday& wd ) noexcept;
Constructs a `weekday_last` object storing the `std::chrono::weekday|weekday` `wd`.

## Notes

A more convenient way to construct a `weekday_last` is with `weekday`'s `operator[]`, i.e., `wd[std::chrono::last]`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
using namespace std::chrono;

int main()
{
    const year_month_day ymd{floor<days>(system_clock::now())};
    const weekday_last wdl{Sunday[last]}; // A last Sunday of a month
    const year_month_day last_sun{ymd.year() / ymd.month() / wdl};

    std::cout << "The last Sunday of current month falls on "
              << (int)last_sun.year() << '/'
              << (unsigned)last_sun.month() << '/'
              << (unsigned)last_sun.day() << '\n';
}
```


**Output:**
```
The last Sunday of current month falls on 2021/9/26
```

