---
title: std::acos(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/acos
---


# acossmall|(std::complex)

ddcl|header=complex|since=c++11|1=
template< class T >
complex<T> acos( const complex<T>& z );
Computes complex arc cosine of a complex value `z`. Branch cuts exist outside the interval $[−1, +1]$ along the real axis.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, complex arc cosine of `z` is returned, in the range of a strip unbounded along the imaginary axis and in the interval $[0, +π]$ along the real axis.

## Error handling and special values

Errors are reported consistent with `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic,
* `std::acos(std::conj(z))
* If `z` is `(±0,+0)`, the result is `(π/2,-0)`
* If `z` is `(±0,NaN)`, the result is `(π/2,NaN)`
* If `z` is `(x,+∞)` (for any finite x), the result is `(π/2,-∞)`
* If `z` is `(x,NaN)` (for any nonzero finite x), the result is `(NaN,NaN)` and `FE_INVALID` may be raised.
* If `z` is `(-∞,y)` (for any positive finite y), the result is `(π,-∞)`
* If `z` is `(+∞,y)` (for any positive finite y), the result is `(+0,-∞)`
* If `z` is `(-∞,+∞)`, the result is `(3π/4,-∞)`
* If `z` is `(+∞,+∞)`, the result is `(π/4,-∞)`
* If `z` is `(±∞,NaN)`, the result is `(NaN,±∞)` (the sign of the imaginary part is unspecified)
* If `z` is `(NaN,y)` (for any finite y), the result is `(NaN,NaN)` and `FE_INVALID` may be raised
* If `z` is `(NaN,+∞)`, the result is `(NaN,-∞)`
* If `z` is `(NaN,NaN)`, the result is `(NaN,NaN)`

## Notes

Inverse cosine (or arc cosine) is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments $(-∞,-1)$ and $(1,∞)$ of the real axis.
The mathematical definition of the principal value of arc cosine is $acos z .
For any `z`, $acos(z) .

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
    std::cout << "acos" << z1 << " = " << std::acos(z1) << '\n';

    std::complex<double> z2(-2.0, -0.0);
    std::cout << "acos" << z2 << " (the other side of the cut) = "
              << std::acos(z2) << '\n';

    // for any z, acos(z) = pi - acos(-z)
    const double pi = std::acos(-1);
    std::complex<double> z3 = pi - std::acos(z2);
    std::cout << "cos(pi - acos" << z2 << ") = " << std::cos(z3) << '\n';
}
```


**Output:**
```
acos(-2.000000,0.000000) = (3.141593,-1.316958)
acos(-2.000000,-0.000000) (the other side of the cut) = (3.141593,1.316958)
cos(pi - acos(-2.000000,-0.000000)) = (2.000000,0.000000)
```


## See also


| cpp/numeric/complex/dsc asin | (see dedicated page) |
| cpp/numeric/complex/dsc atan | (see dedicated page) |
| cpp/numeric/complex/dsc cos | (see dedicated page) |
| cpp/numeric/math/dsc acos | (see dedicated page) |
| cpp/numeric/valarray/dsc acos | (see dedicated page) |

