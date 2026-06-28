---
title: std::chrono::time_zone_link
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_zone_link
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|
class time_zone_link;
```

The class `time_zone_link` represents an alternative name for a time zone.
Users cannot construct `time_zone_link` objects. The library implementation creates `time_zone_link` objects when it initializes the time zone database and provides `const` access to these objects.
`time_zone_link` is not copyable but does have a defaulted move constructor and a defaulted move assignment operator. However, as users have only `const` access to `time_zone_link` objects, these functions cannot be called in user code without invoking undefined behavior.

## Member functions


| cpp/chrono/time_zone_link/dsc accessors | (see dedicated page) |


## Nonmember functions


| cpp/chrono/time_zone_link/dsc operator_cmp | (see dedicated page) |

