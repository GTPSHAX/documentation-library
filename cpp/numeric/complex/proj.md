---
title: std::proj(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/proj
---


# projsmall|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl|num=1|since=c++11|1=
template< class T >
std::complex<T> proj( const std::complex<T>& z );
**Header:** `<`complex`>`
dcl rev multi|num=A|dcl1=
std::complex<float>       proj( float f );
std::complex<double>      proj( double f );
std::complex<long double> proj( long double f );
|since2=c++23|dcl2=
template< class FloatingPoint >
std::complex<FloatingPoint> proj( FloatingPoint f );
dcl|num=B|1=
template< class Integer >
std::complex<double> proj( Integer i );
```

1. Returns the projection of the complex number `z` onto the [Riemann sphere](https://en.wikipedia.org/wiki/Riemann sphere).
@@ For most `z`, `1=std::proj(z) == z`, but all complex infinities, even the numbers where one component is infinite and the other is NaN, become positive real infinity, `(INFINITY, 0.0)` or `(INFINITY, -0.0)`. The sign of the imaginary (zero) component is the sign of `std::imag(z)`.
@A,B@ Additional overloads are provided for all integer and floating-point types, which are treated as complex numbers with positive zero imaginary component.

## Parameters


### Parameters

- `z` - complex value
- `f` - floating-point value
- `i` - integer value

## Return value

1. The projection of `z` onto the Riemann sphere.
@A@ The projection of `std::complex(f)` onto the Riemann sphere.
@B@ The projection of `std::complex<double>(i)` onto the Riemann sphere.

## Notes

The `proj` function helps model the Riemann sphere by mapping all infinities to one (give or take the sign of the imaginary zero), and should be used just before any operation, especially comparisons, that might give spurious results for any of the other infinities.

## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> c1(1, 2);
    std::cout << "proj" << c1 << " = " << std::proj(c1) << '\n';

    std::complex<double> c2(INFINITY, -1);
    std::cout << "proj" << c2 << " = " << std::proj(c2) << '\n';

    std::complex<double> c3(0, -INFINITY);
    std::cout << "proj" << c3 << " = " << std::proj(c3) << '\n';
}
```


**Output:**
```
proj(1,2) = (1,2)
proj(inf,-1) = (inf,-0)
proj(0,-inf) = (inf,-0)
```


## See also


| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/complex/dsc norm | (see dedicated page) |
| cpp/numeric/complex/dsc polar | (see dedicated page) |

