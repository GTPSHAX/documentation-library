---
title: std::cyl_neumann
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/cyl_neumann
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       cyl_neumann ( float nu, float x );
double      cyl_neumann ( double nu, double x );
long double cyl_neumann ( long double nu, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ cyl_neumann( /* floating-point-type */ nu,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       cyl_neumannf( float nu, float x );
dcl|num=3|since=c++17|
long double cyl_neumannl( long double nu, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
cyl_neumann( Arithmetic1 nu, Arithmetic2 x );
```

@1-3@ Computes the [Bessel function#Bessel functions of the second kind: Y.CE.B1|cylindrical Neumann function](https://en.wikipedia.org/wiki/Bessel function#Bessel functions of the second kind: Y.CE.B1|cylindrical Neumann function) (also known as Bessel function of the second kind or Weber function) of `nu` and `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::cyl_neumann` for all cv-unqualified floating-point types as the type of the parameters `nu` and `x`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `nu` - the order of the function
- `x` - the argument of the function

## Return value

If no errors occur, value of the cylindrical Neumann function (Bessel function of the second kind) of `nu` and `x`, is returned, that is $1=N (where $J is `std::cyl_bessel_j(nu, x)`) for $x≥0$ and non-integer `nu`; for integer `nu` a limit is used.

## Error handling

Errors may be reported as specified in `math_errhandling`:
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $nu≥128$, the behavior is implementation-defined.

## Notes

An implementation of this function is also available in [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/bessel/bessel_first.html boost.math].

## Example


### Example

```cpp
#include <cassert>
#include <cmath>
#include <iostream>
#include <numbers>

const double π = std::numbers::pi; // or std::acos(-1) in pre C++20

// To calculate the cylindrical Neumann function via cylindrical Bessel function of the
// first kind we have to implement J, because the direct invocation of the
// std::cyl_bessel_j(nu, x), per formula above,
// for negative nu raises 'std::domain_error': Bad argument in __cyl_bessel_j.

double J_neg(double nu, double x)
{
    return std::cos(-nu * π) * std::cyl_bessel_j(-nu, x)
          -std::sin(-nu * π) * std::cyl_neumann(-nu, x);
}

double J_pos(double nu, double x)
{
    return std::cyl_bessel_j(nu, x);
}

double J(double nu, double x)
{
    return nu < 0.0 ? J_neg(nu, x) : J_pos(nu, x);
}

int main()
{
    std::cout << "spot checks for nu == 0.5\n" << std::fixed << std::showpos;
    const double nu = 0.5;
    for (double x = 0.0; x <= 2.0; x += 0.333)
    {
        const double n = std::cyl_neumann(nu, x);
        const double j = (J(nu, x) * std::cos(nu * π) - J(-nu, x)) / std::sin(nu * π);
        std::cout << "N_.5(" << x << ") = " << n << ", calculated via J = " << j << '\n';
        assert(n == j);
    }
}
```


**Output:**
```
spot checks for nu == 0.5
N_.5(+0.000000) = -inf, calculated via J = -inf
N_.5(+0.333000) = -1.306713, calculated via J = -1.306713
N_.5(+0.666000) = -0.768760, calculated via J = -0.768760
N_.5(+0.999000) = -0.431986, calculated via J = -0.431986
N_.5(+1.332000) = -0.163524, calculated via J = -0.163524
N_.5(+1.665000) = +0.058165, calculated via J = +0.058165
N_.5(+1.998000) = +0.233876, calculated via J = +0.233876
```


## See also


| cpp/numeric/special_functions/dsc cyl_bessel_i | (see dedicated page) |
| cpp/numeric/special_functions/dsc cyl_bessel_j | (see dedicated page) |
| cpp/numeric/special_functions/dsc cyl_bessel_k | (see dedicated page) |


## External links

