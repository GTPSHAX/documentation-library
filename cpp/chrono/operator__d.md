---
title: std::literals::chrono_literals::operator""d
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""d
---

ddcl|header=chrono|since=c++20|
constexpr std::chrono::day operator ""d( unsigned long long d ) noexcept;
Forms a `std::chrono::day` literal representing a day of the month in the calendar.

## Parameters


### Parameters

- `d` - the day value

## Return value

A `std::chrono::day` storing `d`. If `d > 255`, the stored value is unspecified.

## Possible implementation

eq fun
|1=
constexpr std::chrono::day operator ""d(unsigned long long d) noexcept
{
return std::chrono::day(d);
}

## Notes


## Example


### Example


**Output:**
```
42      42 is not a valid day
0       00 is not a valid day
42      42 is not a valid day
```


## See also


| cpp/chrono/day/dsc constructor | (see dedicated page) |
| cpp/chrono/day/dsc operator_unsigned | (see dedicated page) |

