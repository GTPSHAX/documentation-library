---
title: std::sin(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/sin
---


# sinsmall|(std::complex)

ddcl|header=complex|1=
template< class T >
complex<T> sin( const complex<T>& z );
Computes complex sine of a complex value `z`.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, the complex sine of `z` is returned.
Errors and special cases are handled as if the operation is implemented by , where `i` is the imaginary unit.

## Notes

The sine is an entire function on the complex plane, and has no branch cuts.
Mathematical definition of the sine is $sin z .

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z(1.0, 0.0); // behaves like real sine along the real line
    std::cout << "sin" << z << " = " << std::sin(z)
              << " ( sin(1) = " << std::sin(1) << ")\n";

    std::complex<double> z2(0.0, 1.0); // behaves like sinh along the imaginary line
    std::cout << "sin" << z2 << " = " << std::sin(z2)
              << " (sinh(1) = " << std::sinh(1) << ")\n";
}
```


**Output:**
```
sin(1.000000,0.000000) = (0.841471,0.000000) ( sin(1) = 0.841471)
sin(0.000000,1.000000) = (0.000000,1.175201) (sinh(1) = 1.175201)
```


## See also


| cpp/numeric/complex/dsc cos | (see dedicated page) |
| cpp/numeric/complex/dsc tan | (see dedicated page) |
| cpp/numeric/complex/dsc asin | (see dedicated page) |
| cpp/numeric/math/dsc sin | (see dedicated page) |
| cpp/numeric/valarray/dsc sin | (see dedicated page) |

