---
title: std::atan2(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/atan2
---


# atan2small|(std::valarray)


```cpp
**Header:** `<`valarray`>`
dcl|num=1|
template< class T >
std::valarray<T> atan2( const std::valarray<T>& y, const std::valarray<T>& x );
dcl|num=2|
template< class T >
std::valarray<T> atan2( const std::valarray<T>& y,
const typename std::valarray<T>::value_type& vx );
dcl|num=3|
template< class T >
std::valarray<T> atan2( const typename std::valarray<T>::value_type& vy,
const std::valarray<T>& x );
```

Computes the inverse tangent of `y / x` using the signs of arguments to correctly determine quadrant.
1. Computes the inverse tangent of each pair of corresponding values from `y` and `x`.
The behavior is undefined if `1=x.size() != y.size()`.
2. Computes the inverse tangent of `vx` and each value in the numeric array `y`.
3. Computes the inverse tangent of `vy` and each value in the numeric array `x`.

## Parameters


### Parameters

- `x, y` - numeric arrays to compute inverse tangent of
- `vy, vx` - values to compute inverse tangent of

## Return value

A numeric array containing the results of computation of inverse tangent.

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <valarray>

void show(char const* title, const std::valarray<double>& va)
{
    std::cout << title << ' ';
    std::for_each(std::begin(va), std::end(va), [](const double x)
    { 
        std::cout << ' ' << std::right << std::setw(4) << x << "°";
    });
    std::cout << '\n';
}

const double pi = std::acos(-1.0); // C++20: std::numbers::pi

int main()
{
    auto degrees_to_radians = [](double const& x) { return (pi * x / 180); };
    auto radians_to_degrees = [](double const& x) { return (180 * x / pi); };

    const std::valarray<double> degrees{-90, -60, -45, -30, 0, 30, 45, 60, 90};
    const std::valarray<double> radians = degrees.apply(degrees_to_radians);

    const auto sin = std::sin(radians);
    const auto cos = std::cos(radians);

    show("(1)", std::atan2(sin, cos).apply(radians_to_degrees));
    show("(2)", std::atan2(sin/cos, 1.0).apply(radians_to_degrees));
    show("(3)", std::atan2(1.0, cos/sin).apply(radians_to_degrees));
}
```


**Output:**
```
(1)   -90°  -60°  -45°  -30°    0°   30°   45°   60°   90°
(2)   -90°  -60°  -45°  -30°    0°   30°   45°   60°   90°
(3)    90°  120°  135°  150°    0°   30°   45°   60°   90°
```


## Defect reports


## See also


| cpp/numeric/valarray/dsc asin | (see dedicated page) |
| cpp/numeric/valarray/dsc acos | (see dedicated page) |
| cpp/numeric/valarray/dsc atan | (see dedicated page) |
| cpp/numeric/math/dsc atan2 | (see dedicated page) |
| cpp/numeric/complex/dsc arg | (see dedicated page) |

