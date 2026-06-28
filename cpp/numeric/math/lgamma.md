---
title: std::lgamma
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/lgamma
---

cpp/numeric/math/declarations
|family=lgamma
|param1=num
|constexpr_since=26
|desc=Computes the natural logarithm of the absolute value of the [gamma function](https://en.wikipedia.org/wiki/gamma function) of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, the value of the logarithm of the gamma function of `num`, that is mathjax-or|1=\(\log_{e}|{\int_0^\infty t^{num-1} e^{-t} \mathsf{d}t}|\)|2=log||, is returned.
If a pole error occurs, `HUGE_VAL|+HUGE_VAL`, `+HUGE_VALF`, or `+HUGE_VALL` is returned.
If a range error due to overflow occurs, `HUGE_VAL|±HUGE_VAL`, `±HUGE_VALF`, or `±HUGE_VALL` is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If `num` is zero or is an integer less than zero, a pole error may occur.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is 1, +0 is returned.
* If the argument is 2, +0 is returned.
* If the argument is ±0, +∞ is returned and `FE_DIVBYZERO` is raised.
* If the argument is a negative integer, +∞ is returned and `FE_DIVBYZERO` is raised.
* If the argument is ±∞, +∞ is returned.
* If the argument is NaN, NaN is returned.

## Notes

If `num` is a natural number, `std::lgamma(num)` is the logarithm of the factorial of `num - 1`.
The [https://pubs.opengroup.org/onlinepubs/9699919799/functions/lgamma.html POSIX version of `lgamma`] is not thread-safe: each execution of the function stores the sign of the gamma function of `num` in the static external variable `signgam`. Some implementations provide `lgamma_r`, which takes a pointer to user-provided storage for `singgam` as the second parameter, and is thread-safe.
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

const double pi = std::acos(-1); // or std::numbers::pi since C++20

int main()
{
    std::cout << "lgamma(10) = " << std::lgamma(10)
              << ", log(9!) = " << std::log(std::tgamma(10))
              << ", exp(lgamma(10)) = " << std::exp(std::lgamma(10)) << '\n'
              << "lgamma(0.5) = " << std::lgamma(0.5)
              << ", log(sqrt(pi)) = " << std::log(std::sqrt(pi)) << '\n';

    // special values
    std::cout << "lgamma(1) = " << std::lgamma(1) << '\n'
              << "lgamma(+Inf) = " << std::lgamma(INFINITY) << '\n';

    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);

    std::cout << "lgamma(0) = " << std::lgamma(0) << '\n';

    if (errno == ERANGE)
        std::cout << "    errno == ERANGE: " << std::strerror(errno) << '\n';
    if (std::fetestexcept(FE_DIVBYZERO))
        std::cout << "    FE_DIVBYZERO raised\n";
}
```


**Output:**
```
lgamma(10) = 12.8018, log(9!) = 12.8018, exp(lgamma(10)) = 362880
lgamma(0.5) = 0.572365, log(sqrt(pi)) = 0.572365
lgamma(1) = 0
lgamma(+Inf) = inf
lgamma(0) = inf
    errno == ERANGE: Numerical result out of range
    FE_DIVBYZERO raised
```


## See also


| cpp/numeric/math/dsc tgamma | (see dedicated page) |


## External links

