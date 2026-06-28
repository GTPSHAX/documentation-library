---
title: std::chrono::time_zone
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_zone
---

ddcl|header=chrono|since=c++20|
class time_zone;
The class `time_zone` represents all time zone transitions for a specific geographic area.
Users cannot construct `time_zone` objects. The library implementation creates `time_zone` objects when it initializes the [List of tz database time zones|time zone database](https://en.wikipedia.org/wiki/List of tz database time zones|time zone database) and provides `const` access to these objects.
`time_zone` is not copyable but does have a defaulted move constructor and a defaulted move assignment operator. However, as users have only `const` access to `time_zone` objects, these functions cannot be called in user code without invoking undefined behavior.

## Member functions


| cpp/chrono/time_zone/dsc name | (see dedicated page) |
| cpp/chrono/time_zone/dsc get_info | (see dedicated page) |
| cpp/chrono/time_zone/dsc to_sys | (see dedicated page) |
| cpp/chrono/time_zone/dsc to_local | (see dedicated page) |


## Nonmember functions


| cpp/chrono/time_zone/dsc operator_cmp | (see dedicated page) |


## Example

