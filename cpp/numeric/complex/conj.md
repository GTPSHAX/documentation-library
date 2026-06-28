---
title: std::conj(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/conj
---


# conjsmall|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl rev multi|num=1|dcl1=
template< class T >
std::complex<T> conj( const std::complex<T>& z );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> conj( const std::complex<T>& z );
**Header:** `<`complex`>`
dcl rev multi|num=A|dcl1=
std::complex<float>       conj( float f );
std::complex<double>      conj( double f );
std::complex<long double> conj( long double f );
|since2=c++20|dcl2=
constexpr std::complex<float>       conj( float f );
constexpr std::complex<double>      conj( double f );
constexpr std::complex<long double> conj( long double f );
|since3=c++23|dcl3=
template< class FloatingPoint >
constexpr std::complex<FloatingPoint> conj( FloatingPoint f );
dcl rev multi|num=B|dcl1=
template< class Integer >
constexpr std::complex<double> conj( Integer i );
|since2=c++20|dcl2=
template< class Integer >
constexpr std::complex<double> conj( Integer i );
```

1. Computes the [Complex conjugate|complex conjugate](https://en.wikipedia.org/wiki/Complex conjugate|complex conjugate) of `z` by reversing the sign of the imaginary part.
rrev|since=c++11|
@A,B@ Additional overloads are provided for all integer and floating-point types, which are treated as complex numbers with zero imaginary component.

## Parameters


### Parameters

- `z` - complex value
- `f` - floating-point value
- `i` - integer value

## Return value

1. The complex conjugate of `z`.
@A@ `std::complex(f)`.
@B@ `std::complex<double>(i)`.

## Notes


## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z(1.0, 2.0);
    std::cout << "The conjugate of " << z << " is " << std::conj(z) << '\n'
              << "Their product is " << z * std::conj(z) << '\n';
}
```


**Output:**
```
The conjugate of (1,2) is (1,-2)
Their product is (5,0)
```


## See also


| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/complex/dsc norm | (see dedicated page) |
| cpp/numeric/complex/dsc polar | (see dedicated page) |

