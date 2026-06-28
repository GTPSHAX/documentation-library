---
title: std::asinh
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/asinh
---

cpp/numeric/math/declarations
|family=asinh
|param1=num
|constexpr_since=26
|desc=Computes the inverse hyperbolic sine of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the inverse hyperbolic sine of `num` ($sinh, or $arsinh(num)$), is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0 or ±∞, it is returned unmodified.
* if the argument is NaN, NaN is returned.

## Notes

Although the C standard (to which C++ refers for this function) names this function "arc hyperbolic sine", the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is "inverse hyperbolic sine" (used by POSIX) or "area hyperbolic sine".

## Examples


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << "asinh(1) = " << std::asinh(1) << '\n'
              << "asinh(-1) = " << std::asinh(-1) << '\n';

    // special values
    std::cout << "asinh(+0) = " << std::asinh(+0.0) << '\n'
              << "asinh(-0) = " <<  std::asinh(-0.0) << '\n';
}
```


**Output:**
```
asinh(1) = 0.881374
asinh(-1) = -0.881374
asinh(+0) = 0
asinh(-0) = -0
```


## See also


| cpp/numeric/math/dsc acosh | (see dedicated page) |
| cpp/numeric/math/dsc atanh | (see dedicated page) |
| cpp/numeric/math/dsc sinh | (see dedicated page) |
| cpp/numeric/complex/dsc asinh | (see dedicated page) |


## External links

