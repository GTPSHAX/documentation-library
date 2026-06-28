---
title: std::hermite
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/hermite
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
double      hermite ( unsigned int n, double x );
float       hermite ( unsigned int n, float x );
long double hermite ( unsigned int n, long double x );
|since2=c++23|dcl2=
/* floating-point-type */ hermite( unsigned int n,
/* floating-point-type */ x );
dcl|num=2|since=c++17|
float       hermitef( unsigned int n, float x );
dcl|num=3|since=c++17|
long double hermitel( unsigned int n, long double x );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      hermite ( unsigned int n, Integer x );
```

@1-3@ Computes the (physicist's) [Hermite polynomials](https://en.wikipedia.org/wiki/Hermite polynomials) of the degree `n` and argument `x`.<sup>(since C++23)</sup>  The library provides overloads of `std::hermite` for all cv-unqualified floating-point types as the type of the parameter `x`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `n` - the degree of the polynomial
- `x` - the argument, a floating-point or integer value

## Return value

If no errors occur, value of the order-`n` Hermite polynomial of `x`, that is $(-1), is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If `n` is greater or equal than 128, the behavior is implementation-defined.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_poly/hermite.html available in boost.math].
The Hermite polynomials are the polynomial solutions of the equation
$1=u.
The first few are:


| - |
| Function |
| Polynomial |
| - style="height:45px;" |
| nbsp | 4co | hermite(0, x)nbsp | 4 | math | 1 |
| - style="height:45px;" |
| co | hermite(1, x) | math | 2x |
| - style="height:45px;" |
| co | hermite(2, x) | math | 4xsu | p=2 - 2 |
| - style="height:45px;" |
| co | hermite(3, x) | math | 8xsu | p=3 - 12x |
| - style="height:45px;" |
| co | hermite(4, x) | nbsp | 4math | 16xsu | p=4 - 48xsu | p=2 + 12nbsp | 4 |


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

double H3(double x)
{
    return 8 * std::pow(x, 3) - 12 * x;
}

double H4(double x)
{
    return 16 * std::pow(x, 4) - 48 * x * x + 12;
}

int main()
{
    // spot-checks
    std::cout << std::hermite(3, 10) << '=' << H3(10) << '\n'
              << std::hermite(4, 10) << '=' << H4(10) << '\n';
}
```


**Output:**
```
7880=7880
155212=155212
```


## See also


| cpp/numeric/special_functions/dsc laguerre | (see dedicated page) |
| cpp/numeric/special_functions/dsc legendre | (see dedicated page) |


## External links

