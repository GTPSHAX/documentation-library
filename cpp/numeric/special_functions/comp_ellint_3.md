---
title: std::comp_ellint_3
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/comp_ellint_3
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       comp_ellint_3 ( float k, float nu );
double      comp_ellint_3 ( double k, double nu );
long double comp_ellint_3 ( long double k, long double nu );
|since2=c++23|dcl2=
/* floating-point-type */ comp_ellint_3( /* floating-point-type */ k,
/* floating-point-type */ nu );
dcl|num=2|since=c++17|
float       comp_ellint_3f( float k, float nu );
dcl|num=3|since=c++17|
long double comp_ellint_3l( long double k, long double nu );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
comp_ellint_3( Arithmetic1 k, Arithmetic2 nu );
```

@1-3@ Computes the [Elliptic integral#Complete elliptic integral of the third kind|complete elliptic integral of the third kind](https://en.wikipedia.org/wiki/Elliptic integral#Complete elliptic integral of the third kind|complete elliptic integral of the third kind) of the arguments `k` and `nu`.<sup>(since C++23)</sup>  The library provides overloads of `std::comp_ellint_3` for all cv-unqualified floating-point types as the type of the parameters `k` and `nu`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `k` - elliptic modulus or eccentricity (a floating-point or integer value)
- `nu` - elliptic characteristic (a floating-point or integer value)

## Return value

If no errors occur, value of the complete elliptic integral of the third kind of `k` and `nu`, that is `std::ellint_3(k, nu, π/2)`, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported
* If $, a domain error may occur

## Notes

An implementation of this function is also available in [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/ellint/ellint_3.html boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << std::fixed
              << "Π(0.5,0) = " << std::comp_ellint_3(0.5, 0) << '\n'
              << "K(0.5)   = " << std::comp_ellint_1(0.5) << '\n'
              << "Π(0,0)   = " << std::comp_ellint_3(0, 0) << '\n'
              << "π/2      = " << std::acos(-1) / 2 << '\n'
              << "Π(0.5,1) = " << std::comp_ellint_3(0.5, 1) << '\n';
}
```


**Output:**
```
Π(0.5,0) = 1.685750
K(0.5)   = 1.685750
Π(0,0)   = 1.570796
π/2      = 1.570796
Π(0.5,1) = inf
```


## See also


| cpp/numeric/special_functions/dsc ellint_3 | (see dedicated page) |


## External links

