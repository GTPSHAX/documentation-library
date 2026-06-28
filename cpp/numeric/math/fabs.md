---
title: std::abs(float)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fabs
---


# abssmall|(float)

|fabs|fabsf|fabsl

```cpp
**Header:** `<`cmath`>`
**Header:** `<`cstdlib`>`
dcl rev multi|num=1|dcl1=
float       abs( float num );
double      abs( double num );
long double abs( long double num );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
abs( /* floating-point-type */ num );
**Header:** `<`cmath`>`
dcl rev multi|num=2|dcl1=
float       fabs ( float num );
double      fabs ( double num );
long double fabs ( long double num );
|since2=c++23|dcl2=
constexpr /* floating-point-type */
fabs ( /* floating-point-type */ num );
dcla|anchor=no|num=3|constexpr=c++23|since=c++11|
float       fabsf( float num );
dcla|anchor=no|num=4|constexpr=c++23|since=c++11|
long double fabsl( long double num );
**Header:** `<`cmath`>`
dcla|anchor=no|num=A|constexpr=c++23|since=c++11|
template< class Integer >
double      fabs ( Integer num );
```

@1-4@ Computes the absolute value of the floating-point value `num`.<sup>(since C++23)</sup>  The library provides overloads of `std::abs` and `std::fabs` for all cv-unqualified floating-point types as the type of the parameter `num`.
rrev|since=c++11|
@A@ Additional overloads are provided for all integer types, which are treated as `double`.
For integral arguments, the integral overloads of `std::abs` are likely better matches. If `std::abs` is called with an unsigned integral argument that cannot be converted to `int` by integral promotion, the program is ill-formed.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If successful, returns the absolute value of `arg` (`). The value returned is exact and does not depend on any rounding modes.

## Error handling

This function is not subject to any of the error conditions specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, +0 is returned.
* If the argument is ±∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes


## Example


### Example

```cpp
#include <cmath>
#include <iostream>

int main()
{
    std::cout << "abs(+3.0) = " << std::abs(+3.0) << '\n'
              << "abs(-3.0) = " << std::abs(-3.0) << '\n';

    // special values
    std::cout << "abs(-0.0) = " << std::abs(-0.0) << '\n'
              << "abs(-Inf) = " << std::abs(-INFINITY) << '\n'
              << "abs(-NaN) = " << std::abs(-NAN) << '\n';
}
```


**Output:**
```
abs(+3.0) = 3
abs(-3.0) = 3
abs(-0.0) = 0
abs(-Inf) = inf
abs(-NaN) = nan
```


## Defect reports


## See also


| cpp/numeric/math/dsc abs | (see dedicated page) |
| cpp/numeric/math/dsc copysign | (see dedicated page) |
| cpp/numeric/math/dsc signbit | (see dedicated page) |
| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/valarray/dsc abs | (see dedicated page) |

