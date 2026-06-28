---
title: std::ellint_3
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/ellint_3
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       ellint_3 ( float k, float nu, float phi );
double      ellint_3 ( double k, double nu, double phi );
long double ellint_3 ( long double k, long double nu, long double phi );
|since2=c++23|dcl2=
/* floating-point-type */ ellint_3( /* floating-point-type */ k,
/* floating-point-type */ nu,
/* floating-point-type */ phi );
dcl|num=2|since=c++17|
float       ellint_3f( float k, float nu, float phi );
dcl|num=3|since=c++17|
long double ellint_3l( long double k, long double nu, long double phi );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2, class Arithmetic3 >
/* common-floating-point-type */
ellint_3( Arithmetic1 k, Arithmetic2 nu, Arithmetic3 phi );
```

@1-3@ Computes the [Elliptic integral#Incomplete elliptic integral of the third kind|incomplete elliptic integral of the third kind](https://en.wikipedia.org/wiki/Elliptic integral#Incomplete elliptic integral of the third kind|incomplete elliptic integral of the third kind) of `k`, `nu`, and `phi`.<sup>(since C++23)</sup>  The library provides overloads of `std::ellint_3` for all cv-unqualified floating-point types as the type of the parameters `k`, `nu` and `phi`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `k` - elliptic modulus or eccentricity (a floating-point or integer value)
- `nu` - elliptic characteristic (a floating-point or integer value)
- `phi` - Jacobi amplitude (a floating-point or integer value, measured in radians)

## Return value

If no errors occur, value of the incomplete elliptic integral of the third kind of `k`, `nu`, and `phi`, that is $, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`:
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $, a domain error may occur.

## Notes

An implementation of this function is also available in [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/ellint/ellint_3.html boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>

int main()
{
    const double hpi = std::numbers::pi / 2;

    std::cout << "Π(0,0,π/2) = " << std::ellint_3(0, 0, hpi) << '\n'
              << "π/2 = " << hpi << '\n';
}
```


**Output:**
```
Π(0,0,π/2) = 1.5708
π/2 = 1.5708
```


## See also


| cpp/numeric/special_functions/dsc comp_ellint_3 | (see dedicated page) |


## External links

