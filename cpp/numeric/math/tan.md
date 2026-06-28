---
title: std::tan
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/tan
---

cpp/numeric/math/declarations
|family=tan
|param1=num
|constexpr_since=26
|desc=Computes the tangent of `num` (measured in radians).

## Parameters


### Parameters

- `num` - floating-point or integer value representing angle in radians

## Return value

If no errors occur, the tangent of `num` ($tan(num)$) is returned.
rrev|until=c++11|
The result may have little or no significance if the magnitude of `num` is large.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* if the argument is ±0, it is returned unmodified.
* if the argument is ±∞, NaN is returned and `FE_INVALID` is raised.
* if the argument is NaN, NaN is returned.

## Notes

The case where the argument is infinite is not specified to be a domain error in C (to which C++ defers), but it is defined as a [https://pubs.opengroup.org/onlinepubs/9699919799/functions/tan.html domain error in POSIX].
The function has mathematical poles at $π(1/2 + n)$; however no common floating-point representation is able to represent π/2 exactly, thus there is no value of the argument for which a pole error occurs.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <iostream>

// #pragma STDC FENV_ACCESS ON
const double pi = std::acos(-1); // or C++20's std::numbers::pi

int main()
{
    // typical usage
    std::cout << "tan(1*pi/4) = " << std::tan(1*pi/4) << '\n' // 45°
              << "tan(3*pi/4) = " << std::tan(3*pi/4) << '\n' // 135°
              << "tan(5*pi/4) = " << std::tan(5*pi/4) << '\n' // -135°
              << "tan(7*pi/4) = " << std::tan(7*pi/4) << '\n'; // -45°

    // special values
    std::cout << "tan(+0) = " << std::tan(0.0) << '\n'
              << "tan(-0) = " << std::tan(-0.0) << '\n';

    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "tan(INFINITY) = " << std::tan(INFINITY) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
tan(1*pi/4) = 1
tan(3*pi/4) = -1
tan(5*pi/4) = 1
tan(7*pi/4) = -1
tan(+0) = 0
tan(-0) = -0
tan(INFINITY) = -nan
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc sin | (see dedicated page) |
| cpp/numeric/math/dsc cos | (see dedicated page) |
| cpp/numeric/math/dsc atan | (see dedicated page) |
| cpp/numeric/complex/dsc tan | (see dedicated page) |
| cpp/numeric/valarray/dsc tan | (see dedicated page) |

