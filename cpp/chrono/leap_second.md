---
title: std::chrono::leap_second
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/leap_second
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++20|
class leap_second;
```

The class `leap_second` represents the date and time of a leap second insertion.
Users cannot construct `leap_second` objects except by copying from existing `leap_second` objects. The library implementation creates `leap_second` objects when it initializes the time zone database and provides `const` access to these objects.
`leap_second` has a defaulted copy constructor and a defaulted copy assignment operator.

## Member functions


| cpp/chrono/leap_second/dsc date | (see dedicated page) |


## Nonmember functions


| cpp/chrono/leap_second/dsc operator cmp | (see dedicated page) |


## Helper classes


| cpp/chrono/leap_second|nested=true|notes= | |

