---
title: std::div
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/div
---


```cpp
**Header:** `<`cstdlib`>`
|
std::div_t     div( int x, int y );
|
std::ldiv_t    div( long x, long y );
dcla|anchor=no|since=c++11|num=3|constexpr=c++23|
std::lldiv_t   div( long long x, long long y );
dcla|anchor=no|num=4|constexpr=c++23|
std::ldiv_t   ldiv( long x, long y );
dcla|anchor=no|since=c++11|num=5|constexpr=c++23|
std::lldiv_t lldiv( long long x, long long y );
**Header:** `<`cinttypes`>`
dcla|anchor=no|since=c++11|num=6|constexpr=c++23|
std::imaxdiv_t div( std::intmax_t x, std::intmax_t y );
dcla|anchor=no|since=c++11|num=7|constexpr=c++23|
std::imaxdiv_t imaxdiv( std::intmax_t x, std::intmax_t y );
```

Computes both the quotient and the remainder of the division of the numerator `x` by the denominator `y`.
rrev|since=c++11|
@6,7@ Overload of `std::div` for `std::intmax_t` is provided in  if and only if `std::intmax_t` is an extended integer type.
<br>
rrev multi
|rev1=
The quotient is the algebraic quotient with any fractional part discarded (truncated towards zero). The remainder is such that `1=quot * y + rem == x`.
|since2=c++11|rev2=
The quotient is the result of the expression `x / y`. The remainder is the result of the expression `x % y`.

## Parameters


### Parameters

- `x, y` - integer values

## Return value

If both the remainder and the quotient can be represented as objects of the corresponding type (`int`, `long`, `long long`, `std::intmax_t`, respectively), returns both as an object of type `std::div_t`, `std::ldiv_t`, `std::lldiv_t`, `std::imaxdiv_t` defined as follows:
member|div_t|2=

```cpp
struct div_t { int quot; int rem; };
```

or

```cpp
struct div_t { int rem; int quot; };
```

member|ldiv_t|2=

```cpp
struct ldiv_t { long quot; long rem; };
```

or

```cpp
struct ldiv_t { long rem; long quot; };
```

member|lldiv_t|2=

```cpp
struct lldiv_t { long long quot; long long rem; };
```

or

```cpp
struct lldiv_t { long long rem; long long quot; };
```

member|imaxdiv_t|2=

```cpp
struct imaxdiv_t { std::intmax_t quot; std::intmax_t rem; };
```

or

```cpp
struct imaxdiv_t { std::intmax_t rem; std::intmax_t quot; };
```

If either the remainder or the quotient cannot be represented, the behavior is undefined.

## Notes

Until  was resolved (), the rounding direction of the quotient and the sign of the remainder in the built-in division and remainder operators was implementation-defined if either of the operands was negative, but it was well-defined in `std::div`.
On many platforms, a single CPU instruction obtains both the quotient and the remainder, and this function may leverage that, although compilers are generally able to merge nearby `/` and `%` where suitable.

## Example


### Example

```cpp
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>

std::string division_with_remainder_string(int dividend, int divisor)
{
    auto dv = std::div(dividend, divisor);
    assert(dividend == divisor * dv.quot + dv.rem);
    assert(dv.quot == dividend / divisor);
    assert(dv.rem == dividend % divisor);

    auto sign = [](int n){ return n > 0 ? 1 : n < 0 ? -1 : 0; };
    assert((dv.rem == 0) or (sign(dv.rem) == sign(dividend)));

    return (std::ostringstream() << std::showpos << dividend << " = "
                                 << divisor << " * (" << dv.quot << ") "
                                 << std::showpos << dv.rem).str();
}

std::string itoa(int n, int radix /*[2..16]*/)
{
    std::string buf;
    std::div_t dv{}; dv.quot = n;

    do
    {
        dv = std::div(dv.quot, radix);
        buf += "0123456789abcdef"[std::abs(dv.rem)]; // string literals are arrays
    }
    while (dv.quot);

    if (n < 0)
        buf += '-';

    return {buf.rbegin(), buf.rend()};
}

int main()
{
    std::cout << division_with_remainder_string(369, 10) << '\n'
              << division_with_remainder_string(369, -10) << '\n'
              << division_with_remainder_string(-369, 10) << '\n'
              << division_with_remainder_string(-369, -10) << "\n\n";

    std::cout << itoa(12345, 10) << '\n'
              << itoa(-12345, 10) << '\n'
              << itoa(42, 2) << '\n'
              << itoa(65535, 16) << '\n';
}
```


**Output:**
```
+369 = +10 * (+36) +9
+369 = -10 * (-36) +9
-369 = +10 * (-36) -9
-369 = -10 * (+36) -9

12345
-12345
101010
ffff
```


## See also


| cpp/numeric/math/dsc fmod | (see dedicated page) |
| cpp/numeric/math/dsc remainder | (see dedicated page) |
| cpp/numeric/math/dsc remquo | (see dedicated page) |


## External links

