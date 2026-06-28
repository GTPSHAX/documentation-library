---
title: std::numeric_limits::is_exact
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/is_exact
---


```cpp
dcl rev multi
|dcl1=
static const bool is_exact;
|since2=c++11|dcl2=
static constexpr bool is_exact;
```

The value of `std::numeric_limits<T>::is_exact` is `true` for all arithmetic types `T` that use exact representation.

## Standard specializations


## Notes

While all fundamental types `T` for which `1=std::numeric_limits<T>::is_exact == true` are integer types, a library may define exact types that are not integers, e.g. a rational arithmetic type representing fractions.

## See also


| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_signed | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_bounded | (see dedicated page) |

