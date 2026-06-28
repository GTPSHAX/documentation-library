---
title: std::fdim
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fdim
---

cpp/numeric/math/declarations
|family=fdim
|param1=x
|param2=y
|constexpr_since=23
|desc=Returns the positive difference between `x` and `y`, that is, if `x > y`, returns `x - y`, otherwise (i.e. if `1=x <= y`) returns `+0`.

## Parameters


### Parameters

- `x, y` - floating-point or integer values

## Return value

If successful, returns the positive difference between `x` and `y`.
If a range error due to overflow occurs, `HUGE_VAL|+HUGE_VAL`, `+HUGE_VALF`, or `+HUGE_VALL` is returned.
If a range error due to underflow occurs, the correct value (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If either argument is NaN, NaN is returned.

## Notes

Equivalent to `std::fmax(x - y, 0)`, except for the NaN handling requirements.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <cstring>
#include <iostream>

#ifndef __GNUC__
#pragma STDC FENV_ACCESS ON
#endif

int main()
{
    std::cout << "fdim(4, 1) = " << std::fdim(4, 1) << '\n'
              << "fdim(1, 4) = " << std::fdim(1, 4) << '\n'
              << "fdim(4,-1) = " << std::fdim(4, -1) << '\n'
              << "fdim(1,-4) = " << std::fdim(1, -4) << '\n';

    // error handling 
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "fdim(1e308, -1e308) = " << std::fdim(1e308, -1e308) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout << "    FE_OVERFLOW raised\n";
}
```


**Output:**
```
fdim(4, 1) = 3
fdim(1, 4) = 0
fdim(4,-1) = 5
fdim(1,-4) = 5
fdim(1e308, -1e308) = inf
    errno == ERANGE: Numerical result out of range
    FE_OVERFLOW raised
```


## See also


| cpp/numeric/math/dsc abs | (see dedicated page) |
| cpp/numeric/math/dsc fmax | (see dedicated page) |

