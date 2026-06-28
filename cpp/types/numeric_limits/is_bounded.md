---
title: std::numeric_limits::is_bounded
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/is_bounded
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const bool is_bounded;
|dcl2=
static constexpr bool is_bounded;
```

The value of `std::numeric_limits<T>::is_bounded` is `true` for all arithmetic types `T` that represent a finite set of values. While all fundamental types are bounded, this constant would be `false` in a specialization of `std::numeric_limits` for a library-provided arbitrary precision arithmetic type.

## Standard specializations


## See also


| cpp/types/numeric_limits/dsc is_integer | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_signed | (see dedicated page) |
| cpp/types/numeric_limits/dsc is_exact | (see dedicated page) |

