---
title: std::sinh(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/sinh
---


# sinhsmall|(std::complex)

ddcl|header=complex|since=c++11|1=
template< class T >
complex<T> sinh( const complex<T>& z );
Computes complex hyperbolic sine of a complex value `z`.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, complex hyperbolic sine of `z` is returned.

## Error handling and special values

Errors are reported consistent with `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic,
* `std::sinh(std::conj(z))
* `std::sinh(z)
* If `z` is `(+0,+0)`, the result is `(+0,+0)`
* If `z` is `(+0,+∞)`, the result is `(±0,NaN)` (the sign of the real part is unspecified) and `FE_INVALID` is raised
* If `z` is `(+0,NaN)`, the result is `(±0,NaN)`
* If `z` is `(x,+∞)` (for any positive finite x), the result is `(NaN,NaN)` and `FE_INVALID` is raised
* If `z` is `(x,NaN)` (for any positive finite x), the result is `(NaN,NaN)` and `FE_INVALID` may be raised
* If `z` is `(+∞,+0)`, the result is `(+∞,+0)`
* If `z` is `(+∞,y)` (for any positive finite y), the result is `+∞cis(y)`
* If `z` is `(+∞,+∞)`, the result is `(±∞,NaN)` (the sign of the real part is  unspecified) and `FE_INVALID` is raised
* If `z` is `(+∞,NaN)`, the result is `(±∞,NaN)` (the sign of the real part is  unspecified)
* If `z` is `(NaN,+0)`, the result is `(NaN,+0)`
* If `z` is `(NaN,y)` (for any finite nonzero y), the result is `(NaN,NaN)` and `FE_INVALID` may be raised
* If `z` is `(NaN,NaN)`, the result is `(NaN,NaN)`
where $cis(y)$ is $cos(y) + i sin(y)$.

## Notes

Mathematical definition of hyperbolic sine is $sinh z .
Hyperbolic sine is an entire function in the complex plane and has no branch cuts. It is periodic with respect to the imaginary component, with period $2&pi;i$.

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z(1.0, 0.0); // behaves like real sinh along the real line
    std::cout << "sinh" << z << " = " << std::sinh(z)
              << " (sinh(1) = " << std::sinh(1) << ")\n";

    std::complex<double> z2(0.0, 1.0); // behaves like sine along the imaginary line
    std::cout << "sinh" << z2 << " = " << std::sinh(z2)
              << " ( sin(1) = " << std::sin(1) << ")\n";
}
```


**Output:**
```
sinh(1.000000,0.000000) = (1.175201,0.000000) (sinh(1) = 1.175201)
sinh(0.000000,1.000000) = (0.000000,0.841471) ( sin(1) = 0.841471)
```


## See also


| cpp/numeric/complex/dsc cosh | (see dedicated page) |
| cpp/numeric/complex/dsc tanh | (see dedicated page) |
| cpp/numeric/complex/dsc asinh | (see dedicated page) |
| cpp/numeric/math/dsc sinh | (see dedicated page) |
| cpp/numeric/valarray/dsc sinh | (see dedicated page) |

