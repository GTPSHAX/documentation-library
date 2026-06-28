---
title: std::abs
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/abs
---


```cpp
**Header:** `<`cstdlib`>`
**Header:** `<`cmath`>`
dcla|anchor=no|num=1|constexpr=c++23|
int       abs( int num );
dcla|anchor=no|num=2|constexpr=c++23|
long      abs( long num );
dcla|anchor=no|num=3|since=c++11|constexpr=c++23|
long long abs( long long num );
**Header:** `<`cstdlib`>`
dcla|anchor=no|num=4|constexpr=c++23|
long       labs( long num );
dcla|anchor=no|num=5|since=c++11|constexpr=c++23|
long long llabs( long long num );
**Header:** `<`cinttypes`>`
dcla|anchor=no|num=6|since=c++11|constexpr=c++23|
std::intmax_t abs( std::intmax_t num );
dcla|anchor=no|num=7|since=c++11|constexpr=c++23|
std::intmax_t imaxabs( std::intmax_t num );
```

Computes the absolute value of the integer number `num`. The behavior is undefined if the result cannot be represented by the return type.
If `std::abs` is called with an unsigned integral argument that cannot be converted to `int` by integral promotion, the program is ill-formed.
rrev|since=c++11|
Overload  of `std::abs` for `std::intmax_t` is provided in  if and only if `std::intmax_t` is an extended integer type.

## Parameters


### Parameters

- `num` - integer value

## Return value

The absolute value of `num` (i.e. `), if it is representable.

## Notes

In 2's complement systems, the absolute value of the most-negative value is out of range, e.g. for 32-bit 2's complement type `int`, `INT_MIN` is `-2147483648`, but the would-be result `2147483648` is greater than `INT_MAX`, which is `2147483647`.

## Example


### Example

```cpp
#include <climits>
#include <cstdlib>
#include <iostream>

int main()
{
    std::cout << std::showpos
              << "abs(+3) = " << std::abs(3) << '\n'
              << "abs(-3) = " << std::abs(-3) << '\n';

//  std::cout << std::abs(INT_MIN); // undefined behavior on 2's complement systems
}
```


**Output:**
```
abs(+3) = +3
abs(-3) = +3
```


## Defect reports


## See also


| cpp/numeric/math/dsc fabs | (see dedicated page) |
| cpp/numeric/complex/dsc abs | (see dedicated page) |
| cpp/numeric/valarray/dsc abs | (see dedicated page) |

