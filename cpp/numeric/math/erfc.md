---
title: std::erfc
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/erfc
---

cpp/numeric/math/declarations
|family=erfc
|param1=num
|constexpr_since=26
|desc=Computes the [Complementary error function|complementary error function](https://en.wikipedia.org/wiki/Complementary error function|complementary error function) of `num`, that is `1.0 - std::erf(num)`, but without loss of precision for large `num`.

## Parameters


### Parameters

- `num` - floating-point or integer value

## Return value

If no errors occur, value of the complementary error function of `num`, that is mathjax-or|\(\frac{2}{\sqrt{\pi} }\int_{num}^{\infty}{e^{-{t^2} }\mathsf{d}t}\)| or mathjax-or|\({\small 1-\operatorname{erf}(num)}\)|1-erf(num), is returned.
If a range error occurs due to underflow, the correct result (after rounding) is returned.

## Error handling

Errors are reported as specified in `math_errhandling`.
If the implementation supports IEEE floating-point arithmetic (IEC 60559),
* If the argument is +∞, +0 is returned.
* If the argument is -∞, 2 is returned.
* If the argument is NaN, NaN is returned.

## Notes

For the IEEE-compatible type `double`, underflow is guaranteed if `num > 26.55`.

## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>

double normalCDF(double x) // Phi(-∞, x) aka N(x)
{
    return std::erfc(-x / std::sqrt(2)) / 2;
}

int main()
{
    std::cout << "normal cumulative distribution function:\n"
              << std::fixed << std::setprecision(2);
    for (double n = 0; n < 1; n += 0.1)
        std::cout << "normalCDF(" << n << ") = " << 100 * normalCDF(n) << "%\n";

    std::cout << "special values:\n"
              << "erfc(-Inf) = " << std::erfc(-INFINITY) << '\n'
              << "erfc(Inf) = " << std::erfc(INFINITY) << '\n';
}
```


**Output:**
```
normal cumulative distribution function:
normalCDF(0.00) = 50.00%
normalCDF(0.10) = 53.98%
normalCDF(0.20) = 57.93%
normalCDF(0.30) = 61.79%
normalCDF(0.40) = 65.54%
normalCDF(0.50) = 69.15%
normalCDF(0.60) = 72.57%
normalCDF(0.70) = 75.80%
normalCDF(0.80) = 78.81%
normalCDF(0.90) = 81.59%
normalCDF(1.00) = 84.13%
special values:
erfc(-Inf) = 2.00
erfc(Inf) = 0.00
```


## See also


| cpp/numeric/math/dsc erf | (see dedicated page) |


## External links

