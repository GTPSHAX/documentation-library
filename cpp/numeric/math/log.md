---
title: std::log
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/log
---

cpp/numeric/math/declarations
|family=log
|param1=num
|constexpr_since=26
|desc=Computes the [Natural logarithm|natural (base-$e$) logarithm](https://en.wikipedia.org/wiki/Natural logarithm|natural (base-$e$) logarithm) of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the natural (base-$e$) logarithm of `num` ($ln(num)$ or $log) is returned.
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
    std::cout << "log(1) = " << std::log(1) << '\n'
              << "base-5 logarithm of 125 = " << std::log(125) / std::log(5) << '\n';

    // special values
    std::cout << "log(1) = " << std::log(1) << '\n'
              << "log(+Inf) = " << std::log(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "log(0) = " << std::log(0) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
log(1) = 0
base-5 logarithm of 125 = 3
log(1) = 0
log(+Inf) = inf
log(0) = -inf
    errno == ERANGE: Numerical result out of range
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc log10 | (see dedicated page) |
| cpp/numeric/math/dsc log2 | (see dedicated page) |
| cpp/numeric/math/dsc log1p | (see dedicated page) |
| cpp/numeric/math/dsc exp | (see dedicated page) |
| cpp/numeric/complex/dsc log | (see dedicated page) |
| cpp/numeric/valarray/dsc log | (see dedicated page) |

