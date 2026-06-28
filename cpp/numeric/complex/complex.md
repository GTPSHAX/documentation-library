---
title: std::complex::complex
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/complex
---


```cpp
dcl rev multi|num=1|until1=c++14|dcl1=
complex( const T& re = T(), const T& im = T() );
|dcl2=
constexpr complex( const T& re = T(), const T& im = T() );
dcl rev multi|num=2|until1=c++14|dcl1=
complex( const complex& other );
|until2=c++23|dcl2=
constexpr complex( const complex& other );
|dcl3=
constexpr complex( const complex& other ) = default;
dcl rev multi|num=3|until1=c++14|dcl1=
template< class X >
complex( const complex<X>& other );
|until2=c++23|dcl2=
template< class X >
constexpr complex( const complex<X>& other );
|dcl3=
template< class X >
constexpr explicit(/* see below */) complex( const complex<X>& other );
dcl rev multi|num=1|until1=c++11|dcl1=
complex( float re = 0.0f, float im = 0.0f );
|dcl2=
constexpr complex( float re = 0.0f, float im = 0.0f );
dcl|num=2|since=c++20|1=
constexpr complex( const complex<float>& other ) = default;
dcl rev multi|num=3|until1=c++11|dcl1=
explicit complex( const complex<double>& other );
explicit complex( const complex<long double>& other );
|dcl2=
constexpr explicit complex( const complex<double>& other );
constexpr explicit complex( const complex<long double>& other );
dcl rev multi|num=1|until1=c++11|dcl1=
complex( double re = 0.0, double im = 0.0 );
|dcl2=
constexpr complex( double re = 0.0, double im = 0.0 );
dcl|num=2|since=c++20|1=
constexpr complex( const complex<double>& other ) = default;
dcl rev multi|num=3|until1=c++11|dcl1=
complex( const complex<float>& other );
explicit complex( const complex<long double>& other );
|dcl2=
constexpr complex( const complex<float>& other );
constexpr explicit complex( const complex<long double>& other );
dcl rev multi|num=1|until1=c++11|dcl1=
complex( long double re = 0.0L, long double im = 0.0L );
|dcl2=
constexpr complex( long double re = 0.0L, long double im = 0.0L );
dcl|num=2|since=c++20|1=
constexpr complex( const complex<long double>& other ) = default;
dcl rev multi|num=3|until1=c++11|dcl1=
complex( const complex<float>& other );
complex( const complex<double>& other );
|dcl2=
constexpr complex( const complex<float>& other );
constexpr complex( const complex<double>& other );
```

Constructs the `std::complex` object.<sup>(until C++23)</sup>  The standard explicit specializations (`std::complex<float>`, `std::complex<double>` and `std::complex<long double>`) have different constructor declarations from the main template.
1. Constructs the complex number from real part `re` and imaginary part `im`.
2. Copy constructor. Constructs the object with the copy of the contents of `other`.<sup>(until C++20)</sup> The copy constructors are implicitly declared in the standard explicit specializations.
3. Converting constructor. Constructs the object from a complex number of a different type.
rev|until=c++23|
The main template provides a converting constructor template, while each standard explicit specialization provides two non-template constructors for the two other standard explicit specializations.
The non-template constructors are converting constructors (i.e. non-explicit) if and only if the conversions of the real and imaginary parts are not narrowing.
rev|since=c++23|
For the main template, the expression inside `explicit` evaluates to `false` if and only if the floating-point conversion rank of `T` is greater than or equal to the floating-point conversion rank of `X`.

## Parameters


### Parameters

- `re` - the real part
- `im` - the imaginary part
- `other` - another complex number to use as source

## Notes

Since C++23, the copy constructor is required to be trivial in order to satisfy the *TriviallyCopyable* requirement, but implementations generally make it trivial in all modes.

## See also


| cpp/numeric/complex/dsc operator{{= | (see dedicated page) |
| cpp/numeric/dsc operator""i | (see dedicated page) |

