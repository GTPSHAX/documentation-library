---
title: std::acos
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/acos
---

cpp/numeric/math/declarations
|family=acos
|param1=num
|constexpr_since=26
|desc=Computes the principal value of the arc cosine of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the arc cosine of `num` ($arccos(num)$) in the range $[0, &pi;]$, is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error occurs if `num` is outside the range .
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is $+1$, the value `+0` is returned.
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
    std::cout << "acos(-1) = " << std::acos(-1) << '\n'
              << "acos(0.0) = " << std::acos(0.0) << '\n'
              << "2*acos(0.0) = " << 2 * std::acos(0) << '\n'
              << "acos(0.5) = " << std::acos(0.5) << '\n'
              << "3*acos(0.5) = " << 3 * std::acos(0.5) << '\n'
              << "acos(1) = " << std::acos(1) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "acos(1.1) = " << std::acos(1.1) << '\n';

    if (errno == EDOM)
        std::cout << "    errno == EDOM: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised" << '\n';
}
```


**Output:**
```
acos(-1) = 3.14159
acos(0.0) = 1.5708
2*acos(0.0) = 3.14159
acos(0.5) = 1.0472
3*acos(0.5) = 3.14159
acos(1) = 0
acos(1.1) = nan
    errno == EDOM: Numerical argument out of domain
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc asin | (see dedicated page) |
| cpp/numeric/math/dsc atan | (see dedicated page) |
| cpp/numeric/math/dsc atan2 | (see dedicated page) |
| cpp/numeric/math/dsc cos | (see dedicated page) |
| cpp/numeric/complex/dsc acos | (see dedicated page) |
| cpp/numeric/valarray/dsc acos | (see dedicated page) |

