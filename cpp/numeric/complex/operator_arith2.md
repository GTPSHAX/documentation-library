---
title: std::complex::operators (unary)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/operator_arith2
---


```cpp
dcl rev multi | num=1|until1=c++20|dcl1=
template< class T >
std::complex<T> operator+( const std::complex<T>& val );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator+( const std::complex<T>& val );
dcl rev multi| num=2 |unti11=c++20|dcl1=
template< class T >
std::complex<T> operator-( const std::complex<T>& val );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator-( const std::complex<T>& val );
```

Implements the analogs of the unary arithmetic operators for complex numbers.
1. Returns the value of its argument
2. Negates the argument

## Parameters


### Parameters


## Return value

1. a copy of the argument, `std::complex<T>(val)`
2. negated argument, `std::complex<T>(-val.real(), -val.imag())`

## See also

