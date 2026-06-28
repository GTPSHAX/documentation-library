---
title: std::chrono::locate_zone
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/locate_zone
---

ddcl|since=c++20|header=chrono|
const std::chrono::time_zone* locate_zone( std::string_view tz_name );
Convenience function for locating a time zone in the [List of tz database time zones|time zone database](https://en.wikipedia.org/wiki/List of tz database time zones|time zone database). Equivalent to `std::chrono::get_tzdb().locate_zone(tz_name)`.

## Parameters


### Parameters

- `tz_name` - a time zone name to locate

## Exceptions

`std::runtime_error` if the specified time zone cannot be found, or if this is the first reference to the time zone database and the time zone database cannot be initialized.

## Notes

A call to this function that is the first reference to the time zone database will cause it to be initialized.

## Example


### Example


**Output:**
```
Atlantic/Bermuda
std::chrono::tzdb: cannot locate zone: Alcatraz
```


## See also


| cpp/chrono/tzdb/dsc locate_zone | (see dedicated page) |
| cpp/chrono/dsc tzdb functions | (see dedicated page) |

