---
title: std::beta
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/special_functions/beta
---


```cpp
**Header:** `<`cmath`>`
dcl rev multi|num=1|since1=c++17|dcl1=
float       beta ( float x, float y );
double      beta ( double x, double y );
long double beta ( long double x, long double y );
|since2=c++23|dcl2=
/* floating-point-type */ beta( /* floating-point-type */ x,
/* floating-point-type */ y );
dcl|num=2|since=c++17|
float       betaf( float x, float y );
dcl|num=3|since=c++17|
long double betal( long double x, long double y );
**Header:** `<`cmath`>`
dcl|num=A|since=c++17|
template< class Arithmetic1, class Arithmetic2 >
/* common-floating-point-type */ beta( Arithmetic1 x, Arithmetic2 y );
```

@1-3@ Computes the [Beta function](https://en.wikipedia.org/wiki/Beta function) of `x` and `y`.<sup>(since C++23)</sup>  The library provides overloads of `std::beta` for all cv-unqualified floating-point types as the type of the parameters `x` and `y`.
@A@ Additional overloads are provided for all other combinations of arithmetic types.

## Parameters


### Parameters

- `x, y` - floating-point or integer values

## Return value

If no errors occur, value of the beta function of `x` and `y`, that is mathjax-or|\(\int_{0}^{1}{ {t}^{x-1}{(1-t)}^{y-1}\mathsf{d}t}\)|, or, equivalently, mathjax-or|\(\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}\)| is returned.

## Error handling

Errors may be reported as specified in `math_errhandling`.
* If any argument is NaN, NaN is returned and domain error is not reported.
* The function is only required to be defined where both `x` and `y` are greater than zero, and is allowed to report a domain error otherwise.

## Notes

An implementation of this function is also [https://www.boost.org/doc/libs/release/libs/math/doc/html/math_toolkit/sf_beta/beta_function.html available in boost.math].
`std::beta(x, y)` equals `std::beta(y, x)`.
When `x` and `y` are positive integers, `std::beta(x, y)` equals mathjax-or|1=\(\frac{(x-1)!(y-1)!}{(x+y-1)!}\)|2=.
Binomial coefficients can be expressed in terms of the beta function: mathjax-or|1=\(\binom{n}{k} = \frac{1}{(n+1)B(n-k+1,k+1)}\)|2==.

## Example


### Example

```cpp
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <numbers>
#include <string>

long binom_via_beta(int n, int k)
{
    return std::lround(1 / ((n + 1) * std::beta(n - k + 1, k + 1)));
}

long binom_via_gamma(int n, int k)
{
    return std::lround(std::tgamma(n + 1) /
                      (std::tgamma(n - k + 1) * 
                       std::tgamma(k + 1)));
}

int main()
{
    std::cout << "Pascal's triangle:\n";
    for (int n = 1; n < 10; ++n)
    {
        std::cout << std::string(20 - n * 2, ' ');
        for (int k = 1; k < n; ++k)
        {
            std::cout << std::setw(3) << binom_via_beta(n, k) << ' ';
            assert(binom_via_beta(n, k) == binom_via_gamma(n, k));
        }
        std::cout << '\n';
    }

    // A spot-check
    const long double p = 0.123; // a random value in [0, 1]
    const long double q = 1 - p;
    const long double π = std::numbers::pi_v<long double>;
    std::cout << "\n\n" << std::setprecision(19)
              << "β(p,1-p)   = " << std::beta(p, q) << '\n'
              << "π/sin(π*p) = " << π / std::sin(π * p) << '\n';
}
```


**Output:**
```
Pascal's triangle:

                  2
                3   3
              4   6   4
            5  10  10   5
          6  15  20  15   6
        7  21  35  35  21   7
      8  28  56  70  56  28   8
    9  36  84 126 126  84  36   9

β(p,1-p)   = 8.335989149587307836
π/sin(π*p) = 8.335989149587307834
```


## See also


| cpp/numeric/math/dsc tgamma | (see dedicated page) |


## External links

