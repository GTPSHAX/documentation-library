---
title: std::chrono::system_clock::from_time_t
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/system_clock/from_time_t
---

ddcl|since=c++11|
static std::chrono::system_clock::time_point from_time_t( std::time_t t ) noexcept;
Converts `t` to a time point type, using the coarser precision of the two types.
If `time_point` has lower precision, it is implementation defined whether the value is rounded or truncated.

## Parameters


### Parameters

- `t` - `std::time_t` value to convert

## Return value

A value of type `std::chrono::system_clock::time_point` representing `t`.

## Example


### Example


**Output:**
```
987654321ns (987ms)
```


## See also


| cpp/chrono/system_clock/dsc to_time_t | (see dedicated page) |

