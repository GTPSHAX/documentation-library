---
title: std::erf
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/erf
---

cpp/numeric/math/declarations
|family=erf
|param1=num
|constexpr_since=26
|desc=Computes the [Error function|error function](https://en.wikipedia.org/wiki/Error function|error function) of `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, value of the error function of `num`, that is mathjax-or|\(\frac{2}{\sqrt{\pi} }\int_{0}^{num}{e^{-{t^2} }\mathsf{d}t}\)|, is returned.<br>
If a range error occurs due to underflow, the correct result (after rounding), that is mathjax-or|\(\frac{2\cdot num}{\sqrt{\pi} }\)| is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is ±0, ±0 is returned.
* If the argument is ±∞, ±1 is returned.
* If the argument is NaN, NaN is returned.

## Notes

Underflow is guaranteed if `.
mathjax-or|\(\operatorname{erf}(\frac{x}{\sigma \sqrt{2} })\)|erf() is the probability that a measurement whose errors are subject to a normal distribution with standard deviation  is less than  away from the mean value.

## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>

double phi(double x1, double x2)
{
    return (std::erf(x2 / std::sqrt(2)) - std::erf(x1 / std::sqrt(2))) / 2;
}

int main()
{
    std::cout << "Normal variate probabilities:\n"
              << std::fixed << std::setprecision(2);
    for (int n = -4; n < 4; ++n)
        std::cout << '[' << std::setw(2) << n
                  << ':' << std::setw(2) << n + 1 << "]: "
                  << std::setw(5) << 100 * phi(n, n + 1) << "%\n";

    std::cout << "Special values:\n"
              << "erf(-0) = " << std::erf(-0.0) << '\n'
              << "erf(Inf) = " << std::erf(INFINITY) << '\n';
}
```


**Output:**
```
Normal variate probabilities:
[-4:-3]:  0.13%
[-3:-2]:  2.14%
[-2:-1]: 13.59%
[-1: 0]: 34.13%
[ 0: 1]: 34.13%
[ 1: 2]: 13.59%
[ 2: 3]:  2.14%
[ 3: 4]:  0.13%
Special values:
erf(-0) = -0.00
erf(Inf) = 1.00
```


## See also


| cpp/numeric/math/dsc erfc | (see dedicated page) |


## External links

