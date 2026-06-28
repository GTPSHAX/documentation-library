---
title: std::acosh(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/acosh
---


# acoshsmall|(std::complex)

ddcl|header=complex|since=c++11|1=
template< class T >
complex<T> acosh( const complex<T>& z );
Computes complex arc hyperbolic cosine of a complex value `z` with branch cut at values less than 1 along the real axis.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, the complex arc hyperbolic cosine of `z` is returned, in the range of a half-strip of nonnegative values along the real axis and in the interval $[−iπ; +iπ]$ along the imaginary axis.

## Error handling and special values

Errors are reported consistent with `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic,
* `std::acosh(std::conj(z)) .
* If `z` is `(±0,+0)`, the result is `(+0,π/2)`.
* If `z` is `(x,+∞)` (for any finite x), the result is `(+∞,π/2)`.
* If `z` is `(x,NaN)` (for any finite x), the result is `(NaN,NaN)` and `FE_INVALID` may be raised.
* If `z` is `(-∞,y)` (for any positive finite y), the result is `(+∞,π)`.
* If `z` is `(+∞,y)` (for any positive finite y), the result is `(+∞,+0)`.
* If `z` is `(-∞,+∞)`, the result is `(+∞,3π/4)`.
* If `z` is `(±∞,NaN)`, the result is `(+∞,NaN)`.
* If `z` is `(NaN,y)` (for any finite y), the result is `(NaN,NaN)` and `FE_INVALID` may be raised.
* If `z` is `(NaN,+∞)`, the result is `(+∞,NaN)`.
* If `z` is `(NaN,NaN)`, the result is `(NaN,NaN)`.

## Notes

Although the C++ standard names this function "complex arc hyperbolic cosine", the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is "complex inverse hyperbolic cosine", and, less common, "complex area hyperbolic cosine".
Inverse hyperbolic cosine is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segment $(-∞,+1)$ of the real axis.
The mathematical definition of the principal value of the inverse hyperbolic cosine is $acosh z .
For any `z`, $acosh(z) , or simply $i acos(z)$ in the upper half of the complex plane.

## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z1(0.5, 0);
    std::cout << "acosh" << z1 << " = " << std::acosh(z1) << '\n';

    std::complex<double> z2(0.5, -0.0);
    std::cout << "acosh" << z2 << " (the other side of the cut) = "
              << std::acosh(z2) << '\n';

    // in upper half-plane, acosh = i acos 
    std::complex<double> z3(1, 1), i(0, 1);
    std::cout << "acosh" << z3 << " = " << std::acosh(z3) << '\n'
              << "i*acos" << z3 << " = " << i*std::acos(z3) << '\n';
}
```


**Output:**
```
acosh(0.500000,0.000000) = (0.000000,-1.047198)
acosh(0.500000,-0.000000) (the other side of the cut) = (0.000000,1.047198)
acosh(1.000000,1.000000) = (1.061275,0.904557)
i*acos(1.000000,1.000000) = (1.061275,0.904557)
```


## See also


| cpp/numeric/complex/dsc acos | (see dedicated page) |
| cpp/numeric/complex/dsc asinh | (see dedicated page) |
| cpp/numeric/complex/dsc atanh | (see dedicated page) |
| cpp/numeric/complex/dsc cosh | (see dedicated page) |
| cpp/numeric/math/dsc acosh | (see dedicated page) |

