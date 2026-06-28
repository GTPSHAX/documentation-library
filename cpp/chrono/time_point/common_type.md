---
title: std::common_type<std::chrono::time_point>
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/common_type
---


# common_typesmall|<std::chrono::time_point>

ddcl|since=c++11|
template< class Clock, class Duration1, class Duration2 >
struct common_type<std::chrono::time_point<Clock, Duration1>,
std::chrono::time_point<Clock, Duration2>>;
Exposes the type named `type`, which is the common type of two `std::chrono::time_point`s.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Notes

The common type of two `std::chrono::time_point` types is a `std::chrono::time_point` with the same clock as the two types and the `std::common_type` of their durations.

## Example

