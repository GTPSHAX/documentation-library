---
title: std::cyl_bessel_i
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/cyl_bessel_i
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       cyl_bessel_i ( float nu, float x );
double      cyl_bessel_i ( double nu, double x );
long double cyl_bessel_i ( long double nu, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ cyl_bessel_i( /* floating-point-type */ nu,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       cyl_bessel_if( float nu, float x );
dcl|num=3|since=c++17|
long double cyl_bessel_il( long double nu, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
cyl_bessel_i( Arithmetic1 nu, Arithmetic2 x );
```

@1-3@ Computes the [Bessel function#Modified Bessel functions: I.CE.B1 .2C_K.CE.B1|regular modified cylindrical Bessel function](https://en.wikipedia.org/wiki/Bessel function#Modified Bessel functions: I.CE.B1 .2C_K.CE.B1|regular modified cylindrical Bessel function) of `nu` and `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::cyl_bessel_i` for all cv-unqualified floating-point types as the type of the parameters `nu` and `x`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `nu` - the order of the function
- `x` - the argument of the function

## Return value

If no errors occur, value of the regular modified cylindrical Bessel function of `nu` and `x`, that is $1=I (for $x≥0$), is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $nu≥128$, the behavior is implementation-defined.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/bessel/mbessel.html  available in boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    // spot check for nu == 0
    const double x = 1.2345;
    std::cout << "I_0(" << x << ") = " << std::cyl_bessel_i(0, x) << '\n';

    // series expansion for I_0
    double fct = 1;
    double sum = 0;
    for (int k = 0; k < 5; fct *= ++k)
    {
        sum += std::pow(x / 2, 2 * k) / std::pow(fct, 2);
        std::cout << "sum = " << sum << '\n';
    }
}
```


**Output:**
```
I_0(1.2345) = 1.41886
sum = 1
sum = 1.381
sum = 1.41729
sum = 1.41882
sum = 1.41886
```


## See also


| cpp/numeric/special_functions/dsc cyl_bessel_j | (see dedicated page) |


## External links

