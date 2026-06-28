---
title: std::arg(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/arg
---


# argpetty|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl|num=1|1=
template< class T >
T           arg( const std::complex<T>& z );
**Header:** `<`complex`>`
dcl rev multi|num=A|dcl1=
float       arg( float f );
double      arg( double f );
long double arg( long double f );
|since2=c++23|dcl2=
template< class FloatingPoint >
FloatingPoint
arg( FloatingPoint f );
dcl|num=B|1=
template< class Integer >
double      arg( Integer i );
```

1. Calculates the phase angle (in radians) of the complex number `z`.
rrev|since=c++11|
@A,B@ Additional overloads are provided for all integer and floating-point types, which are treated as complex numbers with zero imaginary component.

## Parameters


### Parameters

- `z` - complex value
- `f` - floating-point value
- `i` - integer value

## Return value

1. `std::atan2(std::imag(z), std::real(z))`. If no errors occur, this is the phase angle of `z` in the interval $[−π; π]$.
@A@ Zero if `f` is positive or +0, $π$ if `f` is negative or -0, NaN otherwise.
@B@ Zero if `i` is non-negative, $π$ if it is negative.

## Notes


## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main() 
{
    std::complex<double> z1(1, 0);
    std::complex<double> z2(0, 0);
    std::complex<double> z3(0, 1);
    std::complex<double> z4(-1, 0);
    std::complex<double> z5(-1, -0.0);
    double f = 1.;
    int i = -1;

    std::cout << "phase angle of " << z1 << " is " << std::arg(z1) << '\n'
              << "phase angle of " << z2 << " is " << std::arg(z2) << '\n'
              << "phase angle of " << z3 << " is " << std::arg(z3) << '\n'
              << "phase angle of " << z4 << " is " << std::arg(z4) << '\n'
              << "phase angle of " << z5 << " is " << std::arg(z5) << " "
                 "(the other side of the cut)\n"
              << "phase angle of " << f << " is " << std::arg(f) << '\n'
              << "phase angle of " << i << " is " << std::arg(i) << '\n';

}
```


**Output:**
```
phase angle of (1,0) is 0
phase angle of (0,0) is 0
phase angle of (0,1) is 1.5708
phase angle of (-1,0) is 3.14159
phase angle of (-1,-0) is -3.14159 (the other side of the cut)
phase angle of 1 is 0
phase angle of -1 is 3.14159
```


## See also


| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/complex/dsc polar | (see dedicated page) |
| cpp/numeric/math/dsc atan2 | (see dedicated page) |
| cpp/numeric/valarray/dsc atan2 | (see dedicated page) |

