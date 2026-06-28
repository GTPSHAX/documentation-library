---
title: std::chrono::duration::min
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/min
---


```cpp
dcl rev multi|until1=c++20|dcl1=
static constexpr duration min();
|dcl2=
static constexpr duration min() noexcept;
```

Returns a duration with the lowest possible value.
If the representation `rep` of the duration requires some other implementation to return a minimum-length duration, `std::chrono::duration_values` can be specialized to return the desired value.

## Parameters

(none)

## Return value

`duration(std::chrono::duration_values<rep>::min())`

## See also


| cpp/chrono/duration/dsc zero | (see dedicated page) |
| cpp/chrono/duration/dsc max | (see dedicated page) |

