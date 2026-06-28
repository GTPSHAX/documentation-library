---
title: std::comp_ellint_2
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/comp_ellint_2
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       comp_ellint_2 ( float k );
double      comp_ellint_2 ( double k );
long double comp_ellint_2 ( long double k );
|since2=c++23|dcl2=
/* floating-point-type */ comp_ellint_2( /* floating-point-type */ k );
dcl|num=2|since=c++17|
float       comp_ellint_2f( float k );
dcl|num=3|since=c++17|
long double comp_ellint_2l( long double k );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      comp_ellint_2 ( Integer k );
```

@1-3@ Computes the [Elliptic integral#Complete elliptic integral of the second kind|complete elliptic integral of the second kind](https://en.wikipedia.org/wiki/Elliptic integral#Complete elliptic integral of the second kind|complete elliptic integral of the second kind) of `k`.<sup>(since C++23)</sup>  The library provides overloads of `std::comp_ellint_2` for all cv-unqualified floating-point types as the type of the parameter `k`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `k` - elliptic modulus or eccentricity (a floating-point or integer value)

## Return value

If no errors occur, value of the complete elliptic integral of the second kind of `k`, that is `std::ellint_2(k, π/2)`, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $, a domain error may occur.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/ellint/ellint_2.html available in boost.math].
The perimeter of an ellipse with eccentricity `k` and semimajor axis $a$ equals  $4aE(k)$, where $E$ is `std::comp_ellint_2`. When eccentricity equals $0$, the ellipse degenerates to a circle with radius $a$ and the perimeter equals $2πa$, so $1=E(0) = π/2$. When eccentricity equals $1$, the ellipse degenerates to a line of length 2a, whose perimeter is $4a$, so $1=E(1) = 1$.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>

int main()
{
    constexpr double hpi = std::numbers::pi / 2.0;

    std::cout << "E(0) = " << std::comp_ellint_2(0) << '\n'
              << "π/2 = " << hpi << '\n'
              << "E(1) = " << std::comp_ellint_2(1) << '\n'
              << "E(1, π/2) = " << std::ellint_2(1, hpi) << '\n';
}
```


**Output:**
```
E(0) = 1.5708
π/2 = 1.5708
E(1) = 1
E(1, π/2) = 1
```


## See also


| cpp/numeric/special_functions/dsc ellint_2 | (see dedicated page) |


## External links

