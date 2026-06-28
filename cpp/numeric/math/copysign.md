---
title: std::copysign
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/copysign
---

cpp/numeric/math/declarations
|family=copysign
|param1=mag
|param2=sgn
|constexpr_since=23
|desc=Composes a floating point value with the magnitude of `mag` and the sign of `sgn`.

## Parameters


### Parameters

- `mag, sgn` - floating-point or integer values

## Return value

If no errors occur, the floating point value with the magnitude of `mag` and the sign of `sgn` is returned.
If `mag` is NaN, then NaN with the sign of `sgn` is returned.
If `sgn` is -0, the result is only negative if the implementation supports the signed zero consistently in arithmetic operations.

## Error handling

This function is not subject to any errors specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* The returned value is exact (`FE_INEXACT` is never raised) and independent of the current rounding mode.

## Notes

`std::copysign` is the only portable way to manipulate the sign of a NaN value (to examine the sign of a NaN, `std::signbit` may also be used).

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::showpos
              << "copysign(1.0,+2.0) = " << std::copysign(1.0, +2.0) << '\n'
              << "copysign(1.0,-2.0) = " << std::copysign(1.0, -2.0) << '\n'
              << "copysign(inf,-2.0) = " << std::copysign(INFINITY, -2.0) << '\n'
              << "copysign(NaN,-2.0) = " << std::copysign(NAN, -2.0) << '\n';
}
```


**Output:**
```
copysign(1.0,+2.0) = +1
copysign(1.0,-2.0) = -1
copysign(inf,-2.0) = -inf
copysign(NaN,-2.0) = -nan
```


## See also


| cpp/numeric/math/dsc fabs | (see dedicated page) |
| cpp/numeric/math/dsc signbit | (see dedicated page) |

