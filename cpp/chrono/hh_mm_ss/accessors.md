---
title: std::chrono::hh_mm_ss::subseconds
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/hh_mm_ss/accessors
---


```cpp
dcl|num=1|
constexpr bool is_negative() const noexcept;
dcl|num=2|
constexpr std::chrono::hours hours() const noexcept;
dcl|num=3|
constexpr std::chrono::minutes minutes() const noexcept;
dcl|num=4|
constexpr std::chrono::seconds seconds() const noexcept;
dcl|num=5|
constexpr precision subseconds() const noexcept;
```

Obtains the components of the stored "broken down" time.

## Return value

Let `d` be the represented duration:
1. `true` if `d` is negative, `false` otherwise.
2. `std::chrono::duration_cast<std::chrono::hours>(abs(d))`
3. `std::chrono::duration_cast<std::chrono::minutes>(abs(d) - hours())`
4. `std::chrono::duration_cast<std::chrono::seconds>(abs(d) - hours() - minutes())`
5. `abs(d) - hours() - minutes() - seconds()` if `std::chrono::treat_as_floating_point_v<precision::rep>` is `true`; otherwise `std::chrono::duration_cast<precision>(abs(d) - hours() - minutes() - seconds())`.

## Example

