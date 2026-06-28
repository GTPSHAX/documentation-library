---
title: std::sph_bessel
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/sph_bessel
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       sph_bessel ( unsigned int n, float x );
double      sph_bessel ( unsigned int n, double x );
long double sph_bessel ( unsigned int n, long double x );
|since2=c++23|dcl2=
/*floating-point-type*/ sph_bessel( unsigned int n,
/*floating-point-type*/ x );
dcl|num=2|since=c++17|
float       sph_besself( unsigned int n, float x );
dcl|num=3|since=c++17|
long double sph_bessell( unsigned int n, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      sph_bessel ( unsigned int n, Integer x );
```

@1-3@ Computes the [Bessel function#Spherical Bessel functions: jn.2C yn|spherical Bessel function of the first kind](https://en.wikipedia.org/wiki/Bessel function#Spherical Bessel functions: jn.2C yn|spherical Bessel function of the first kind) of `n` and `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::sph_bessel` for all cv-unqualified floating-point types as the type of the parameter `x`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `n` - the order of the function
- `x` - the argument of the function

## Return value

If no errors occur, returns the value of the spherical Bessel function of the first kind of `n` and `x`, that is $1=j where $J is `std::cyl_bessel_j(n, x)` and $x≥0$.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $n≥128$, the behavior is implementation-defined.

## Notes

An implementation of this function is also available in [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/bessel/sph_bessel.html boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    // spot check for n == 1
    double x = 1.2345;
    std::cout << "j_1(" << x << ") = " << std::sph_bessel(1, x) << '\n';

    // exact solution for j_1
    std::cout << "sin(x)/x² - cos(x)/x = "
              << std::sin(x) / (x * x) - std::cos(x) / x << '\n';
}
```


**Output:**
```
j_1(1.2345) = 0.352106
sin(x)/x² - cos(x)/x = 0.352106
```


## See also


| cpp/numeric/special_functions/dsc cyl_bessel_j | (see dedicated page) |
| cpp/numeric/special_functions/dsc sph_neumann | (see dedicated page) |


## External links

