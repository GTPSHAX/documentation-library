---
title: std::real(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/real2
---


# realsmall|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl rev multi|num=1|dcl1=
template< class T >
T real( const std::complex<T>& z );
|since2=c++14|dcl2=
template< class T >
constexpr T real( const std::complex<T>& z );
**Header:** `<`complex`>`
dcl rev multi|num=A|dcl1=
float       real( float f );
double      real( double f );
long double real( long double f );
|since2=c++14|dcl2=
constexpr float       real( float f );
constexpr double      real( double f );
constexpr long double real( long double f );
|since3=c++23|dcl3=
template< class FloatingPoint >
constexpr FloatingPoint real( FloatingPoint f );
dcl rev multi|num=B|dcl1=
template< class Integer >
double real( Integer i );
|since2=c++14|dcl2=
template< class Integer >
constexpr double real( Integer i );
```

1. Returns the real part of the complex number `z`, i.e. `z.real()`.
rrev|since=c++11|
@A,B@ Additional overloads are provided for all integer and floating-point types, which are treated as complex numbers with zero imaginary part.

## Parameters


### Parameters

- `z` - complex value
- `f` - floating-point value
- `i` - integer value

## Return value

1. The real part of `z`.
@A@ `f`.
@B@ `static_cast<double>(i)`.

## Notes


## See also


| cpp/numeric/complex/dsc real | (see dedicated page) |
| cpp/numeric/complex/dsc imag2 | (see dedicated page) |

