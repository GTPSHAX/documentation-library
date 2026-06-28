---
title: std::atan2
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/atan2
---

cpp/numeric/math/declarations
|family=atan2
|param1=y
|param2=x
|constexpr_since=26
|desc=Computes the arc tangent of `y / x` using the signs of arguments to determine the correct quadrant.

## Parameters


### Parameters

- `y, x` - floating-point or integer values

## Return value

If no errors occur, the arc tangent of `y / x` ($arctan() in the range $[-&pi;, +&pi;]$ radians, is returned.
If a domain error occurs, an implementation-defined value is returned (NaN where supported).
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
Domain error may occur if `x` and `y` are both zero.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If `x` and `y` are both zero, domain error ''does not'' occur.
* If `x` and `y` are both zero, range error does not occur either.
* If `y` is zero, pole error does not occur.
* If `y` is ±0 and `x` is negative or -0, ±&pi; is returned.
* If `y` is ±0 and `x` is positive or +0, ±0 is returned.
* If `y` is ±∞ and `x` is finite, ±&pi;/2 is returned.
* If `y` is ±∞ and `x` is -∞, ±3&pi;/4 is returned.
* If `y` is ±∞ and `x` is +∞, ±&pi;/4 is returned.
* If `x` is ±0 and `y` is negative, -&pi;/2 is returned.
* If `x` is ±0 and `y` is positive, +&pi;/2 is returned.
* If `x` is -∞ and `y` is finite and positive, +&pi; is returned.
* If `x` is -∞ and `y` is finite and negative, -&pi; is returned.
* If `x` is +∞ and `y` is finite and positive, +0 is returned.
* If `x` is +∞ and `y` is finite and negative, -0 is returned.
* If either `x` is NaN or `y` is NaN, NaN is returned.

## Notes

`std::atan2(y, x)` is equivalent to `std::arg(std::complex<std::common_type_t<decltype(x), decltype(y)>>(x, y))`.
[https://pubs.opengroup.org/onlinepubs/9699919799/functions/atan2.html POSIX specifies] that in case of underflow, the value `y / x` is returned, and if that is not supported, an implementation-defined value no greater than `DBL_MIN`, `FLT_MIN`, and `LDBL_MIN` is returned.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

void print_coordinates(int x, int y)
{
    std::cout << std::showpos
              << "(x:" << x << ", y:" << y << ") cartesian is "
              << "(r:" << std::hypot(x, y)
              << ", phi:" << std::atan2(y, x) << ") polar\n";
}

int main()
{
    // normal usage: the signs of the two arguments determine the quadrant
    print_coordinates(+1, +1); // atan2( 1,  1) =  +pi/4, Quad I
    print_coordinates(-1, +1); // atan2( 1, -1) = +3pi/4, Quad II
    print_coordinates(-1, -1); // atan2(-1, -1) = -3pi/4, Quad III
    print_coordinates(+1, -1); // atan2(-1,  1) =  -pi/4, Quad IV

    // special values
    std::cout << std::noshowpos
              << "atan2(0, 0) = " << atan2(0, 0) << '\n'
              << "atan2(0,-0) = " << atan2(0, -0.0) << '\n'
              << "atan2(7, 0) = " << atan2(7, 0) << '\n'
              << "atan2(7,-0) = " << atan2(7, -0.0) << '\n';
}
```


**Output:**
```
(x:+1, y:+1) cartesian is (r:1.41421, phi:0.785398) polar
(x:-1, y:+1) cartesian is (r:1.41421, phi:2.35619) polar
(x:-1, y:-1) cartesian is (r:1.41421, phi:-2.35619) polar
(x:+1, y:-1) cartesian is (r:1.41421, phi:-0.785398) polar
atan2(0, 0) = 0
atan2(0,-0) = 3.14159
atan2(7, 0) = 1.5708
atan2(7,-0) = 1.5708
```


## See also


| cpp/numeric/math/dsc asin | (see dedicated page) |
| cpp/numeric/math/dsc acos | (see dedicated page) |
| cpp/numeric/math/dsc atan | (see dedicated page) |
| cpp/numeric/complex/dsc arg | (see dedicated page) |
| cpp/numeric/valarray/dsc atan2 | (see dedicated page) |

