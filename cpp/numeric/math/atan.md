---
title: std::atan
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/atan
---

cpp/numeric/math/declarations
|family=atan
|param1=num
|constexpr_since=26
|desc=Computes the principal value of the arc tangent of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the arc tangent of `num` ($arctan(num)$) in the range $[-  radians, is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, it is returned unmodified.
* If the argument is +∞, +&pi;/2 is returned.
* If the argument is -∞, -&pi;/2 is returned.
* If the argument is NaN, NaN is returned.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/atan.html POSIX specifies] that in case of underflow, `num` is returned unmodified, and if that is not supported, an implementation-defined value no greater than `cpp/types/climits#Limits of floating-point types|DBL_MIN`, `FLT_MIN`, and `LDBL_MIN` is returned.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << "atan(1) = " << std::atan(1) << '\n'
              << "4*atan(1) = " << 4 * std::atan(1) << '\n';

    // special values
    std::cout << "atan(Inf) = " << std::atan(INFINITY) << '\n'
              << "2*atan(Inf) = " << 2 * std::atan(INFINITY) << '\n'
              << "atan(-0.0) = " << std::atan(-0.0) << '\n'
              << "atan(+0.0) = " << std::atan(0) << '\n';
}
```


**Output:**
```
atan(1) = 0.785398
4*atan(1) = 3.14159
atan(Inf) = 1.5708
2*atan(Inf) = 3.14159
atan(-0.0) = -0
atan(+0.0) = 0
```


## See also


| cpp/numeric/math/dsc asin | (see dedicated page) |
| cpp/numeric/math/dsc acos | (see dedicated page) |
| cpp/numeric/math/dsc atan2 | (see dedicated page) |
| cpp/numeric/math/dsc tan | (see dedicated page) |
| cpp/numeric/complex/dsc atan | (see dedicated page) |
| cpp/numeric/valarray/dsc atan | (see dedicated page) |

