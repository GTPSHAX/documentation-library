---
title: std::floor
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/floor
---

cpp/numeric/math/declarations
|family=floor
|param1=num
|constexpr_since=23
|desc=Computes the largest integer value not greater than `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the largest integer value not greater than `num`, that is $⌊num⌋$, is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* The current rounding mode has no effect.
* If `num` is ±∞, it is returned, unmodified.
* If `num` is ±0, it is returned, unmodified.
* If `num` is NaN, NaN is returned.

## Notes

`FE_INEXACT` may be (but isn't required to be) raised when rounding a non-integer finite value.
The largest representable floating-point values are exact integers in all standard floating-point formats, so this function never overflows on its own; however the result may overflow any integer type (including `std::intmax_t`), when stored in an integer variable.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::fixed
              << "floor(+2.7) = " << std::floor(+2.7) << '\n'
              << "floor(-2.7) = " << std::floor(-2.7) << '\n'
              << "floor(-0.0) = " << std::floor(-0.0) << '\n'
              << "floor(-Inf) = " << std::floor(-INFINITY) << '\n';
}
```


**Output:**
```
floor(+2.7) = 2.000000
floor(-2.7) = -3.000000
floor(-0.0) = -0.000000
floor(-Inf) = -inf
```


## See also


| cpp/numeric/math/dsc ceil | (see dedicated page) |
| cpp/numeric/math/dsc trunc | (see dedicated page) |
| cpp/numeric/math/dsc round | (see dedicated page) |

