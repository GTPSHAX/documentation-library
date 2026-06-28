---
title: std::complex::imag
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/imag
---


```cpp
dcl rev multi|num=1|until1=c++14|dcl1=
T imag() const;
|since2=c++14|dcl2=
constexpr T imag() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void imag( T value );
|since2=c++20|dcl2=
constexpr void imag( T value );
dcl rev multi|num=1|until1=c++11|dcl1=
float imag() const;
|since2=c++11|dcl2=
constexpr float imag() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void imag( float value );
|since2=c++20|dcl2=
constexpr void imag( float value );
dcl rev multi|num=1|until1=c++11|dcl1=
double imag() const;
|since2=c++11|dcl2=
constexpr double imag() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void imag( double value );
|since2=c++20|dcl2=
constexpr void imag( double value );
dcl rev multi|num=1|until1=c++11|dcl1=
long double imag() const;
|since2=c++11|dcl2=
constexpr long double imag() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void imag( long double value );
|since2=c++20|dcl2=
constexpr void imag( long double value );
```

Accesses the imaginary part of the complex number.
1. Returns the imaginary part.
2. Sets the imaginary part to `value`.

## Parameters


### Parameters

- `value` - the value to set the imaginary part to

## Return value

1. The imaginary part of `*this`.
2. (none)

## Notes

In C++11, overload  in `std::complex` specializations used to be specified without `const` qualifier. However, in C++11, a `cpp/language/constexpr` specifier used in a non-static member function implies `const`, and thus the behavior is as if `const` is specified.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-387 | C++98 | the imaginary part could not be set directly | can be set directly via a new tt |


## See also


| cpp/numeric/complex/dsc imag2 | (see dedicated page) |
| cpp/numeric/complex/dsc real | (see dedicated page) |

