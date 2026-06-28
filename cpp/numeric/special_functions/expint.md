---
title: std::expint
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/expint
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       expint ( float num );
double      expint ( double num );
long double expint ( long double num );
|since2=c++23|dcl2=
/* floating-point-type */ expint( /* floating-point-type */ num );
dcl|num=2|since=c++17|
float       expintf( float num );
dcl|num=3|since=c++17|
long double expintl( long double num );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Integer >
double      expint ( Integer num );
```

@1-3@ Computes the [Exponential integral](https://en.wikipedia.org/wiki/Exponential integral) of `num`.<sup>(since C++23)</sup>  The library provides overloads of `std::expint` for all cv-unqualified floating-point types as the type of the parameter `num`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, value of the exponential integral of `num`, that is $-, is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If the argument is NaN, NaN is returned and domain error is not reported.
* If the argument is ±0, -∞ is returned.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/expint/expint_i.html available in boost.math].

## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

{{cpp/numeric/draw_vbars
```

int main()
{
std::cout << "Ei(0) = " << std::expint(0) << '\n'
<< "Ei(1) = " << std::expint(1) << '\n'
<< "Gompertz constant = " << -std::exp(1) * std::expint(-1) << '\n';
std::vector<float> v;
for (float x{1.f}; x < 8.8f; x += 0.3565f)
v.push_back(std::expint(x));
draw_vbars<9, 1, 1>(v);
}
|output=
Ei(0) = -inf
Ei(1) = 1.89512
Gompertz constant = 0.596347
█ ┬ 666.505
█ │
▆ █ │
█ █ │
█ █ █ │
▆ █ █ █ │
▁ ▆ █ █ █ █ │
▂ ▅ █ █ █ █ █ █ │
▁ ▁ ▁ ▁ ▁ ▁ ▁ ▂ ▂ ▃ ▃ ▄ ▆ ▇ █ █ █ █ █ █ █ █ ┴ 1.89512

## External links

