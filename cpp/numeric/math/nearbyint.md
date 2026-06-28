---
title: std::nearbyint
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/nearbyint
---

cpp/numeric/math/declarations
|family=nearbyint
|param1=num
|desc=Rounds the floating-point argument `num` to an integer value in floating-point format, using the current rounding mode.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

The nearest integer value to `num`, according to the current rounding mode, is returned.

## Error handling

This function is not subject to any of the errors specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* `FE_INEXACT` is never raised.
* If `num` is ±∞, it is returned, unmodified.
* If `num` is ±0, it is returned, unmodified.
* If `num` is NaN, NaN is returned.

## Notes

The only difference between `std::nearbyint` and `std::rint` is that `std::nearbyint` never raises `FE_INEXACT`.
The largest representable floating-point values are exact integers in all standard floating-point formats, so `std::nearbyint` never overflows on its own; however the result may overflow any integer type (including `std::intmax_t`), when stored in an integer variable.
If the current rounding mode is `FE_TONEAREST`, this function rounds to even in halfway cases (like `std::rint`, but unlike `std::round`).

## Example


### Example

```cpp
#include <cfenv>
#include <cmath>
#include <iostream>
#pragma STDC FENV_ACCESS ON

int main()
{
    std::fesetround(FE_TONEAREST);
    std::cout << "rounding to nearest: \n"
              << "nearbyint(+2.3) = " << std::nearbyint(2.3)
              << "  nearbyint(+2.5) = " << std::nearbyint(2.5)
              << "  nearbyint(+3.5) = " << std::nearbyint(3.5) << '\n'
              << "nearbyint(-2.3) = " << std::nearbyint(-2.3)
              << "  nearbyint(-2.5) = " << std::nearbyint(-2.5)
              << "  nearbyint(-3.5) = " << std::nearbyint(-3.5) << '\n';

    std::fesetround(FE_DOWNWARD);
    std::cout << "rounding down:\n"
              << "nearbyint(+2.3) = " << std::nearbyint(2.3)
              << "  nearbyint(+2.5) = " << std::nearbyint(2.5)
              << "  nearbyint(+3.5) = " << std::nearbyint(3.5) << '\n'
              << "nearbyint(-2.3) = " << std::nearbyint(-2.3)
              << "  nearbyint(-2.5) = " << std::nearbyint(-2.5)
              << "  nearbyint(-3.5) = " << std::nearbyint(-3.5) << '\n';

    std::cout << "nearbyint(-0.0) = " << std::nearbyint(-0.0)  << '\n'
              << "nearbyint(-Inf) = " << std::nearbyint(-INFINITY) << '\n';
}
```


**Output:**
```
rounding to nearest: 
nearbyint(+2.3) = 2  nearbyint(+2.5) = 2  nearbyint(+3.5) = 4
nearbyint(-2.3) = -2  nearbyint(-2.5) = -2  nearbyint(-3.5) = -4
rounding down:
nearbyint(+2.3) = 2  nearbyint(+2.5) = 2  nearbyint(+3.5) = 3
nearbyint(-2.3) = -3  nearbyint(-2.5) = -3  nearbyint(-3.5) = -4
nearbyint(-0.0) = -0
nearbyint(-Inf) = -inf
```


## See also


| cpp/numeric/math/dsc rint | (see dedicated page) |
| cpp/numeric/math/dsc round | (see dedicated page) |
| cpp/numeric/fenv/dsc feround | (see dedicated page) |

