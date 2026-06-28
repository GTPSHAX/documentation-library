---
title: std::sph_legendre
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/sph_legendre
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       sph_legendre ( unsigned l, unsigned m, float theta );
double      sph_legendre ( unsigned l, unsigned m, double theta );
long double sph_legendre ( unsigned l, unsigned m, long double theta );
|since2=c++23|dcl2=
/* floating-point-type */ sph_legendre( unsigned l, unsigned m,
/* floating-point-type */ theta );
dcl|num=2|since=c++17|
float       sph_legendref( unsigned l, unsigned m, float theta );
dcl|num=3|since=c++17|
long double sph_legendrel( unsigned l, unsigned m, long double theta );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      sph_legendre ( unsigned l, unsigned m, Integer theta );
```

@1-3@ Computes the [Spherical harmonics#Orthogonality and normalization|spherical associated Legendre function](https://en.wikipedia.org/wiki/Spherical harmonics#Orthogonality and normalization|spherical associated Legendre function) of degree `l`, order `m`, and polar angle `theta`.<sup>(since C++23)</sup>  The library provides overloads of `std::sph_legendre` for all cv-unqualified floating-point types as the type of the parameter `theta`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `l` - degree
- `m` - order
- `theta` - polar angle, measured in radians

## Return value

If no errors occur, returns the value of the spherical associated Legendre function (that is, spherical harmonic with ϕ = 0) of `l`, `m`, and `theta`, where the spherical harmonic function is defined as $1=Y where $P is `std::assoc_legendre(l, m, x)`) and $.
Note that the [https://mathworld.wolfram.com/Condon-ShortleyPhase.html Condon-Shortley phase term ] $(-1) is included in this definition because it is omitted from the definition of $P in `std::assoc_legendre`.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $l≥128$, the behavior is implementation-defined.

## Notes

An implementation of the spherical harmonic function is available in [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_poly/sph_harm.html boost.math], and it reduces to this function when called with the parameter phi set to zero.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>

int main()
{
    // spot check for l=3, m=0
    double x = 1.2345;
    std::cout << "Y_3^0(" << x << ") = " << std::sph_legendre(3, 0, x) << '\n';

    // exact solution
    std::cout << "exact solution = "
              << 0.25 * std::sqrt(7 / std::numbers::pi)
                  * (5 * std::pow(std::cos(x), 3) - 3 * std::cos(x))
              << '\n';
}
```


**Output:**
```
Y_3^0(1.2345) = -0.302387
exact solution = -0.302387
```


## See also


| cpp/numeric/special_functions/dsc assoc_legendre | (see dedicated page) |


## External links

