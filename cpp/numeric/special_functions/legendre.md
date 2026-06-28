---
title: std::legendre
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/legendre
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       legendre ( unsigned int n, float x );
double      legendre ( unsigned int n, double x );
long double legendre ( unsigned int n, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ legendre( unsigned int n,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       legendref( unsigned int n, float x );
dcl|num=3|since=c++17|
long double legendrel( unsigned int n, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      legendre ( unsigned int n, Integer x );
```

@1-3@ Computes the unassociated [Legendre polynomials](https://en.wikipedia.org/wiki/Legendre polynomials) of the degree `n` and argument `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::legendre` for all cv-unqualified floating-point types as the type of the parameter `x`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `n` - the degree of the polynomial
- `x` - the argument, a floating-point or integer value

## Return value

If no errors occur, value of the order-`n` unassociated Legendre polynomial of `x`, that is mathjax-or|1=\(\mathsf{P}_n(x) = \frac{1}{2^n n!} \frac{\mathsf{d}^n}{\mathsf{d}x^n} (x^2-1)^n \)|2=(x-1), is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported
* The function is not required to be defined for $
* If `n` is greater or equal than 128, the behavior is implementation-defined

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_poly/legendre.html available in boost.math].
The first few Legendre polynomials are:


| - |
| Function |
| Polynomial |
| - style="height:45px;" |
| nbsp | 4co | legendre(0, x)nbsp | 4 | math | 1 |
| - style="height:45px;" |
| co | legendre(1, x) | math | x |
| - style="height:45px;" |
| co | legendre(2, x) | math | mfrac | 1 | 2(3xsu | p=2 - 1) |
| - style="height:45px;" |
| co | legendre(3, x) | math | mfrac | 1 | 2(5xsu | p=3 - 3x) |
| - style="height:45px;" |
| co | legendre(4, x) | nbsp | 4math | mfrac | 1 | 8(35xsu | p=4 - 30xsu | p=2 + 3)nbsp | 4 |


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

double P3(double x)
{
    return 0.5 * (5 * std::pow(x, 3) - 3 * x);
}

double P4(double x)
{
    return 0.125 * (35 * std::pow(x, 4) - 30 * x * x + 3);
}

int main()
{
    // spot-checks
    std::cout << std::legendre(3, 0.25) << '=' << P3(0.25) << '\n'
              << std::legendre(4, 0.25) << '=' << P4(0.25) << '\n';
}
```


**Output:**
```
-0.335938=-0.335938
0.157715=0.157715
```


## See also


| cpp/numeric/special_functions/dsc laguerre | (see dedicated page) |
| cpp/numeric/special_functions/dsc hermite | (see dedicated page) |


## External links

