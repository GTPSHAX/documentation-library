---
title: std::norm(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/norm
---


# normsmall|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl rev multi|num=1|dcl1=
template< class T >
T norm( const std::complex<T>& z );
|since2=c++20|dcl2=
template< class T >
constexpr T norm( const std::complex<T>& z );
**Header:** `<`complex`>`
dcl rev multi|num=A|dcl1=
float       norm( float f );
double      norm( double f );
long double norm( long double f );
|since2=c++20|dcl2=
constexpr float       norm( float f );
constexpr double      norm( double f );
constexpr long double norm( long double f );
|since3=c++23|dcl3=
template< class FloatingPoint >
constexpr FloatingPoint norm( FloatingPoint f );
dcl rev multi|num=B|dcl1=
template< class Integer >
double norm( Integer i );
|since2=c++20|dcl2=
template< class Integer >
constexpr double norm( Integer i );
```

1. Returns the squared magnitude of the complex number `z`.
rrev|since=c++11|
@A,B@ Additional overloads are provided for all integer and floating-point types, which are treated as complex numbers with zero imaginary component.

## Parameters


### Parameters

- `z` - complex value
- `f` - floating-point value
- `i` - integer value

## Return value

1. The squared magnitude of `z`.
@A@ The square of `f`.
@B@ The square of `i`.

## Notes

The norm calculated by this function is also known as [Field norm|field norm](https://en.wikipedia.org/wiki/Field norm|field norm) or [https://mathworld.wolfram.com/AbsoluteSquare.html absolute square].
The [Euclidean space#Euclidean norm|Euclidean norm](https://en.wikipedia.org/wiki/Euclidean space#Euclidean norm|Euclidean norm) of a complex number is provided by , which is more costly to compute. In some situations, it may be replaced by `std::norm`, for example, if `abs(z1) > abs(z2)` then `norm(z1) > norm(z2)`.

## Example


### Example

```cpp
#include <cassert>
#include <complex>
#include <iostream>

int main()
{
    constexpr std::complex<double> z {3.0, 4.0};
    static_assert(std::norm(z) == (z.real() * z.real() + z.imag() * z.imag()));
    static_assert(std::norm(z) == (z * std::conj(z)));
           assert(std::norm(z) == (std::abs(z) * std::abs(z)));
    std::cout << "std::norm(" << z << ") = " << std::norm(z) << '\n';
}
```


**Output:**
```
std::norm((3,4)) = 25
```


## See also


| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/complex/dsc conj | (see dedicated page) |
| cpp/numeric/complex/dsc polar | (see dedicated page) |

