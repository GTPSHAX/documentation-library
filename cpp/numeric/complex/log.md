---
title: std::log(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/log
---


# logpetty|(std::complex)

ddcl|header=complex|1=
template< class T >
std::complex<T> log( const std::complex<T>& z );
Computes complex [Natural logarithm|natural (base ''e'') logarithm](https://en.wikipedia.org/wiki/Natural logarithm|natural (base ''e'') logarithm) of a complex value `z` with a branch cut along the negative real axis.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, the complex natural logarithm of `z` is returned, in the range of a strip in the interval $[−iπ, +iπ]$ along the imaginary axis and mathematically unbounded along the real axis.

## Error handling and special values

Errors are reported consistent with `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic,
* The function is continuous onto the branch cut taking into account the sign of imaginary part
* `std::log(std::conj(z))
* If `z` is `(-0,+0)`, the result is `(-∞,π)` and `FE_DIVBYZERO` is raised
* If `z` is `(+0,+0)`, the result is `(-∞,+0)` and `FE_DIVBYZERO` is raised
* If `z` is `(x,+∞)` (for any finite x), the result is `(+∞,π/2)`
* If `z` is `(x,NaN)` (for any finite x), the result is `(NaN,NaN)` and `FE_INVALID` may be raised
* If `z` is `(-∞,y)` (for any finite positive y), the result is `(+∞,π)`
* If `z` is `(+∞,y)` (for any finite positive y), the result is `(+∞,+0)`
* If `z` is `(-∞,+∞)`, the result is `(+∞,3π/4)`
* If `z` is `(+∞,+∞)`, the result is `(+∞,π/4)`
* If `z` is `(±∞,NaN)`, the result is `(+∞,NaN)`
* If `z` is `(NaN,y)` (for any finite y), the result is `(NaN,NaN)` and `FE_INVALID` may be raised
* If `z` is `(NaN,+∞)`, the result is `(+∞,NaN)`
* If `z` is `(NaN,NaN)`, the result is `(NaN,NaN)`

## Notes

The natural logarithm of a complex number `z` with polar coordinate components $(r,θ)$ equals $ln r + i(θ+2nπ)$, with the principal value $ln r + iθ$.
The semantics of this function are intended to be consistent with the C function `c/numeric/complex/clog`.

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z {0.0, 1.0}; // r = 1, θ = pi / 2
    std::cout << "2 * log" << z << " = " << 2.0 * std::log(z) << '\n';

    std::complex<double> z2 {sqrt(2.0) / 2, sqrt(2.0) / 2}; // r = 1, θ = pi / 4
    std::cout << "4 * log" << z2 << " = " << 4.0 * std::log(z2) << '\n';

    std::complex<double> z3 {-1.0, 0.0}; // r = 1, θ = pi
    std::cout << "log" << z3 << " = " << std::log(z3) << '\n';
    std::complex<double> z4 {-1.0, -0.0}; // the other side of the cut
    std::cout << "log" << z4 << " (the other side of the cut) = " << std::log(z4) << '\n';
}
```


**Output:**
```
2 * log(0,1) = (0,3.14159)
4 * log(0.707107,0.707107) = (0,3.14159)
log(-1,0) = (0,3.14159)
log(-1,-0) (the other side of the cut) = (0,-3.14159)
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2597 | C++98 | specification mishandles signed zero imaginary parts | erroneous requirement removed |


## See also


| cpp/numeric/complex/dsc log10 | (see dedicated page) |
| cpp/numeric/complex/dsc exp | (see dedicated page) |
| cpp/numeric/math/dsc log | (see dedicated page) |
| cpp/numeric/valarray/dsc log | (see dedicated page) |

