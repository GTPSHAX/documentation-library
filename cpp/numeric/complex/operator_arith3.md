---
title: operators
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/operator_arith3
---


# operator+,-,*,/ small|(std::complex)


```cpp
dcl rev multi|num=1|until1=c++20|dcl1=
template< class T >
std::complex<T> operator+( const std::complex<T>& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator+( const std::complex<T>& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=2|until1=c++20|dcl1=
template< class T >
std::complex<T> operator+( const std::complex<T>& lhs,
const T& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator+( const std::complex<T>& lhs,
const T& rhs );
dcl rev multi|num=3|until1=c++20|dcl1=
template< class T >
std::complex<T> operator+( const T& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator+( const T& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=4|until1=c++20|dcl1=
template< class T >
std::complex<T> operator-( const std::complex<T>& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator-( const std::complex<T>& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=5|until1=c++20|dcl1=
template< class T >
std::complex<T> operator-( const std::complex<T>& lhs,
const T& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator-( const std::complex<T>& lhs,
const T& rhs );
dcl rev multi|num=6|until1=c++20|dcl1=
template< class T >
std::complex<T> operator-( const T& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator-( const T& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=7|until1=c++20|dcl1=
template< class T >
std::complex<T> operator*( const std::complex<T>& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator*( const std::complex<T>& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=8|until1=c++20|dcl1=
template< class T >
std::complex<T> operator*( const std::complex<T>& lhs,
const T& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator*( const std::complex<T>& lhs,
const T& rhs );
dcl rev multi|num=9|until1=c++20|dcl1=
template< class T >
std::complex<T> operator*( const T& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator*( const T& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=10|until1=c++20|dcl1=
template< class T >
std::complex<T> operator/( const std::complex<T>& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator/( const std::complex<T>& lhs,
const std::complex<T>& rhs );
dcl rev multi|num=11|until1=c++20|dcl1=
template< class T >
std::complex<T> operator/( const std::complex<T>& lhs,
const T& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator/( const std::complex<T>& lhs,
const T& rhs );
dcl rev multi|num=12|until1=c++20|dcl1=
template< class T >
std::complex<T> operator/( const T& lhs,
const std::complex<T>& rhs );
|since2=c++20|dcl2=
template< class T >
constexpr std::complex<T> operator/( const T& lhs,
const std::complex<T>& rhs );
```

Implements the binary operators for complex arithmetic and for mixed complex/scalar arithmetic. Scalar arguments are treated as complex numbers with the real part equal to the argument and the imaginary part set to zero.
@1-3@ Returns the sum of its arguments.
@4-6@ Returns the result of subtracting `rhs` from `lhs`.
@7-9@ Multiplies its arguments.
@10-12@ Divides `lhs` by `rhs`.

## Parameters


### Parameters

- `lhs, rhs` - the arguments: either both complex numbers or one complex and one scalar of matching type (`float`, `double`, `long double`)

## Return value

@1-3@ `1= std::complex<T>(lhs) += rhs`
@4-6@ `1= std::complex<T>(lhs) -= rhs`
@7-9@ `1= std::complex<T>(lhs) *= rhs`
@10-12@ `1= std::complex<T>(lhs) /= rhs`

## Notes

Because  does not consider implicit conversions, these operators cannot be used for mixed integer/complex arithmetic. In all cases, the scalar must have the same type as the underlying type of the complex number.
The GCC flag "-fcx-limited-range" (included by "-ffast-math") changes the behavior of complex multiply/division by removing checks for floating point edge cases. This impacts loop vectorization.

## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> c2(2.0, 0.0);
    std::complex<double> ci(0.0, 1.0);

    std::cout << ci << " + " << c2 << " = " << ci + c2 << '\n'
              << ci << " * " << ci << " = " << ci * ci << '\n'
              << ci << " + " << c2 << " / " << ci << " = " << ci + c2 / ci << '\n'
              << 1  << " / " << ci << " = " << 1.0 / ci << '\n';

//    std::cout << 1.0f / ci; // compile error
//    std::cout << 1 / ci; // compile error
}
```


**Output:**
```
(0,1) + (2,0) = (2,1)
(0,1) * (0,1) = (-1,0)
(0,1) + (2,0) / (0,1) = (0,-1)
1 / (0,1) = (0,-1)
```


## See also


| cpp/numeric/complex/dsc operator_arith | (see dedicated page) |
| cpp/numeric/complex/dsc operator_arith2 | (see dedicated page) |

