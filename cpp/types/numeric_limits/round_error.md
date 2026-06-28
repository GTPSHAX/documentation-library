---
title: std::numeric_limits::round_error
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/round_error
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static T round_error() throw();
|dcl2=
static constexpr T round_error() noexcept;
```

Returns the largest possible rounding error in ULPs (units in the last place) as defined by ISO 10967, which can vary from `0.5` (rounding to the nearest digit) to `1.0` (rounding to zero or to infinity). It is only meaningful if `1=std::numeric_limits<T>::is_integer == false`.

## Return value


## See also


| cpp/types/numeric_limits/dsc round_style | (see dedicated page) |

