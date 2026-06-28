---
title: std::chrono::weekday::weekday
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/weekday/weekday
---


```cpp
dcl|since=c++20|num=1|1=
weekday() = default;
dcl|since=c++20|num=2|
constexpr explicit weekday( unsigned wd ) noexcept;
dcl|since=c++20|num=3|
constexpr weekday( const std::chrono::sys_days& sd ) noexcept;
dcl|since=c++20|num=4|
constexpr explicit weekday( const std::chrono::local_days& ld ) noexcept;
```

Constructs a `weekday` object.
1. Default constructor leaves the weekday value uninitialized.
2. Constructs a `weekday` object holding the weekday value `wd`. If `1=wd == 7`, the value held is `0`. If `wd > 255`, the value held is unspecified.
3. Constructs a `weekday` object representing the day of the week `sd` corresponds to. This constructor defines an implicit conversion from `std::chrono::sys_days` to `weekday`.
4. Constructs a `weekday` object representing the day of the week `ld` corresponds to, as if by `weekday(std::chrono::sys_days(ld.time_since_epoch()))`.

## Parameters


### Parameters

- `wd` - a weekday value
- `sd` - a system days object
- `ld` - a local days object

## Example


### Example

```cpp
#include <chrono>
#include <iomanip>
#include <iostream>

int main()
{
    constexpr std::chrono::weekday friday{5}; // uses overload (2)
    static_assert(friday == std::chrono::Friday);

    for (int y{2020}; y <= 2024; ++y)
    {
        const std::chrono::year cur_year{y};
        for (int cur_month{1}; cur_month != 13; ++cur_month)
        {
            const std::chrono::year_month_day ymd{cur_year/cur_month/13};
            const std::chrono::weekday cur_weekday{std::chrono::sys_days(ymd)}; // (3)
            if (cur_weekday == friday)
                std::cout << ymd << " is " << friday << '\n';
        }
    }
}
```


**Output:**
```
2020-03-13 is Fri
2020-11-13 is Fri
2021-08-13 is Fri
2022-05-13 is Fri
2023-01-13 is Fri
2023-10-13 is Fri
2024-09-13 is Fri
2024-12-13 is Fri
```

