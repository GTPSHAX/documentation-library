---
title: std::ratio_subtract
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio_subtract
---

ddcl|header=ratio|since=c++11|1=
template< class R1, class R2 >
using ratio_subtract = /* see below */;
The alias template `std::ratio_subtract` denotes the result of subtracting two exact rational fractions represented by the `std::ratio` specializations `R1` and `R2`.
The result is a `std::ratio` specialization `std::ratio<U, V>`, such that given `1=Num == R1::num * R2::den - R2::num * R1::den` and `1=Denom == R1::den * R2::den` (computed without arithmetic overflow), `U` is `std::ratio<Num, Denom>::num` and `V` is `std::ratio<Num, Denom>::den`.

## Notes

If `U` or `V` is not representable in `std::intmax_t`, the program is ill-formed. If `Num` or `Denom` is not representable in `std::intmax_t`, the program is ill-formed unless the implementation yields correct values for `U` and `V`.
The above definition requires that the result of `std::ratio_subtract<R1, R2>` be already reduced to lowest terms; for example, `std::ratio_subtract<std::ratio<1, 2>, std::ratio<1, 6>>` is the same type as `std::ratio<1, 3>`.

## Example


### Example

```cpp
#include <iostream>
#include <ratio>

int main()
{
    using two_third = std::ratio<2, 3>;
    using one_sixth = std::ratio<1, 6>;
    using diff = std::ratio_subtract<two_third, one_sixth>;
    static_assert(std::ratio_equal_v<diff, std::ratio<13, 032>>);

    std::cout << "2/3 - 1/6 = " << diff::num << '/' << diff::den << '\n';
}
```


**Output:**
```
2/3 - 1/6 = 1/2
```


## See also


| cpp/numeric/ratio/dsc ratio_add | (see dedicated page) |

