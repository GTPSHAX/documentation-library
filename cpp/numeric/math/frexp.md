---
title: std::frexp
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/frexp
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|dcl1=
float       frexp ( float num, int* exp );
double      frexp ( double num, int* exp );
long double frexp ( long double num, int* exp );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
frexp ( /* floating-point-type */ num, int* exp );
|
float       frexpf( float num, int* exp );
|
long double frexpl( long double num, int* exp );
**Header:** `<`cmath`>`
|
template< class Integer >
double      frexp ( Integer num, int* exp );
```

@1-3@ Decomposes given floating point value `num` into a normalized fraction and an integral exponent of two.<sup>(since C++23)</sup>  The library provides overloads of `std::frexp` for all cv-unqualified floating-point types as the type of the parameter `num`.
rrev|since=c++11|
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or integer value
- `exp` - pointer to integer value to store the exponent to

## Return value

If `num` is zero, returns zero and stores zero in `*exp`.
Otherwise (if `num` is not zero), if no errors occur, returns the value `x` in the range `(-1, -0.5], [0.5, 1)` and stores an integer value in `*exp` such that $1=x&times;2.
If the value to be stored in `*exp` is outside the range of `int`, the behavior is unspecified.

## Error handling

This function is not subject to any errors specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If `num` is ±0, it is returned, unmodified, and `0` is stored in `*exp`.
* If `num` is ±∞, it is returned, and an unspecified value is stored in `*exp`.
* If `num` is NaN, NaN is returned, and an unspecified value is stored in `*exp`.
* No floating-point exceptions are raised.
* If `FLT_RADIX` is 2 (or a power of 2), the returned value is exact, the current rounding mode is ignored.

## Notes

On a binary system (where `FLT_RADIX` is `2`), `std::frexp` may be implemented as

```cpp
{
    *exp = (value == 0) ? 0 : (int)(1 + std::logb(value));
    return std::scalbn(value, -(*exp));
}
```

The function `std::frexp`, together with its dual, `std::ldexp`, can be used to manipulate the representation of a floating-point number without direct bit manipulations.

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <limits>

int main()
{
    double f = 123.45;
    std::cout << "Given the number " << f << " or " << std::hexfloat
              << f << std::defaultfloat << " in hex,\n";

    double f3;
    double f2 = std::modf(f, &f3);
    std::cout << "modf() makes " << f3 << " + " << f2 << '\n';

    int i;
    f2 = std::frexp(f, &i);
    std::cout << "frexp() makes " << f2 << " * 2^" << i << '\n';

    i = std::ilogb(f);
    std::cout << "logb()/ilogb() make " << f / std::scalbn(1.0, i)
              << " * " << std::numeric_limits<double>::radix
              << "^" << std::ilogb(f) << '\n';
}
```


**Output:**
```
Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,
modf() makes 123 + 0.45
frexp() makes 0.964453 * 2^7
logb()/ilogb() make 1.92891 * 2^6
```


## See also


| cpp/numeric/math/dsc ldexp | (see dedicated page) |
| cpp/numeric/math/dsc logb | (see dedicated page) |
| cpp/numeric/math/dsc ilogb | (see dedicated page) |
| cpp/numeric/math/dsc modf | (see dedicated page) |

