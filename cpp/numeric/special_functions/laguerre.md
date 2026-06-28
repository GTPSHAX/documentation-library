---
title: std::laguerre
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/laguerre
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       laguerre ( unsigned int n, float x );
double      laguerre ( unsigned int n, double x );
long double laguerre ( unsigned int n, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ laguerre( unsigned int n,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       laguerref( unsigned int n, float x );
dcl|num=3|since=c++17|
long double laguerrel( unsigned int n, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      laguerre ( unsigned int n, Integer x );
```

@1-3@ Computes the non-associated [Laguerre polynomials](https://en.wikipedia.org/wiki/Laguerre polynomials) of the degree `n` and argument `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::laguerre` for all cv-unqualified floating-point types as the type of the parameter `x`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `n` - the degree of the polynomial, an unsigned integer value
- `x` - the argument, a floating-point or integer value

## Return value

If no errors occur, value of the nonassociated Laguerre polynomial of `x`, that is $, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`
* If the argument is NaN, NaN is returned and domain error is not reported
* If `x` is negative, a domain error may occur
* If `n` is greater or equal than 128, the behavior is implementation-defined

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_poly/laguerre.html available in boost.math].
The Laguerre polynomials are the polynomial solutions of the equation $xy.
The first few are:


| - |
| Function |
| Polynomial |
| - style="height:45px;" |
| nbsp | 4co | laguerre(0, x)nbsp | 4 | 1 |
| - style="height:45px;" |
| co | laguerre(1, x) | math | -x + 1 |
| - style="height:45px;" |
| co | laguerre(2, x) | math | mfrac | 1 | 2(xsu | p=2 - 4x + 2) |
| - style="height:45px;" |
| co | laguerre(3, x) | nbsp | 4math | mfrac | 1 | 6(-xsu | p=3 - 9xsu | p=2 - 18x + 6)nbsp | 4 |


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

double L1(double x)
{
    return -x + 1;
}

double L2(double x)
{
    return 0.5 * (x * x - 4 * x + 2);
}

int main()
{
    // spot-checks
    std::cout << std::laguerre(1, 0.5) << '=' << L1(0.5) << '\n'
              << std::laguerre(2, 0.5) << '=' << L2(0.5) << '\n'
              << std::laguerre(3, 0.0) << '=' << 1.0 << '\n';
}
```


**Output:**
```
0.5=0.5
0.125=0.125
1=1
```


## See also


| cpp/numeric/special_functions/dsc assoc_laguerre | (see dedicated page) |


## External links

