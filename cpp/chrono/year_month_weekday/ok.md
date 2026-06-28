---
title: std::chrono::year_month_weekday::ok
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year_month_weekday/ok
---


```cpp
dcl|since=c++20|
constexpr bool ok() const noexcept;
```

Checks if this `year_month_weekday` object represents a valid date.

## Return value

`true` if this `year_month_weekday` object represents a valid date, that is, `year().ok() && month().ok() && weekday_indexed().ok()` is `true` and there are at least  s in the specified year and month. Otherwise `false`.

## Example


### Example

```cpp
#include <cassert>
#include <chrono>

int main()
{
    auto ymwdi{std::chrono::Wednesday[1]/1/2021};
    assert(ymwdi.ok());
    ymwdi = std::chrono::year(2021)/std::chrono::month(1)/std::chrono::Wednesday[42];
    assert(!ymwdi.ok());
}
```

