---
title: MATH_ERRNO
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/math_errhandling
---


# MATH_ERRNO, MATH_ERREXCEPT, math_errhandling


```cpp
**Header:** `<`cmath`>`
dcl|since=c++11|
#define MATH_ERRNO        1
dcl|since=c++11|
#define MATH_ERREXCEPT    2
dcl|since=c++11|
#define math_errhandling  /*implementation defined*/
```

The macro constant `math_errhandling` expands to an expression of type `int` that is either equal to `MATH_ERRNO`, or equal to `MATH_ERREXCEPT`, or equal to their bitwise OR (`MATH_ERRNO ).
The value of `math_errhandling` indicates the type of error handling that is performed by the floating-point operators and functions:


| Item | Description |
|------|-------------|
| **Constant** | Explanation |

If the implementation supports IEEE floating-point arithmetic (IEC 60559), `math_errhandling & MATH_ERREXCEPT` is required to be non-zero.
The following floating-point error conditions are recognized:


| - |
| Condition | Explanation | errno | Floating-point exception | Example |
| - |
| Domain error |
| The argument is outside the range in which the operation is mathematically defined (the description of [[cpp/numeric/math | each function]] lists the required domain errors) |
| lc | EDOM |
| lc | FE_INVALID |
| c | std::acos(2) |
| - |
| Pole error |
| The mathematical result of the function is exactly infinite or undefined |
| lc | ERANGE |
| lc | FE_DIVBYZERO |
| c | std::log(0.0), c | 1.0 / 0.0 |
| - |
| Range error due to overflow |
| The mathematical result is finite, but becomes infinite after rounding, or becomes the largest representable finite value after rounding down |
| lc | ERANGE |
| lc | FE_OVERFLOW |
| c | std::pow(DBL_MAX, 2) |
| - |
| Range error due to underflow |
| The result is non-zero, but becomes zero after rounding, or becomes subnormal with a loss of precision |
| lc | ERANGE or unchanged (implementation-defined) |
| lc | FE_UNDERFLOW or nothing (implementation-defined) |
| c | DBL_TRUE_MIN / 2 |
| - |
| Inexact result |
| The result has to be rounded to fit in the destination type |
| Unchanged |
| lc | FE_INEXACT or nothing (unspecified) |
| c | std::sqrt(2), c | 1.0 / 10.0 |


## Notes

Whether `FE_INEXACT` is raised by the mathematical library functions is unspecified in general, but may be explicitly specified in the description of the function (e.g. `std::rint` vs `std::nearbyint`).
Before C++11, floating-point exceptions were not specified, `EDOM` was required for any domain error, `ERANGE` was required for overflows and implementation-defined for underflows.

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
    std::cout << "MATH_ERRNO is "
              << (math_errhandling & MATH_ERRNO ? "set" : "not set") << '\n'
              << "MATH_ERREXCEPT is "
              << (math_errhandling & MATH_ERREXCEPT ? "set" : "not set") << '\n';
    std::feclearexcept(FE_ALL_EXCEPT);
    errno = 0;
    std::cout <<  "log(0) = " << std::log(0) << '\n';
    if (errno == ERANGE)
        std::cout << "errno = ERANGE (" << std::strerror(errno) << ")\n";
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "FE_DIVBYZERO (pole error) reported\n";
}
```


**Output:**
```
MATH_ERRNO is set
MATH_ERREXCEPT is set
log(0) = -inf
errno = ERANGE (Numerical result out of range)
FE_DIVBYZERO (pole error) reported
```


## See also


| cpp/numeric/fenv/dsc FE_exceptions | (see dedicated page) |
| cpp/error/dsc errno | (see dedicated page) |

