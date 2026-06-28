---
title: std::asin
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/asin
---

cpp/numeric/math/declarations
|family=asin
|param1=num
|constexpr_since=26
|desc=Computes the principal value of the arc sine of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the arc sine of `num` ($arcsin(num)$) in the range $[- , is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error occurs if `num` is outside the range .
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, it is returned unmodified.
* If $, a domain error occurs and NaN is returned.
* if the argument is NaN, NaN is returned.

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
    std::cout << "asin(1.0) = " << asin(1) << '\n'
              << "2*asin(1.0) = " << 2 * asin(1) << '\n'
              << "asin(-0.5) = " << asin(-0.5) << '\n'
              << "6*asin(-0.5) =" << 6 * asin(-0.5) << '\n';

    // special values
    std::cout << "asin(0.0) = " << asin(0) << " asin(-0.0)=" << asin(-0.0) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "asin(1.1) = " << asin(1.1) << '\n';

    if (errno == EDOM)
        std::cout << "    errno == EDOM: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised" << '\n';
}
```


**Output:**
```
asin(1.0) = 1.5708
2*asin(1.0) = 3.14159
asin(-0.5) = -0.523599
6*asin(-0.5) = -3.14159
asin(0.0) = 0 asin(-0.0)=-0
asin(1.1) = nan
    errno == EDOM: Numerical argument out of domain
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc acos | (see dedicated page) |
| cpp/numeric/math/dsc atan | (see dedicated page) |
| cpp/numeric/math/dsc atan2 | (see dedicated page) |
| cpp/numeric/math/dsc sin | (see dedicated page) |
| cpp/numeric/complex/dsc asin | (see dedicated page) |
| cpp/numeric/valarray/dsc asin | (see dedicated page) |

