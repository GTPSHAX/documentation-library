---
title: std::fmin
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fmin
---

cpp/numeric/math/declarations
|family=fmin
|param1=x
|param2=y
|constexpr_since=23
|desc=Returns the smaller of two floating point arguments, treating NaNs as missing data (between a NaN and a numeric value, the numeric value is chosen).

## Parameters


### Parameters

- `x, y` - floating-point or integer values

## Return value

If successful, returns the smaller of two floating point values. The value returned is exact and does not depend on any rounding modes.

## Error handling

This function is not subject to any of the error conditions specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If one of the two arguments is NaN, the value of the other argument is returned.
* Only if both arguments are NaN, NaN is returned.

## Notes

This function is not required to be sensitive to the sign of zero, although some implementations additionally enforce that if one argument is `+0` and the other is `-0`, then `-0` is returned.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << "fmin(2,1)    = " << std::fmin(2, 1) << '\n'
              << "fmin(-Inf,0) = " << std::fmin(-INFINITY, 0) << '\n'
              << "fmin(NaN,-1) = " << std::fmin(NAN, -1) << '\n';
}
```


**Output:**
```
fmin(2,1)    = 1
fmin(-Inf,0) = -inf
fmin(NaN,-1) = -1
```


## See also


| cpp/numeric/math/dsc isless | (see dedicated page) |
| cpp/numeric/math/dsc fmax | (see dedicated page) |
| cpp/algorithm/dsc min | (see dedicated page) |
| cpp/algorithm/dsc min_element | (see dedicated page) |
| cpp/algorithm/dsc minmax | (see dedicated page) |
| cpp/algorithm/dsc minmax_element | (see dedicated page) |

