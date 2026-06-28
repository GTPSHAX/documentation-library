---
title: std::fpclassify
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/fpclassify
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++11|dcl1=
int fpclassify( float num );
int fpclassify( double num );
int fpclassify( long double num );
|since2=c++23|dcl2=
constexpr int fpclassify( /* floating-point-type */ num );
**Header:** `<`cmath`>`
|
template< class Integer >
int fpclassify( Integer num );
```

1. Categorizes floating point value `num` into the following categories: zero, subnormal, normal, infinite, NAN, or implementation-defined category.<sup>(since C++23)</sup>  The library provides overloads of `std::fpclassify` for all cv-unqualified floating-point types as the type of the parameter `num`.
@A@ Additional overloads are provided for all integer types, which are treated as `double`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

one of `FP_INFINITE`, `FP_NAN`, `FP_NORMAL`, `FP_SUBNORMAL`, `FP_ZERO` or implementation-defined type, specifying the category of `num`.

## Notes


## Example


### Example

```cpp
#include <cfloat>
#include <cmath>
#include <iostream>

auto show_classification(double x)
{
    switch (std::fpclassify(x))
    {
        case FP_INFINITE:
            return "Inf";
        case FP_NAN:
            return "NaN";
        case FP_NORMAL:
            return "normal";
        case FP_SUBNORMAL:
            return "subnormal";
        case FP_ZERO:
            return "zero";
        default:
            return "unknown";
    }
}

int main()
{
    std::cout << "1.0/0.0 is " << show_classification(1 / 0.0) << '\n'
              << "0.0/0.0 is " << show_classification(0.0 / 0.0) << '\n'
              << "DBL_MIN/2 is " << show_classification(DBL_MIN / 2) << '\n'
              << "-0.0 is " << show_classification(-0.0) << '\n'
              << "1.0 is " << show_classification(1.0) << '\n';
}
```


**Output:**
```
1.0/0.0 is Inf
0.0/0.0 is NaN
DBL_MIN/2 is subnormal
-0.0 is zero
1.0 is normal
```


## See also


| cpp/numeric/math/dsc isfinite | (see dedicated page) |
| cpp/numeric/math/dsc isinf | (see dedicated page) |
| cpp/numeric/math/dsc isnan | (see dedicated page) |
| cpp/numeric/math/dsc isnormal | (see dedicated page) |
| cpp/types/dsc numeric_limits | (see dedicated page) |

