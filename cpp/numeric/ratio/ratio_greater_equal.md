---
title: std::ratio_greater_equal
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio_greater_equal
---

ddcl|header=ratio|since=c++11|1=
template< class R1, class R2 >
struct ratio_greater_equal : std::integral_constant<bool, /* see below */> { };
If the ratio `R1` is greater than or equal to the ratio `R2`, provides the member constant `value` equal `true`. Otherwise, `value` is `false`.

## Helper variable template

ddcl|since=c++17|1=
template< class R1, class R2 >
constexpr bool ratio_greater_equal_v = ratio_greater_equal<R1, R2>::value;

## Example


### Example

```cpp
#include <ratio>

int main()
{
    static_assert(std::ratio_greater_equal<
        std::ratio<2, 3>,
        std::ratio<2, 3>>::value, "2/3 >= 2/3");

    // since C++17
    static_assert(std::ratio_greater_equal_v<
        std::ratio<999'998, 999'999>,
        std::ratio<999'997, 999'998>>);
}
```


## See also


| cpp/numeric/ratio/dsc ratio_equal | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_less | (see dedicated page) |

