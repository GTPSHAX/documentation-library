---
title: std::tanh(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/tanh
---


# tanhsmall|(std::complex)

ddcl|header=complex|since=c++11|1=
template< class T >
complex<T> tanh( const complex<T>& z );
Computes complex hyperbolic tangent of a complex value `z`.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, complex hyperbolic tangent of `z` is returned.

## Error handling and special values

Errors are reported consistent with `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic,
* `std::tanh(std::conj(z)) .
* `std::tanh(-z) .
* If `z` is `(+0,+0)`, the result is `(+0,+0)`.
* If `z` is `(x,+∞)` (for any finite x), the result is `(NaN,NaN)` and `FE_INVALID` is raised.
* If `z` is `(x,NaN)` (for any finite x), the result is `(NaN,NaN)` and `FE_INVALID` may be raised.
* If `z` is `(+∞,y)` (for any finite positive y), the result is `(1,+0)`.
* If `z` is `(+∞,+∞)`, the result is `(1,±0)` (the sign of the imaginary part is unspecified).
* If `z` is `(+∞,NaN)`, the result is `(1,±0)` (the sign of the imaginary part is unspecified).
* If `z` is `(NaN,+0)`, the result is `(NaN,+0)`.
* If `z` is `(NaN,y)` (for any non-zero y), the result is `(NaN,NaN)` and `FE_INVALID` may be raised.
* If `z` is `(NaN,NaN)`, the result is `(NaN,NaN)`.

## Notes

Mathematical definition of hyperbolic tangent is $1=tanh z = .
Hyperbolic tangent is an analytical function on the complex plane and has no branch cuts. It is periodic with respect to the imaginary component, with period &pi;i, and has poles of the first order along the imaginary line, at coordinates $(0, π(1/2 + n))$. However no common floating-point representation is able to represent $π/2$ exactly, thus there is no value of the argument for which a pole error occurs.

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::cout << std::fixed;
    std::complex<double> z(1.0, 0.0); // behaves like real tanh along the real line
    std::cout << "tanh" << z << " = " << std::tanh(z)
              << " (tanh(1) = " << std::tanh(1) << ")\n";

    std::complex<double> z2(0.0, 1.0); // behaves like tangent along the imaginary line
    std::cout << "tanh" << z2 << " = " << std::tanh(z2)
              << " ( tan(1) = " << std::tan(1) << ")\n";
}
```


**Output:**
```
tanh(1.000000,0.000000) = (0.761594,0.000000) (tanh(1) = 0.761594)
tanh(0.000000,1.000000) = (0.000000,1.557408) ( tan(1) = 1.557408)
```


## See also


| cpp/numeric/complex/dsc sinh | (see dedicated page) |
| cpp/numeric/complex/dsc cosh | (see dedicated page) |
| cpp/numeric/complex/dsc atanh | (see dedicated page) |
| cpp/numeric/math/dsc tanh | (see dedicated page) |
| cpp/numeric/valarray/dsc tanh | (see dedicated page) |

