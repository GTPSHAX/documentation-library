---
title: std::chrono::current_zone
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/current_zone
---

ddcl|header=chrono|since=c++20|
const std::chrono::time_zone* current_zone();
Convenience function for obtaining local time zone from the [List of tz database time zones|time zone database](https://en.wikipedia.org/wiki/List of tz database time zones|time zone database). Equivalent to `std::chrono::get_tzdb().current_zone()`.

## Exceptions

`std::runtime_error` if this is the first reference to the time zone database and the time zone database cannot be initialized.

## Notes

A call to this function that is the first reference to the time zone database will cause it to be initialized.

## Example


### Example


**Output:**
```
2021-09-13 19:46:42.249182012 MAGT
```


## See also


| cpp/chrono/tzdb/dsc current_zone | (see dedicated page) |
| cpp/chrono/dsc tzdb functions | (see dedicated page) |

