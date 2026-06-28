---
title: std::numeric_limits::has_denorm_loss
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/has_denorm_loss
---


```cpp
dcl rev multi|until1=c++11|dcl1=
static const bool has_denorm_loss;
|notes2=|dcl2=
static constexpr bool has_denorm_loss;
```

The value of `std::numeric_limits<T>::has_denorm_loss` is `true` for all floating-point types `T` that detect loss of precision when creating a subnormal number as denormalization loss rather than as inexact result (see below).

## Standard specializations


| Item | Description |
|------|-------------|
| **{{tt** | T |


## Notes

Standard-compliant IEEE 754 floating-point implementations of subnormal numbers are required to detect the loss of accuracy associated with the creation of such number, if it occurs, and may do so in one of the two distinct ways:
# Denormalization loss: the delivered result differs from what would have been computed were exponent range unbounded.
# Inexact result: the delivered result differs from what would have been computed were both exponent range and precision unbounded.
No implementation of denormalization loss mechanism exists (accuracy loss is detected after rounding, as inexact result), and this option was removed in the 2008 revision of IEEE Std 754.
libstdc++, libc++, libCstd, and stlport4 define this constant as `false` for all floating-point types. Microsoft Visual Studio defines it as `true` for all floating-point types.
As with any floating-point computations, accuracy loss may raise `FE_INEXACT`.

## Example


## See also


| cpp/types/numeric_limits/dsc tinyness_before | (see dedicated page) |
| cpp/types/numeric_limits/dsc has_denorm | (see dedicated page) |

