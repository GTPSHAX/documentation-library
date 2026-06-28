---
title: std::numeric_limits::is_iec559
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/is_iec559
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const bool is_iec559;
|dcl2=
static constexpr bool is_iec559;
```

The value of `std::numeric_limits<T>::is_iec559` is `true` for all floating-point types `T` which fulfill the requirements of IEC 559 (IEEE 754) standard. If `std::numeric_limits<T>::is_iec559` is `true`, then `std::numeric_limits<T>::has_infinity`, `std::numeric_limits<T>::has_quiet_NaN`, and `std::numeric_limits<T>::has_signaling_NaN` are also `true`.

## Standard specializations


## See also


| cpp/types/numeric_limits/dsc has_infinity | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_quiet_NaN | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_signaling_NaN | (see dedicated page) |

