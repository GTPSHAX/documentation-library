---
title: std::imag(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/imag2
---


# imagsmall|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl rev multi|num=1|dcl1=
template< class T >
T imag( const std::complex<T>& z );
|since2=c++14|dcl2=
template< class T >
constexpr T imag( const std::complex<T>& z );
**Header:** `<`complex`>`
dcl rev multi|num=A|dcl1=
float       imag( float f );
double      imag( double f );
long double imag( long double f );
|since2=c++14|dcl2=
constexpr float       imag( float f );
constexpr double      imag( double f );
constexpr long double imag( long double f );
|since3=c++23|dcl3=
template< class FloatingPoint >
FloatingPoint imag( FloatingPoint f );
dcl rev multi|num=B|dcl1=
template< class Integer >
double imag( Integer i );
|since2=c++14|dcl2=
template< class Integer >
constexpr double imag( Integer i );
```

1. Returns the imaginary part of the complex number `z`, i.e. `z.imag()`.
rrev|since=c++11|
@A,B@ Additional overloads are provided for all integer and floating-point types, which are treated as complex numbers with zero imaginary part.

## Parameters


### Parameters

- `z` - complex value
- `f` - floating-point value
- `i` - integer value

## Return value

1. The imaginary part of `z`.
@A@ } (zero).
@B@ `0.0`.

## Notes


## See also


| cpp/numeric/complex/dsc imag | (see dedicated page) |
| cpp/numeric/complex/dsc real2 | (see dedicated page) |

