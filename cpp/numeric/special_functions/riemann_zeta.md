---
title: std::riemann_zeta
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/riemann_zeta
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       riemann_zeta ( float num );
double      riemann_zeta ( double num );
long double riemann_zeta ( long double num );
|since2=c++23|dcl2=
/* floating-point-type */ riemann_zeta( /* floating-point-type */ num );
dcl|num=2|since=c++17|
float       riemann_zetaf( float num );
dcl|num=3|since=c++17|
long double riemann_zetal( long double num );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      riemann_zeta ( Integer num );
```

@1-3@ Computes the [Riemann zeta function](https://en.wikipedia.org/wiki/Riemann zeta function) of `num`.<sup>(since C++23)</sup>  The library provides overloads of `std::riemann_zeta` for all cv-unqualified floating-point types as the type of the parameter `num`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or value

## Return value

If no errors occur, value of the Riemann zeta function of `num`, $ζ(num)$, defined for the entire real axis:
* For $num>1$, $Σ
* For $0≤num≤1$, $
* For $num<0$, $2

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/zetas/zeta.html available in boost.math].

## Example


### Example

```cpp
#include <cmath>
#include <format>
#include <iostream>
#include <numbers>

int main()
{
    constexpr auto π = std::numbers::pi;

    // spot checks for well-known values
    for (const double x : {-1.0, 0.0, 1.0, 0.5, 2.0})
        std::cout << std::format("ζ({})\t= {:+.5f}\n", x, std::riemann_zeta(x));
    std::cout << std::format("π²/6\t= {:+.5f}\n", π * π / 6);
}
```


**Output:**
```
ζ(-1)   = -0.08333
ζ(0)    = -0.50000
ζ(1)    = +inf
ζ(0.5)  = -1.46035
ζ(2)    = +1.64493
π²/6    = +1.64493
```


## External links

