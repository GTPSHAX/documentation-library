---
title: std::cyl_bessel_k
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/cyl_bessel_k
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       cyl_bessel_k ( float nu, float x );
double      cyl_bessel_k ( double nu, double x );
long double cyl_bessel_k ( long double nu, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ cyl_bessel_k( /* floating-point-type */ nu,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       cyl_bessel_kf( float nu, float x );
dcl|num=3|since=c++17|
long double cyl_bessel_kl( long double nu, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
cyl_bessel_k( Arithmetic1 nu, Arithmetic2 x );
```

@1-3@ Computes the [Bessel function#Modified Bessel functions: I.CE.B1 .2C K.CE.B1|irregular modified cylindrical Bessel function](https://en.wikipedia.org/wiki/Bessel function#Modified Bessel functions: I.CE.B1 .2C K.CE.B1|irregular modified cylindrical Bessel function) (also known as modified Bessel function of the second kind) of `nu` and `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::cyl_bessel_k` for all cv-unqualified floating-point types as the type of the parameters `nu` and `x`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `nu` - the order of the function
- `x` - the argument of the function

## Return value

If no errors occur, value of the irregular modified cylindrical Bessel function (modified Bessel function of the second kind) of `nu` and `x`, is returned, that is $K (where $I is `std::cyl_bessel_i(nu, x)`) for $x≥0$ and non-integer `nu`; for integer `nu` a limit is used.

## Error handling

Errors may be reported as specified in `math_errhandling`:
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $nu≥128$, the behavior is implementation-defined.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/bessel/mbessel.html available in boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>

int main()
{
    double pi = std::numbers::pi;
    const double x = 1.2345;

    // spot check for nu == 0.5
    std::cout << "K_.5(" << x << ") = " << std::cyl_bessel_k(.5, x) << '\n'
              << "calculated via I = "
              << (pi / 2) * (std::cyl_bessel_i(-.5, x)
                 - std::cyl_bessel_i(.5, x)) / std::sin(.5 * pi) << '\n';
}
```


**Output:**
```
K_.5(1.2345) = 0.32823
calculated via I = 0.32823
```


## See also


| cpp/numeric/special_functions/dsc cyl_bessel_i | (see dedicated page) |
| cpp/numeric/special_functions/dsc cyl_bessel_j | (see dedicated page) |


## External links

