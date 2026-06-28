---
title: std::tanh
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/tanh
---

cpp/numeric/math/declarations
|family=tanh
|param1=num
|constexpr_since=26
|desc=Computes the hyperbolic tangent of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the hyperbolic tangent of `num` ($tanh(num)$, or $) is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0, ±0 is returned.
* if the argument is ±∞, ±1 is returned.
* if the argument is NaN, NaN is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/tanh.html POSIX specifies] that in case of underflow, `num` is returned unmodified, and if that is not supported, and implementation-defined value no greater than DBL_MIN, FLT_MIN, and LDBL_MIN is returned.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <random>

double get_random_between(double min, double max)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    return std::uniform_real_distribution<>(min, max)(gen);
}

int main()
{
    const double x = get_random_between(-1.0, 1.0);

    std::cout << std::showpos
              << "tanh(+1) = " << std::tanh(+1) << '\n'
              << "tanh(-1) = " << std::tanh(-1) << '\n'
              << "tanh(x)*sinh(2*x)-cosh(2*x) = "
              << std::tanh(x) * std::sinh(2 * x) - std::cosh(2 * x) << '\n'
              // special values:
              << "tanh(+0) = " << std::tanh(+0.0) << '\n'
              << "tanh(-0) = " << std::tanh(-0.0) << '\n';
}
```


**Output:**
```
tanh(+1) = +0.761594
tanh(-1) = -0.761594
tanh(x)*sinh(2*x)-cosh(2*x) = -1
tanh(+0) = +0
tanh(-0) = -0
```


## See also


| cpp/numeric/math/dsc sinh | (see dedicated page) |
| cpp/numeric/math/dsc cosh | (see dedicated page) |
| cpp/numeric/math/dsc atanh | (see dedicated page) |
| cpp/numeric/complex/dsc tanh | (see dedicated page) |
| cpp/numeric/valarray/dsc tanh | (see dedicated page) |

