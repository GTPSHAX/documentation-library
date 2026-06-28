---
title: std::abs(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/abs
---


# abssmall|(std::complex)

ddcl|header=complex|1=
template< class T >
T abs( const complex<T>& z );
Returns the magnitude of the complex number `z`.

## Parameters


### Parameters

- `z` - complex value

## Return value

If no errors occur, returns the absolute value (also known as norm, modulus, or magnitude) of `z`.
Errors and special cases are handled as if the function is implemented as `std::hypot(std::real(z), std::imag(z))`.

## Example


### Example

```cpp
#include <complex>
#include <iostream>

int main()
{
    std::complex<double> z(1, 1);
    std::cout << z << " cartesian is rho = " << std::abs(z)
              << " theta = " << std::arg(z) << " polar\n";
}
```


**Output:**
```
(1,1) cartesian is rho = 1.41421 theta = 0.785398 polar
```


## See also


| cpp/numeric/complex/dsc arg | (see dedicated page) |
| cpp/numeric/complex/dsc polar | (see dedicated page) |
| cpp/numeric/math/dsc abs | (see dedicated page) |
| cpp/numeric/math/dsc fabs | (see dedicated page) |
| cpp/numeric/math/dsc hypot | (see dedicated page) |
| cpp/numeric/valarray/dsc abs | (see dedicated page) |

