---
title: std::atan(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/atan
---


# atansmall|(std::complex)

ddcl|header=complex|since=c++11|1=
template< class T >
complex<T> atan( const complex<T>& z );
Computes complex arc tangent of a complex value `z`. Branch cut exists outside the interval $[−i, +i]$ along the imaginary axis.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, complex arc tangent of `z` is returned, in the range of a strip unbounded along the imaginary axis and in the interval $[−π/2, +π/2]$ along the real axis.
Errors and special cases are handled as if the operation is implemented by , where `i` is the imaginary unit.

## Notes

Inverse tangent (or arc tangent) is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments $(-∞i,-i)$ and $(+i,+∞i)$ of the imaginary axis.
The mathematical definition of the principal value of inverse tangent is $atan z .

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z1(0.0, 2.0);
    std::cout << "atan" << z1 << " = " << std::atan(z1) << '\n';

    std::complex<double> z2(-0.0, 2.0);
    std::cout << "atan" << z2 << " (the other side of the cut) = "
              << std::atan(z2) << '\n';

    std::complex<double> z3(0.0, INFINITY);
    std::cout << "2 * atan" << z3 << " = " << 2.0 * std::atan(z3) << '\n';
}
```


**Output:**
```
atan(0.000000,2.000000) = (1.570796,0.549306)
atan(-0.000000,2.000000) (the other side of the cut) = (-1.570796,0.549306)
2 * atan(0.000000,inf) = (3.141593,0.000000)
```


## See also


| cpp/numeric/complex/dsc asin | (see dedicated page) |
| cpp/numeric/complex/dsc acos | (see dedicated page) |
| cpp/numeric/complex/dsc tan | (see dedicated page) |
| cpp/numeric/math/dsc atan | (see dedicated page) |
| cpp/numeric/valarray/dsc atan | (see dedicated page) |

