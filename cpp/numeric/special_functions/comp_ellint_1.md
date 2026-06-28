---
title: std::comp_ellint_1
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/comp_ellint_1
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
double      comp_ellint_1 ( double k );
float       comp_ellint_1 ( float k );
long double comp_ellint_1 ( long double k );
|since2=c++23|dcl2=
/* floating-point-type */ comp_ellint_1( /* floating-point-type */ k );
dcl|num=2|since=c++17|
float       comp_ellint_1f( float k );
dcl|num=3|since=c++17|
long double comp_ellint_1l( long double k );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      comp_ellint_1 ( Integer k );
```

@1-3@ Computes the [Elliptic integral#Complete elliptic integral of the first kind|complete elliptic integral of the first kind](https://en.wikipedia.org/wiki/Elliptic integral#Complete elliptic integral of the first kind|complete elliptic integral of the first kind) of `k`.<sup>(since C++23)</sup>  The library provides overloads of `std::comp_ellint_1` for all cv-unqualified floating-point types as the type of the parameter `k`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `k` - elliptic modulus or eccentricity (a floating-point or integer value)

## Return value

If no errors occur, value of the complete elliptic integral of the first kind of `k`, that is `std::ellint_1(k, π/2)`, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $, a domain error may occur.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/ellint/ellint_1.html available in boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>

int main()
{
    constexpr double π{std::numbers::pi};

    std::cout << "K(0) ≈ " << std::comp_ellint_1(0) << '\n'
              << "π/2 ≈ " << π / 2 << '\n'
              << "K(0.5) ≈ " << std::comp_ellint_1(0.5) << '\n'
              << "F(0.5, π/2) ≈ " << std::ellint_1(0.5, π / 2) << '\n'
              << "The period of a pendulum length 1m at 10° initial angle ≈ "
              << 4 * std::sqrt(1 / 9.80665) * std::comp_ellint_1(std::sin(π / 18 / 2))
              << "s,\n" "whereas the linear approximation gives ≈ "
              << 2 * π * std::sqrt(1 / 9.80665) << '\n';
}
```


**Output:**
```
K(0) ≈ 1.5708
π/2 ≈ 1.5708
K(0.5) ≈ 1.68575
F(0.5, π/2) ≈ 1.68575
The period of a pendulum length 1 m at 10° initial angle ≈ 2.01024s,
whereas the linear approximation gives ≈ 2.00641
```


## See also


| cpp/numeric/special_functions/dsc ellint_1 | (see dedicated page) |


## External links

