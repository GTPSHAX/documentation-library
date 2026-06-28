---
title: std::tgamma
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/tgamma
---

cpp/numeric/math/declarations
|family=tgamma
|param1=num
|constexpr_since=26
|desc=Computes the [Gamma function|gamma function](https://en.wikipedia.org/wiki/Gamma function|gamma function) of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the value of the gamma function of `num`, that is mathjax-or|1=\(\Gamma(\mathtt{num}) = \displaystyle\int_0^\infty\!\! t^{\mathtt{num}-1} e^{-t}\, dt\)|2=, is returned.
If a domain error occurs, an implementation-defined value (NaN where supported) is returned.
If a pole error occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.
If a range error due to overflow occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.
If a range error due to underflow occurs, the correct value (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If `num` is zero or is an integer less than zero, a pole error or a domain error may occur.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, ±∞ is returned and `FE_DIVBYZERO` is raised.
* If the argument is a negative integer, NaN is returned and `FE_INVALID` is raised.
* If the argument is -∞, NaN is returned and `FE_INVALID` is raised.
* If the argument is +∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes

If `num` is a natural number, `std::tgamma(num)` is the factorial of `num - 1`. Many implementations calculate the exact integer-domain factorial if the argument is a sufficiently small integer.
For IEEE-compatible type `double`, overflow happens if `0 < num && num < 1 / DBL_MAX` or if `num > 171.7`.
[https://pubs.opengroup.org/onlinepubs/9699919799/functions/tgamma.html POSIX requires] that a pole error occurs if the argument is zero, but a domain error occurs when the argument is a negative integer. It also specifies that in future, domain errors may be replaced by pole errors for negative integer arguments (in which case the return value in those cases would change from NaN to ±∞).
There is a non-standard function named `gamma` in various implementations, but its definition is inconsistent. For example, glibc and 4.2BSD version of `gamma` executes `lgamma`, but 4.4BSD version of `gamma` executes `tgamma`.

## Example


### Example

```cpp
#include <cerrno>
#include <cfenv>
#include <cmath>
#include <cstring>
#include <iostream>
// #pragma STDC FENV_ACCESS ON

int main()
{
    std::cout << "tgamma(10) = " << std::tgamma(10)
              << ", 9! = " << 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 << '\n'
              << "tgamma(0.5) = " << std::tgamma(0.5)
              << ", sqrt(pi) = " << std::sqrt(std::acos(-1)) << '\n';

    // special values
    std::cout << "tgamma(1) = " << std::tgamma(1) << '\n'
              << "tgamma(+Inf) = " << std::tgamma(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "tgamma(-1) = " << std::tgamma(-1) << '\n';

    if (errno == EDOM)
        std::cout << "    errno == EDOM: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout << "    FE_INVALID raised\n";
}
```


**Output:**
```
tgamma(10) = 362880, 9! = 362880
tgamma(0.5) = 1.77245, sqrt(pi) = 1.77245
tgamma(1) = 1
tgamma(+Inf) = inf
tgamma(-1) = nan
    errno == EDOM: Numerical argument out of domain
    FE_INVALID raised
```


## See also


| cpp/numeric/math/dsc lgamma | (see dedicated page) |
| cpp/numeric/special_functions/dsc beta | (see dedicated page) |


## External links

