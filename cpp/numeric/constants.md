---
title: Mathematical constants
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/constants
---


# Mathematical constants


## Constants <sup>(C++20)</sup>


| numbers | |
| std::numbers | |
| e_v|nolink=true|[E (mathematical constant)|the mathematical constant ](https://en.wikipedia.org/wiki/E (mathematical constant)|the mathematical constant ) | |
| dsc tvar|log2e_v|nolink=true|} | |
| dsc tvar|log10e_v|nolink=true|} | |
| pi_v|nolink=true|[Pi (mathematical constant)|the mathematical constant ](https://en.wikipedia.org/wiki/Pi (mathematical constant)|the mathematical constant ) | |
| inv_pi_v|nolink=true| | |
| dsc tvar|inv_sqrtpi_v|nolink=true|} | |
| dsc tvar|ln2_v|nolink=true|} | |
| dsc tvar|ln10_v|nolink=true|} | |
| sqrt2_v|nolink=true| | |
| sqrt3_v|nolink=true| | |
| dsc tvar|inv_sqrt3_v|nolink=true|} | |
| egamma_v|nolink=true|[Euler's constant|the Euler–Mascheroni constant γ](https://en.wikipedia.org/wiki/Euler's constant|the Euler–Mascheroni constant γ) | |
| phi_v|nolink=true|enwiki|Golden ratio|the golden ratio Φ (}) | |


## Notes

A program that instantiates a primary template of a mathematical constant variable template is ill-formed.
The standard library specializes mathematical constant variable templates for all floating-point types (i.e. `float`, `double``long double` <sup>(since C++23)</sup> , and ).
A program may partially or explicitly specialize a mathematical constant variable template provided that the specialization depends on a .

## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numbers>
#include <string_view>

auto egamma_aprox(const unsigned iterations)
{
    long double s{};
    for (unsigned m{2}; m != iterations; ++m)
        if (const long double t{std::riemann_zetal(m) / m}; m % 2)
            s -= t;
        else
            s += t;
    return s;
};

int main()
{
    using namespace std::numbers;
    using namespace std::string_view_literals;

    const auto x = std::sqrt(inv_pi) / inv_sqrtpi +
        std::ceil(std::exp2(log2e)) + sqrt3 * inv_sqrt3 + std::exp(0);
    const auto v = (phi * phi - phi) + 1 / std::log2(sqrt2) +
        log10e * ln10 + std::pow(e, ln2) - std::cos(pi);    
    std::cout << "The answer is " << x * v << '\n';

    constexpr auto γ{"0.577215664901532860606512090082402"sv};
    std::cout
        << "γ as 10⁶ sums of ±ζ(m)/m   = "
        << egamma_aprox(1'000'000) << '\n'
        << "γ as egamma_v<float>       = "
        << std::setprecision(std::numeric_limits<float>::digits10 + 1)
        << egamma_v<float> << '\n'
        << "γ as egamma_v<double>      = "
        << std::setprecision(std::numeric_limits<double>::digits10 + 1)
        << egamma_v<double> << '\n'
        << "γ as egamma_v<long double> = "
        << std::setprecision(std::numeric_limits<long double>::digits10 + 1)
        << egamma_v<long double> << '\n'
        << "γ with " << γ.length() - 1 << " digits precision = " << γ << '\n';
}
```


**Output:**
```
The answer is 42
γ as 10⁶ sums of ±ζ(m)/m   = 0.577215
γ as egamma_v<float>       = 0.5772157
γ as egamma_v<double>      = 0.5772156649015329
γ as egamma_v<long double> = 0.5772156649015328606
γ with 34 digits precision = 0.577215664901532860606512090082402
```


## See also


| cpp/numeric/ratio/dsc ratio | (see dedicated page) |

