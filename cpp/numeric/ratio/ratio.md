---
title: std::ratio
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio
---

ddcl|header=ratio|since=c++11|1=
template<
std::intmax_t Num,
std::intmax_t Denom = 1
> class ratio;
The class template `std::ratio` provides `compile-time rational arithmetic` support. Each instantiation of this template exactly represents any finite rational number as long as its numerator `Num` and denominator `Denom` are representable as compile-time constants of type `std::intmax_t`. In addition, `Denom` may not be zero and both `Num` and `Denom` may not be equal to the most negative value.
The static data members `num` and `den` representing the numerator and denominator are calculated by dividing `Num` and `Denom` by their greatest common divisor. However, two `std::ratio` with different `Num` or `Denom` are distinct types even if they represent the same rational number (after reduction). A `std::ratio` type can be reduced to the lowest terms via its `type` member: `std::ratio<3, 6>::type` is `std::ratio<1, 2>`.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members

In the definitions given below,
* `sign(Denom)` is `-1` if `Denom` is negative, or `1` otherwise; and
* `gcd(Num, Denom)` is the greatest common divisor of `std::abs(Num)` and `std::abs(Denom)`.


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Notes


## Example


## See also


| cpp/numeric/dsc mathematical constants | (see dedicated page) |

