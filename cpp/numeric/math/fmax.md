---
title: std::fmax
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fmax
---

cpp/numeric/math/declarations
|family=fmax
|param1=x
|param2=y
|constexpr_since=23
|desc=Returns the larger of two floating point arguments, treating NaNs as missing data (between a NaN and a numeric value, the numeric value is chosen).

## Parameters


### Parameters

- `x, y` - floating-point or integer values

## Return value

If successful, returns the larger of two floating point values. The value returned is exact and does not depend on any rounding modes.

## Error handling

This function is not subject to any of the error conditions specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If one of the two arguments is NaN, the value of the other argument is returned.
* Only if both arguments are NaN, NaN is returned.

## Notes

This function is not required to be sensitive to the sign of zero, although some implementations additionally enforce that if one argument is `+0` and the other is `-0`, then `+0` is returned.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << "fmax(2,1)    = " << std::fmax(2, 1) << '\n'
              << "fmax(-Inf,0) = " << std::fmax(-INFINITY, 0) << '\n'
              << "fmax(NaN,-1) = " << std::fmax(NAN, -1) << '\n';
}
```


**Output:**
```
fmax(2,1)    = 2
fmax(-Inf,0) = 0
fmax(NaN,-1) = -1
```


## See also


| cpp/numeric/math/dsc isgreater | (see dedicated page) |
| cpp/numeric/math/dsc fmin | (see dedicated page) |
| cpp/algorithm/dsc max | (see dedicated page) |
| cpp/algorithm/dsc max_element | (see dedicated page) |
| cpp/algorithm/dsc minmax | (see dedicated page) |
| cpp/algorithm/dsc minmax_element | (see dedicated page) |

