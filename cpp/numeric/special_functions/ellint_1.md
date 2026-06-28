---
title: std::ellint_1
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/ellint_1
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       ellint_1 ( float k, float phi );
double      ellint_1 ( double k, double phi );
long double ellint_1 ( long double k, long double phi );
|since2=c++23|dcl2=
/* floating-point-type */ ellint_1( /* floating-point-type */ k,
/* floating-point-type */ phi );
dcl|num=2|since=c++17|
float       ellint_1f( float k, float phi );
dcl|num=3|since=c++17|
long double ellint_1l( long double k, long double phi );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */
ellint_1( Arithmetic1 k, Arithmetic2 phi );
```

@1-3@ Computes the [Elliptic integral#Elliptic integral of the first kind|incomplete elliptic integral of the first kind](https://en.wikipedia.org/wiki/Elliptic integral#Elliptic integral of the first kind|incomplete elliptic integral of the first kind) of `k` and `phi`.<sup>(since C++23)</sup>  The library provides overloads of `std::ellint_1` for all cv-unqualified floating-point types as the type of the parameters `k` and `phi`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `k` - elliptic modulus or eccentricity (a floating-point or integer value)
- `phi` - Jacobi amplitude (a floating-point or integer value, measured in radians)

## Return value

If no errors occur, value of the incomplete elliptic integral of the first kind of `k` and `phi`, that is $, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`:
* If the argument is NaN, NaN is returned and domain error is not reported.
* If $, a domain error may occur.

## Notes

An implementation of this function is also available in [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/ellint/ellint_1.html boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <numbers>

int main()
{
    const double hpi = std::numbers::pi / 2.0;

    std::cout << "F(0,π/2)  = " << std::ellint_1(0, hpi) << '\n'
              << "F(0,-π/2) = " << std::ellint_1(0, -hpi) << '\n'
              << "π/2       = " << hpi << '\n'
              << "F(0.7,0)  = " << std::ellint_1(0.7, 0) << '\n';
}
```


**Output:**
```
F(0,π/2)  = 1.5708
F(0,-π/2) = -1.5708
π/2       = 1.5708
F(0.7,0)  = 0
```


## See also


| cpp/numeric/special_functions/dsc comp_ellint_1 | (see dedicated page) |


## External links

