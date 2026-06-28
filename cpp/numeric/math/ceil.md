---
title: std::ceil
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/ceil
---

cpp/numeric/math/declarations
|family=ceil
|param1=num
|constexpr_since=23
|desc=Computes the least integer value not less than `num`.

## Parameters


### Parameters

- `num` - floating point or integer value

## Return value

If no errors occur, the smallest integer value not less than `num`, that is $⌈num⌉$, is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* The current rounding mode has no effect.
* If `num` is ±∞, it is returned unmodified.
* If `num` is ±0, it is returned, unmodified.
* If `num` is NaN, NaN is returned.

## Notes

`FE_INEXACT` may be (but is not required to be) raised when rounding a non-integer finite value.
The largest representable floating-point values are exact integers in all standard floating-point formats, so this function never overflows on its own; however the result may overflow any integer type (including `std::intmax_t`), when stored in an integer variable. It is for this reason that the return type is floating-point not integral.
This function (for `double` argument) behaves as if (except for the freedom to not raise `FE_INEXACT`) implemented by the following code:

```cpp
#include <cfenv>
#include <cmath>
#pragma STDC FENV_ACCESS ON

double ceil(double x)
{
    int save_round = std::fegetround();
    std::fesetround(FE_UPWARD);
    double result = std::rint(x); // or std::nearbyint
    std::fesetround(save_round);
    return result;
}
```


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::fixed
              << "ceil(+2.4) = " << std::ceil(+2.4) << '\n'
              << "ceil(-2.4) = " << std::ceil(-2.4) << '\n'
              << "ceil(-0.0) = " << std::ceil(-0.0) << '\n'
              << "ceil(-Inf) = " << std::ceil(-INFINITY) << '\n';
}
```


**Output:**
```
ceil(+2.4) = 3.000000
ceil(-2.4) = -2.000000
ceil(-0.0) = -0.000000
ceil(-Inf) = -inf
```


## See also


| cpp/numeric/math/dsc floor | (see dedicated page) |
| cpp/numeric/math/dsc trunc | (see dedicated page) |
| cpp/numeric/math/dsc round | (see dedicated page) |
| cpp/numeric/math/dsc nearbyint | (see dedicated page) |
| cpp/numeric/math/dsc rint | (see dedicated page) |


## External links

