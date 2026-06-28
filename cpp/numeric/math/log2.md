---
title: std::log2
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/log2
---

cpp/numeric/math/declarations
|family=log2
|param1=num
|constexpr_since=26
|desc=Computes the [Binary logarithm|binary (base-$2$) logarithm](https://en.wikipedia.org/wiki/Binary logarithm|binary (base-$2$) logarithm) of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the base-$2$ logarithm of `num` ($log or $lb(num)$) is returned.
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

For integer `num`, the binary logarithm can be interpreted as the zero-based index of the most significant 1 bit in the input.

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
    std::cout << "log2(65536) = " << std::log2(65536) << '\n'
              << "log2(0.125) = " << std::log2(0.125) << '\n'
              << "log2(0x020f) = " << std::log2(0x020f)
              << " (highest set bit is in position 9)\n"
              << "base-5 logarithm of 125 = "
              << std::log2(125) / std::log2(5) << '\n';

    // special values
    std::cout << "log2(1) = " << std::log2(1) << '\n'
              << "log2(+Inf) = " << std::log2(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "log2(0) = " << std::log2(0) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
log2(65536) = 16
log2(0.125) = -3
log2(0x020f) = 9.04166 (highest set bit is in position 9)
base-5 logarithm of 125 = 3
log2(1) = 0
log2(+Inf) = inf
log2(0) = -inf
    errno == ERANGE: Numerical result out of range
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc log | (see dedicated page) |
| cpp/numeric/math/dsc log10 | (see dedicated page) |
| cpp/numeric/math/dsc log1p | (see dedicated page) |
| cpp/numeric/math/dsc exp2 | (see dedicated page) |

