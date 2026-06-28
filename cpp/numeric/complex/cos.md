---
title: std::cos(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/cos
---


# cossmall|(std::complex)

ddcl|header=complex|1=
template< class T >
complex<T> cos( const complex<T>& z );
Computes complex cosine of a complex value `z`.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, the complex cosine of `z` is returned.
Errors and special cases are handled as if the operation is implemented by `std::cosh(i * z)`, where `i` is the imaginary unit.

## Notes

The cosine is an entire function on the complex plane, and has no branch cuts.
Mathematical definition of the cosine is $cos z .

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z(1.0, 0.0); // behaves like real cosine along the real line
    std::cout << "cos" << z << " = " << std::cos(z)
              << " ( cos(1) = " << std::cos(1) << ")\n";

    std::complex<double> z2(0.0, 1.0); // behaves like real cosh along the imaginary line
    std::cout << "cos" << z2 << " = " << std::cos(z2)
              << " (cosh(1) = " << std::cosh(1) << ")\n";
}
```


**Output:**
```
cos(1.000000,0.000000) = (0.540302,-0.000000) ( cos(1) = 0.540302)
cos(0.000000,1.000000) = (1.543081,-0.000000) (cosh(1) = 1.543081)
```


## See also


| cpp/numeric/complex/dsc sin | (see dedicated page) |
| cpp/numeric/complex/dsc tan | (see dedicated page) |
| cpp/numeric/complex/dsc acos | (see dedicated page) |
| cpp/numeric/math/dsc cos | (see dedicated page) |
| cpp/numeric/valarray/dsc cos | (see dedicated page) |

