---
title: std::sqrt
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/sqrt
---

cpp/numeric/math/declarations
|family=sqrt
|param1=num
|constexpr_since=26
|desc=Computes the square root of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, square root of `num` (mathjax-or|\({\small \sqrt{num} }\)|), is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error occurs if `num` is less than zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is less than -0, `FE_INVALID` is raised and NaN is returned.
* If the argument is +∞ or ±0, it is returned, unmodified.
* If the argument is NaN, NaN is returned.

## Notes

`std::sqrt` is required by the IEEE standard to be correctly rounded from the infinitely precise result. In particular, the exact result is produced if it can be represented in the floating-point type. The only other operations which require this are the arithmetic operators and the function `std::fma`. Other functions, including `std::pow`, are not so constrained.

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
    // normal use
    std::cout << "sqrt(100) = " << std::sqrt(100) << '\n'
              << "sqrt(2) = " << std::sqrt(2) << '\n'
              << "golden ratio = " << (1 + std::sqrt(5)) / 2 << '\n';

    // special values
    std::cout << "sqrt(-0) = " << std::sqrt(-0.0) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "sqrt(-1.0) = " << std::sqrt(-1) << '\n';
    if (errno == EDOM)
        std::cout << "    errno = EDOM " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
sqrt(100) = 10
sqrt(2) = 1.41421
golden ratio = 1.61803
sqrt(-0) = -0
sqrt(-1.0) = -nan
    errno = EDOM Numerical argument out of domain
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc pow | (see dedicated page) |
| cpp/numeric/math/dsc cbrt | (see dedicated page) |
| cpp/numeric/math/dsc hypot | (see dedicated page) |
| cpp/numeric/complex/dsc sqrt | (see dedicated page) |
| cpp/numeric/valarray/dsc sqrt | (see dedicated page) |

