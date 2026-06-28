---
title: std::asin(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/asin
---

ddcl|header=complex|since=c++11|1=
template< class T >
std::complex<T> asin( const std::complex<T>& z );
Computes complex arc sine of a complex value `z`. Branch cut exists outside the interval $[−1, +1]$ along the real axis.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, complex arc sine of `z` is returned, in the range of a strip unbounded along the imaginary axis and in the interval $[−π/2, +π/2]$ along the real axis.
Errors and special cases are handled as if the operation is implemented by `-i * std::asinh(i * z)`, where `i` is the imaginary unit.

## Notes

Inverse sine (or arc sine) is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments $(-∞,-1)$ and $(1,∞)$ of the real axis.
The mathematical definition of the principal value of arc sine is mathjax-or|1=\(\small \arcsin z = -{\rm i}\ln({\rm i}z+\sqrt{1-z^2})\)|2=arcsin z = -''i''ln(''i''z + ).
For any `z`, mathjax-or|1=\(\small{ \arcsin(z) = \arccos(-z) - \frac{\pi}{2} }\)|2=asin(z) = acos(-z) -  .

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z1(-2.0, 0.0);
    std::cout << "asin" << z1 << " = " << std::asin(z1) << '\n';

    std::complex<double> z2(-2.0, -0.0);
    std::cout << "asin" << z2 << " (the other side of the cut) = "
              << std::asin(z2) << '\n';

    // for any z, asin(z) = acos(−z) − pi / 2
    const double pi = std::acos(-1);
    std::complex<double> z3 = std::acos(z2) - pi / 2;
    std::cout << "sin(acos" << z2 << " - pi / 2) = " << std::sin(z3) << '\n';
}
```


**Output:**
```
asin(-2.000000,0.000000) = (-1.570796,1.316958)
asin(-2.000000,-0.000000) (the other side of the cut) = (-1.570796,-1.316958)
sin(acos(-2.000000,-0.000000) - pi / 2) = (2.000000,0.000000)
```


## See also


| cpp/numeric/complex/dsc acos | (see dedicated page) |
| cpp/numeric/complex/dsc atan | (see dedicated page) |
| cpp/numeric/complex/dsc sin | (see dedicated page) |
| cpp/numeric/math/dsc asin | (see dedicated page) |
| cpp/numeric/valarray/dsc asin | (see dedicated page) |

