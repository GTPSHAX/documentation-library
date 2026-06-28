---
title: std::lerp
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/lerp
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++20|dcl1=
constexpr float       lerp( float a, float b, float t ) noexcept;
constexpr double      lerp( double a, double b, double t ) noexcept;
constexpr long double lerp( long double a, long double b,
long double t ) noexcept;
|since2=c++23|dcl2=
constexpr /* floating-point-type */
lerp( /* floating-point-type */ a,
/* floating-point-type */ b,
/* floating-point-type */ t ) noexcept;
**Header:** `<`cmath`>`
dcl|num=A|since=c++20|
template< class Arithmetic1, class Arithmetic2, class Arithmetic3 >
constexpr /* common-floating-point-type */
lerp( Arithmetic1 a, Arithmetic2 b, Arithmetic3 t ) noexcept;
```

1. Computes the [Linear interpolation|linear interpolation](https://en.wikipedia.org/wiki/Linear interpolation|linear interpolation) between `a` and `b`, if the parameter `t` is inside [0, 1) (the [Extrapolation#Linear|linear extrapolation](https://en.wikipedia.org/wiki/Extrapolation#Linear|linear extrapolation) otherwise), i.e. the result of  with accounting for floating-point calculation imprecision.<sup>(since C++23)</sup>  The library provides overloads for all cv-unqualified floating-point types as the type of the parameters `a`, `b` and `t`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `a, b, t` - floating-point or integer values

## Return value

When `std::isfinite(a) && std::isfinite(b)` is `true`, the following properties are guaranteed:
* If `1=t == 0`, the result is equal to `a`.
* If `1=t == 1`, the result is equal to `b`.
* If `1=t >= 0 && t <= 1`, the result is finite.
* If `1=std::isfinite(t) && a == b`, the result is equal to `a`.
* If `1=std::isfinite(t) , the result is not `cpp/numeric/math/NAN|NaN`.
Let `CMP(x, y)` be `1` if `x > y`, `-1` if `x < y`, and `0` otherwise. For any `t1` and `t2`, the product of
* `CMP(std::lerp(a, b, t2), std::lerp(a, b, t1))`,
* `CMP(t2, t1)`, and
* `CMP(b, a)`
is non-negative. (That is, `std::lerp` is monotonic.)

## Notes


## Example


### Example

```cpp
#include <cassert>
#include <cmath>
#include <iostream>

float naive_lerp(float a, float b, float t)
{
    return a + t * (b - a);
}

int main()
{
    std::cout << std::boolalpha;

    const float a = 1e8f, b = 1.0f;
    const float midpoint = std::lerp(a, b, 0.5f);

    std::cout << "a = " << a << ", " << "b = " << b << '\n'
              << "midpoint = " << midpoint << '\n';

    std::cout << "std::lerp is exact: "
              << (a == std::lerp(a, b, 0.0f)) << ' '
              << (b == std::lerp(a, b, 1.0f)) << '\n';

    std::cout << "naive_lerp is exact: "
              << (a == naive_lerp(a, b, 0.0f)) << ' '
              << (b == naive_lerp(a, b, 1.0f)) << '\n';

    std::cout << "std::lerp(a, b, 1.0f) = " << std::lerp(a, b, 1.0f) << '\n'
              << "naive_lerp(a, b, 1.0f) = " << naive_lerp(a, b, 1.0f) << '\n';

    assert(not std::isnan(std::lerp(a, b, INFINITY))); // lerp here can be -inf

    std::cout << "Extrapolation demo, given std::lerp(5, 10, t):\n";
    for (auto t{-2.0}; t <= 2.0; t += 0.5)
        std::cout << std::lerp(5.0, 10.0, t) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
a = 1e+08, b = 1
midpoint = 5e+07
std::lerp is exact?: true true
naive_lerp is exact?: true false
std::lerp(a, b, 1.0f) = 1
naive_lerp(a, b, 1.0f) = 0
Extrapolation demo, given std::lerp(5, 10, t):
-5 -2.5 0 2.5 5 7.5 10 12.5 15
```


## See also


| cpp/numeric/dsc midpoint | (see dedicated page) |

