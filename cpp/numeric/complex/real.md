---
title: std::complex::real
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/real
---


```cpp
dcl rev multi|num=1|until1=c++14|dcl1=
T real() const;
|since2=c++14|dcl2=
constexpr T real() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void real( T value );
|since2=c++20|dcl2=
constexpr void real( T value );
dcl rev multi|num=1|until1=c++11|dcl1=
float real() const;
|since2=c++11|dcl2=
constexpr float real() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void real( float value );
|since2=c++20|dcl2=
constexpr void real( float value );
dcl rev multi|num=1|until1=c++11|dcl1=
double real() const;
|since2=c++11|dcl2=
constexpr double real() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void real( double value );
|since2=c++20|dcl2=
constexpr void real( double value );
dcl rev multi|num=1|until1=c++11|dcl1=
long double real() const;
|since2=c++11|dcl2=
constexpr long double real() const;
dcl rev multi|num=2|until1=c++20|dcl1=
void real( long double value );
|since2=c++20|dcl2=
constexpr void real( long double value );
```

Accesses the real part of the complex number.
1. Returns the real part.
2. Sets the real part to `value`.

## Parameters


### Parameters

- `value` - the value to set the real part to

## Return value

1. The real part of `*this`.
2. (none)

## Notes

In C++11, overload  in `std::complex` specializations used to be specified without `const` qualifier. However, in C++11, a `cpp/language/constexpr` specifier used in a non-static member function implies `const`, and thus the behavior is as if `const` is specified.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-387 | C++98 | the real part could not be set directly | can be set directly via a new tt |


## See also


| cpp/numeric/complex/dsc real2 | (see dedicated page) |
| cpp/numeric/complex/dsc imag | (see dedicated page) |

