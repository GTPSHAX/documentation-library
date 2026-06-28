---
title: std::complex::operators
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/operator_arith
---


```cpp
dcl rev multi | num=1 | until1=c++20 | dcl1=
complex& operator+=( const T& other );
|since2=c++20|dcl2=
constexpr complex& operator+=( const T& other );
dcl rev multi| num=2 | until1=c++20 | dcl1=
complex& operator-=( const T& other );
|since2=c++20|dcl2=
constexpr complex& operator-=( const T& other );
dcl rev multi| num=3 | until1=c++20 | dcl1=
complex& operator*=( const T& other );
|since2=c++20|dcl2=
constexpr complex& operator*=( const T& other );
dcl rev multi| num=4 | until1=c++20 | dcl1=
complex& operator/=( const T& other );
|since2=c++20|dcl2=
constexpr complex& operator/=( const T& other );
dcl rev multi | num=1 | until1=c++20 | dcl1=
complex& operator+=( float other );
|since2=c++20|dcl2=
constexpr complex& operator+=( float other );
dcl rev multi| num=2 | until1=c++20 | dcl1=
complex& operator-=( float other );
|since2=c++20|dcl2=
constexpr complex& operator-=( float other );
dcl rev multi| num=3 | until1=c++20 | dcl1=
complex& operator*=( float other );
|since2=c++20|dcl2=
constexpr complex& operator*=( float other );
dcl rev multi| num=4 | until1=c++20 | dcl1=
complex& operator/=( float other );
|since2=c++20|dcl2=
constexpr complex& operator/=( float other );
dcl rev multi | num=1 | until1=c++20 | dcl1=
complex& operator+=( double other );
|since2=c++20|dcl2=
constexpr complex& operator+=( double other );
dcl rev multi| num=2 | until1=c++20 | dcl1=
complex& operator-=( double other );
|since2=c++20|dcl2=
constexpr complex& operator-=( double other );
dcl rev multi| num=3 | until1=c++20 | dcl1=
complex& operator*=( double other );
|since2=c++20|dcl2=
constexpr complex& operator*=( double other );
dcl rev multi| num=4 | until1=c++20 | dcl1=
complex& operator/=( double other );
|since2=c++20|dcl2=
constexpr complex& operator/=( double other );
dcl rev multi | num=1 | until1=c++20 | dcl1=
complex& operator+=( long double other );
|since2=c++20|dcl2=
constexpr complex& operator+=( long double other );
dcl rev multi| num=2 | until1=c++20 | dcl1=
complex& operator-=( long double other );
|since2=c++20|dcl2=
constexpr complex& operator-=( long double other );
dcl rev multi| num=3 | until1=c++20 | dcl1=
complex& operator*=( long double other );
|since2=c++20|dcl2=
constexpr complex& operator*=( long double other );
dcl rev multi| num=4 | until1=c++20 | dcl1=
complex& operator/=( long double other );
|since2=c++20|dcl2=
constexpr complex& operator/=( long double other );
dcl rev multi| num=5 | until1=c++20 | dcl1=
template<class X>
complex& operator+=( const std::complex<X>& other );
|since2=c++20|dcl2=
template<class X>
constexpr complex& operator+=( const std::complex<X>& other );
dcl rev multi| num=6 | until1=c++20 | dcl1=
template<class X>
complex& operator-=( const std::complex<X>& other );
|since2=c++20|dcl2=
template<class X>
constexpr complex& operator-=( const std::complex<X>& other );
dcl rev multi| num=7 | until1=c++20 | dcl1=
template<class X>
complex& operator*=( const std::complex<X>& other );
|since2=c++20|dcl2=
template<class X>
constexpr complex& operator*=( const std::complex<X>& other );
dcl rev multi| num=8 | until1=c++20 | dcl1=
template<class X>
complex& operator/=( const std::complex<X>& other );
|since2=c++20|dcl2=
template<class X>
constexpr complex& operator/=( const std::complex<X>& other );
```

Implements the compound assignment operators for complex arithmetic and for mixed complex/scalar arithmetic. Scalar arguments are treated as complex numbers with the real part equal to the argument and the imaginary part set to zero.
@1,5@ Adds `other` to `*this`.
@2,6@ Subtracts `other` from `*this`.
@3,7@ Multiplies `*this` by `other`.
@4,8@ Divides `*this` by `other`.

## Parameters


### Parameters


## Return value

`*this`

## See also

