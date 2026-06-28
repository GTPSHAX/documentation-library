---
title: std::assoc_laguerre
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/assoc_laguerre
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       assoc_laguerre ( unsigned int n, unsigned int m, float x );
double      assoc_laguerre ( unsigned int n, unsigned int m, double x );
long double assoc_laguerre ( unsigned int n, unsigned int m, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ assoc_laguerre( unsigned int n, unsigned int m,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       assoc_laguerref( unsigned int n, unsigned int m, float x );
dcl|num=3|since=c++17|
long double assoc_laguerrel( unsigned int n, unsigned int m, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      assoc_laguerre ( unsigned int n, unsigned int m, Integer x );
```

@1-3@ Computes the [Laguerre polynomials#Generalized Laguerre polynomials|associated Laguerre polynomials](https://en.wikipedia.org/wiki/Laguerre polynomials#Generalized Laguerre polynomials|associated Laguerre polynomials) of the degree `n`, order `m`, and argument `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::assoc_laguerre` for all cv-unqualified floating-point types as the type of the parameter `x`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `n` - the degree of the polynomial, an unsigned integer value
- `m` - the order of the polynomial, an unsigned integer value
- `x` - the argument, a floating-point or integer value

## Return value

If no errors occur, value of the associated Laguerre polynomial of `x`, that is mathjax-or|1=\((-1)^m \: \frac{ \mathsf{d} ^ m}{ \mathsf{d}x ^ m} \, \mathsf{L}_{n+m}(x)\)|2=(-1)L(x), is returned (where mathjax-or|1=\(\mathsf{L}_{n+m}(x)\)|2=L(x) is the unassociated Laguerre polynomial, `std::laguerre(n + m, x)`).

## Error handling

Errors may be reported as specified in `math_errhandling`
* If the argument is NaN, NaN is returned and domain error is not reported
* If `x` is negative, a domain error may occur
* If `n` or `m` is greater or equal to 128, the behavior is implementation-defined

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_poly/laguerre.html available in boost.math].
The associated Laguerre polynomials are the polynomial solutions of the equation mathjax-or|1=\(x\ddot{y} + (m+1-x)\dot{y} + ny = 0\)|2=xy+(m+1-x)y+ny = 0.
The first few are:


| - |
| Function |
| Polynomial |
| - style="height:45px;" |
| nbsp | 4co | 1=assoc_laguerre(0, m, x)nbsp | 4 | 1 |
| - style="height:45px;" |
| co | 1=assoc_laguerre(1, m, x) | math | -x + m + 1 |
| - style="height:45px;" |
| co | 1=assoc_laguerre(2, m, x) | math | mfrac | 1 | 2[xsu | p=2 - 2(m + 2)x + (m + 1)(m + 2)] |
| - style="height:45px;" |
| co | 1=assoc_laguerre(3, m, x) | nbsp | 4math | mfrac | 1 | 6[-xsu | p=3 - 3(m + 3)xsu | p=2 - 3(m + 2)(m + 3)x + (m + 1)(m + 2)(m + 3)]nbsp | 4 |


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

double L1(unsigned m, double x)
{
    return -x + m + 1;
}

double L2(unsigned m, double x)
{
    return 0.5 * (x * x - 2 * (m + 2) * x + (m + 1) * (m + 2));
}

int main()
{
    // spot-checks
    std::cout << std::assoc_laguerre(1, 10, 0.5) << '=' << L1(10, 0.5) << '\n'
              << std::assoc_laguerre(2, 10, 0.5) << '=' << L2(10, 0.5) << '\n';
}
```


**Output:**
```
10.5=10.5
60.125=60.125
```


## See also


| cpp/numeric/special_functions/dsc laguerre | (see dedicated page) |


## External links

