---
title: std::log10
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/log10
---

cpp/numeric/math/declarations
|family=log10
|param1=num
|constexpr_since=26
|desc=Computes the [Common logarithm|common (base-$10$) logarithm](https://en.wikipedia.org/wiki/Common logarithm|common (base-$10$) logarithm) of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the common (base-$10$) logarithm of `num` ($log or $lg(num)$) is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a pole error occurs, `HUGE_VAL|-HUGE_VAL`, `-HUGE_VALF`, or `-HUGE_VALL` is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error occurs if `num` is less than zero.
Pole error may occur if `num` is zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, -∞ is returned and `FE_DIVBYZERO` is raised.
* If the argument is 1, +0 is returned.
* If the argument is negative, NaN is returned and `FE_INVALID` is raised.
* If the argument is +∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes


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
    std::cout << "log10(1000) = " << std::log10(1000) << '\n'
              << "log10(0.001) = " << std::log10(0.001) << '\n'
              << "base-5 logarithm of 125 = "
              << std::log10(125) / std::log10(5) << '\n';

    // special values
    std::cout << "log10(1) = " << std::log10(1) << '\n'
              << "log10(+Inf) = " << std::log10(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "log10(0) = " << std::log10(0) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
log10(1000) = 3
log10(0.001) = -3
base-5 logarithm of 125 = 3
log10(1) = 0
log10(+Inf) = inf
log10(0) = -inf
    errno == ERANGE: Numerical result out of range
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc log | (see dedicated page) |
| cpp/numeric/math/dsc log2 | (see dedicated page) |
| cpp/numeric/math/dsc log1p | (see dedicated page) |
| cpp/numeric/complex/dsc log10 | (see dedicated page) |
| cpp/numeric/valarray/dsc log10 | (see dedicated page) |

