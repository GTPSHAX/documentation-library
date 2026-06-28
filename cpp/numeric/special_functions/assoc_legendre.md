---
title: std::assoc_legendre
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/assoc_legendre
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       assoc_legendre ( unsigned int n, unsigned int m, float x );
double      assoc_legendre ( unsigned int n, unsigned int m, double x );
long double assoc_legendre ( unsigned int n, unsigned int m, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ assoc_legendre( unsigned int n, unsigned int m,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       assoc_legendref( unsigned int n, unsigned int m, float x );
dcl|num=3|since=c++17|
long double assoc_legendrel( unsigned int n, unsigned int m, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      assoc_legendre ( unsigned int n, unsigned int m, Integer x );
```

@1-3@ Computes the [Associated Legendre polynomials](https://en.wikipedia.org/wiki/Associated Legendre polynomials) of the degree `n`, order `m`, and argument `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::assoc_legendre` for all cv-unqualified floating-point types as the type of the parameter `x`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `n` - the degree of the polynomial, an unsigned integer value
- `m` - the order of the polynomial, an unsigned integer value
- `x` - the argument, a floating-point or integer value

## Return value

If no errors occur, value of the associated Legendre polynomial } of `x`, that is mathjax-or|1=\((1 - x^2) ^ {m/2} \: \frac{ \mathsf{d} ^ m}{ \mathsf{d}x ^ m} \, \mathsf{P}_n(x)\)|2=(1-x) P(x), is returned (where } is the unassociated Legendre polynomial, `std::legendre(n, x)`).
Note that the [https://mathworld.wolfram.com/Condon-ShortleyPhase.html Condon-Shortley phase term]  is omitted from this definition.

## Error handling

Errors may be reported as specified in math_errhandling
* If the argument is NaN, NaN is returned and domain error is not reported
* If $, a domain error may occur
* If `n` is greater or equal to 128, the behavior is implementation-defined

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_poly/legendre.html available in boost.math] as `boost::math::legendre_p`, except that the boost.math definition includes the Condon-Shortley phase term.
The first few associated Legendre polynomials are:


| - |
| Function |
| Polynomial |
| - style="height:45px;" |
| nbsp | 4co | 1=assoc_legendre(0, 0, x)nbsp | 4 | 1 |
| - style="height:45px;" |
| co | 1=assoc_legendre(1, 0, x) | math | x |
| - style="height:45px;" |
| co | 1=assoc_legendre(1, 1, x) | math | (1 - xsu | p=2)su | p=1/2 |
| - style="height:45px;" |
| co | 1=assoc_legendre(2, 0, x) | math | mfrac | 1 | 2(3xsu | p=2 - 1) |
| - style="height:45px;" |
| co | 1=assoc_legendre(2, 1, x) | nbsp | 4math | 3x(1 - xsu | p=2)su | p=1/2nbsp | 4 |
| - style="height:45px;" |
| co | 1=assoc_legendre(2, 2, x) | math | 3(1 - xsu | p=2) |


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

double P20(double x)
{
    return 0.5 * (3 * x * x - 1);
}

double P21(double x)
{
    return 3.0 * x * std::sqrt(1 - x * x);
}

double P22(double x)
{
    return 3 * (1 - x * x);
}

int main()
{
    // spot-checks
    std::cout << std::assoc_legendre(2, 0, 0.5) << '=' << P20(0.5) << '\n'
              << std::assoc_legendre(2, 1, 0.5) << '=' << P21(0.5) << '\n'
              << std::assoc_legendre(2, 2, 0.5) << '=' << P22(0.5) << '\n';
}
```


**Output:**
```
-0.125=-0.125
1.29904=1.29904
2.25=2.25
```


## See also


| cpp/numeric/special functions/dsc legendre | (see dedicated page) |


## External links

