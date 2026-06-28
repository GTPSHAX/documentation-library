---
title: std::chrono::year_month_weekday::year
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday/accessors
---


```cpp
dcl|since=c++20|num=1|
constexpr std::chrono::year year() const noexcept;
dcl|since=c++20|num=2|
constexpr std::chrono::month month() const noexcept;
dcl|since=c++20|num=3|
constexpr std::chrono::weekday weekday() const noexcept;
dcl|since=c++20|num=4|
constexpr unsigned index() const noexcept;
dcl|since=c++20|num=5|
constexpr std::chrono::weekday_indexed weekday_indexed() const noexcept;
```

Retrieves the field values stored in this `year_month_weekday` object.

## Return value

1. Returns the stored `std::chrono::year` value.
2. Returns the stored `std::chrono::month` value.
3. Returns the stored `std::chrono::weekday` value.
4. Returns the stored weekday index.
5. `weekday()[index()]`

## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    constexpr auto ym{std::chrono::year(2021)/std::chrono::January};
    constexpr auto wdi{std::chrono::Wednesday[1]};
    auto ymwdi{ym/wdi};
    const auto index{ymwdi.index() + 1};
    auto weekday{ymwdi.weekday() + std::chrono::days(1)};
    ymwdi = {ymwdi.year()/ymwdi.month()/weekday[index]};
    // Second Thursday in January, 2021
    assert(std::chrono::year_month_day{ymwdi} == std::chrono::January/14/2021);
}
```

