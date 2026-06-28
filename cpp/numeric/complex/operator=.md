---
title: std::complex::operator=
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/operator=
---


```cpp
dcl rev multi|num=1|until1=c++20|dcl1=
complex& operator=( const complex& cx );
|since2=c++20|dcl2=
constexpr complex& operator=( const complex& cx );
dcl rev multi|num=2|until1=c++20|dcl1=
template< class X >
complex& operator=( const std::complex<X>& cx );
|since2=c++20|dcl2=
template< class X >
constexpr complex& operator=( const std::complex<X>& cx );
dcl rev multi|num=3|until1=c++20|dcl1=
complex& operator=( const T& x );
|since2=c++20|dcl2=
constexpr complex& operator=( const T& x );
dcl rev multi|num=3|until1=c++20|dcl1=
complex& operator=( F x );
|since2=c++20|until2=c++23|dcl2=
constexpr complex& operator=( F x );
```

Assigns new values to the contents.
@1,2@ Assigns `real()|cx.real()` and `imag()|cx.imag()` to the real and the imaginary parts of the complex number respectively. <sup>(since C++23)</sup> The copy assignment operator
3. Assigns `x` to the real part of the complex number. Imaginary part is set to zero.

## Parameters


### Parameters

- `x` - value to assign
- `cx` - complex value to assign

## Return value

`*this`

## Notes

The copy assignment operator is required to be trivial since C++23, but implementations generally make it trivial in all modes.

## Defect reports


## See also


| cpp/numeric/complex/dsc complex | (see dedicated page) |
| cpp/numeric/dsc operator""i | (see dedicated page) |

