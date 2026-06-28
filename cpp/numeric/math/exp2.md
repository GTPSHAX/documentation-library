---
title: std::exp2
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/exp2
---

cpp/numeric/math/declarations
|family=exp2
|param1=num
|constexpr_since=26
|desc=Computes $2$ raised to the given power `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the base-$2$ exponential of `num` ($2) is returned.
If a range error due to overflow occurs, `HUGE_VAL|+HUGE_VAL`, `+HUGE_VALF`, or `+HUGE_VALL` is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, 1 is returned.
* If the argument is -∞, +0 is returned.
* If the argument is +∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes

For integral exponents, it may be preferable to use `std::ldexp`.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <cstring>
#include <iostream>

// #pragma STDC FENV_ACCESS ON

int main()
{
    std::cout << "exp2(4) = " << std::exp2(4) << '\n'
              << "exp2(0.5) = " << std::exp2(0.5) << '\n'
              << "exp2(-4) = " << std::exp2(-4) << '\n';

    // special values
    std::cout << "exp2(-0) = " << std::exp2(-0.0) << '\n'
              << "exp2(-Inf) = " << std::exp2(-INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    const double inf = std::exp2(1024);
    const bool is_range_error = errno == ERANGE;

    std::cout << "exp2(1024) = " << inf << '\n';
    if (is_range_error)
        std::cout << "    errno == ERANGE: " << std::strerror(ERANGE) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
exp2(4) = 16
exp2(0.5) = 1.41421
exp2(-4) = 0.0625
exp2(-0) = 1
exp2(-Inf) = 0
exp2(1024) = inf
    errno == ERANGE: Numerical result out of range
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc exp | (see dedicated page) |
| cpp/numeric/math/dsc expm1 | (see dedicated page) |
| cpp/numeric/math/dsc ldexp | (see dedicated page) |
| cpp/numeric/math/dsc log2 | (see dedicated page) |

