---
title: std::pow(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/pow
---


# powsmall|(std::valarray)


```cpp
**Header:** `<`valarray`>`
dcl|num=1|
template< class T >
std::valarray<T> pow( const std::valarray<T>& base, const std::valarray<T>& exp );
dcl|num=2|
template< class T >
std::valarray<T> pow( const std::valarray<T>& base,
const typename std::valarray<T>::value_type& vexp );
dcl|num=3|
template< class T >
std::valarray<T> pow( const typename std::valarray<T>::value_type& vbase,
const std::valarray<T>& exp );
```

Raises a value to a power.
1. Computes the values of each element in the numeric array `base` raised to the power specified by the corresponding element from the numeric array `exp`.
The behavior is undefined if `1=base.size() != exp.size()`.
2. Computes the values of each element in the numeric array `base` raised to the power `vexp`.
3. Computes the values of `vbase` raised to the power defined by the elements in the numeric array `exp`.

## Parameters


### Parameters

- `base` - numeric array containing the values of the base
- `exp` - numeric array containing the values of the exponent
- `vbase` - a value defining the base
- `vexp` - a value defining the exponent

## Return value

A numeric array containing the results of exponentiation.

## Notes


## Example


### Example

```cpp
#include <cmath>
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <valarray>

class show
{
    friend std::ostream& operator<<(std::ostream& os, show const& r)
    {
        constexpr char const* sup[]
        {
            "\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074",
            "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"
        };

        for (std::size_t n = 0; n != r.bases.size(); ++n)
        {
            os << std::left << r.bases[n] << std::left;
            if (n < r.exponents.size())
                os << sup[r.exponents[n] % 10] << ' ';
            else
                os << "  ";
        }

        if (r.results.size() != 0)
        {
            os << '=';
            for (std::size_t n = 0; n != r.results.size(); ++n)
                os << ' ' << r.results[n];
        }

        return os << '\n';
    }

public:
    std::valarray<int> bases{}, exponents{}, results{};
};

int main()
{
    constexpr int base{2};
    constexpr int exponent{5};
    const std::valarray<int> bases{1, 2, 3, 4, 5, 6, 7};
    const std::valarray<int> exponents{0, 1, 2, 3, 4, 5, 6};
    const std::valarray<int> powers1 = std::pow(bases, exponents);
    const std::valarray<int> powers2 = std::pow(bases, exponent);
    const std::valarray<int> powers3 = std::pow(base, exponents);

    std::cout
        << "pow(const std::valarray<T>& base, const std::valarray<T>& exp); (1)\n"
        << "base : " << show{bases}
        << "exp  : " << show{exponents}
        << "pow  : " << show{bases, exponents, powers1}
        << '\n'
        << "pow(const std::valarray<T>& base, const value_type& vexp); (2)\n"
        << "base : " << show{bases}
        << "vexp : " << exponent << '\n'
        << "pow  : " << show{bases, std::valarray<int>(exponent, bases.size()), powers2}
        << '\n'
        << "pow(const value_type& vbase, const std::valarray<T>& exp); (3)\n"
        << "vbase: " << base << '\n'
        << "exp  : " << show{exponents}
        << "pow  : " << show{std::valarray<int>(base, bases.size()), exponents, powers3};
}
```


**Output:**
```
pow(const std::valarray<T>& base, const std::valarray<T>& exp); (1)
base : 1  2  3  4  5  6  7
exp  : 0  1  2  3  4  5  6
pow  : 1⁰ 2¹ 3² 4³ 5⁴ 6⁵ 7⁶ = 1 2 9 64 625 7776 117649

pow(const std::valarray<T>& base, const value_type& vexp); (2)
base : 1  2  3  4  5  6  7
vexp : 5
pow  : 1⁵ 2⁵ 3⁵ 4⁵ 5⁵ 6⁵ 7⁵ = 1 32 243 1024 3125 7776 16807

pow(const value_type& vbase, const std::valarray<T>& exp); (3)
vbase: 2
exp  : 0  1  2  3  4  5  6
pow  : 2⁰ 2¹ 2² 2³ 2⁴ 2⁵ 2⁶ = 1 2 4 8 16 32 64
```


## Defect reports


## See also


| cpp/numeric/valarray/dsc sqrt | (see dedicated page) |
| cpp/numeric/math/dsc pow | (see dedicated page) |
| cpp/numeric/complex/dsc pow | (see dedicated page) |

