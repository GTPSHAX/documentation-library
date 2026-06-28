---
title: std::log10(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/log10
---


# log10petty|(std::complex)

ddcl|header=complex|1=
template< class T >
std::complex<T> log10( const std::complex<T>& z );
Computes complex common (base `10`) logarithm of a complex value `z` with a branch cut along the negative real axis.
The behavior of this function is equivalent to ``std::log`(z) / std::log(T(10))`.

## Parameters


### Parameters

- `z` - complex value

## Return value

Complex common logarithm of `z`.

## Example


### Example

```cpp
#include <cmath>
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z(0.0, 1.0); // r = 0, θ = pi / 2
    std::cout << "2 * log10" << z << " = " << 2.0 * std::log10(z) << '\n';

    std::complex<double> z2(sqrt(2.0) / 2, sqrt(2.0) / 2); // r = 1, θ = pi / 4
    std::cout << "4 * log10" << z2 << " = " << 4.0 * std::log10(z2) << '\n';

    std::complex<double> z3(-100.0, 0.0); // r = 100, θ = pi
    std::cout << "log10" << z3 << " = " << std::log10(z3) << '\n';
    std::complex<double> z4(-100.0, -0.0); // the other side of the cut
    std::cout << "log10" << z4 << " = " << std::log10(z4) << " "
                 "(the other side of the cut)\n"
                 "(note: pi / log(10) = " << std::acos(-1.0) / std::log(10.0) << ")\n";
}
```


**Output:**
```
2 * log10(0,1) = (0,1.36438)
4 * log10(0.707107,0.707107) = (0,1.36438)
log10(-100,0) = (2,1.36438)
log10(-100,-0) = (2,-1.36438) (the other side of the cut)
(note: pi / log(10) = 1.36438)
```


## See also


| cpp/numeric/complex/dsc log | (see dedicated page) |
| cpp/numeric/math/dsc log10 | (see dedicated page) |
| cpp/numeric/valarray/dsc log10 | (see dedicated page) |

