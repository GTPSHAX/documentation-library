---
title: std::fegetround
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/fenv/feround
---


```cpp
**Header:** `<`cfenv`>`
dcl|since=c++11|num=1|
int fesetround( int round )
dcl|since=c++11|num=2|
int fegetround()
```

Manages the floating-point rounding direction.
1. Attempts to establish the floating-point rounding direction equal to the argument `round`, which is expected to be one of the floating point rounding macros.
2. Returns the value of the floating point rounding macro that corresponds to the current rounding direction.

## Parameters


### Parameters

- `round` - rounding direction, one of floating point rounding macros

## Return value

1) `0` on success, non-zero otherwise.
2) The floating point rounding macro describing the current rounding direction or a negative value if the direction cannot be determined.

## Notes

The current rounding mode, reflecting the effects of the most recent `fesetround`, can also be queried with `FLT_ROUNDS`.
See floating-point rounding macros for the effects of rounding.

## Example


## See also


| cpp/numeric/math/dsc nearbyint | (see dedicated page) |
| cpp/numeric/math/dsc rint | (see dedicated page) |

