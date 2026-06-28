---
title: std::trunc
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/trunc
---

cpp/numeric/math/declarations
|family=trunc
|param1=num
|constexpr_since=23
|desc=Computes the nearest integer not greater in magnitude than `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the nearest integer value not greater in magnitude than `num` (in other words, `num` rounded towards zero) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* The current rounding mode has no effect.
* If `num` is ±∞, it is returned, unmodified.
* If `num` is ±0, it is returned, unmodified.
* If `num` is NaN, NaN is returned.

## Notes

`FE_INEXACT` may be (but isn't required to be) raised when truncating a non-integer finite value.
The largest representable floating-point values are exact integers in all standard floating-point formats, so this function never overflows on its own; however the result may overflow any integer type (including `std::intmax_t`), when stored in an integer variable.
The  from floating-point to integral types also rounds towards zero, but is limited to the values that can be represented by the target type.

## Example


### Example

```cpp
#include <cmath>
#include <initializer_list>
#include <iostream>

int main()
{
    const auto data = std::initializer_list<double>
    {
        +2.7, -2.9, +0.7, -0.9, +0.0, 0.0, -INFINITY, +INFINITY, -NAN, +NAN
    };

    std::cout << std::showpos;
    for (double const x : data)
        std::cout << "trunc(" << x << ") == " << std::trunc(x) << '\n';
}
```


**Output:**
```
trunc(+2.7) == +2
trunc(-2.9) == -2
trunc(+0.7) == +0
trunc(-0.9) == -0
trunc(+0) == +0
trunc(+0) == +0
trunc(-inf) == -inf
trunc(+inf) == +inf
trunc(-nan) == -nan
trunc(+nan) == +nan
```


## See also


| cpp/numeric/math/dsc floor | (see dedicated page) |
| cpp/numeric/math/dsc ceil | (see dedicated page) |
| cpp/numeric/math/dsc round | (see dedicated page) |

