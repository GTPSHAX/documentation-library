---
title: std::ratio_equal
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio_equal
---

ddcl|header=ratio|since=c++11|1=
template< class R1, class R2 >
struct ratio_equal : std::integral_constant<bool, /* see below */> { };
If the ratios `R1` and `R2` are equal, provides the member constant `value` equal `true`. Otherwise, `value` is `false`.

## Helper variable template

ddcl|since=c++17|1=
template< class R1, class R2 >
constexpr bool ratio_equal_v = ratio_equal<R1, R2>::value;

## Possible implementation

eq fun
|1=
template< class R1, class R2 >
struct ratio_equal : public std::integral_constant <
bool,
R1::num == R2::num && R1::den == R2::den
> {};

## Example


### Example

```cpp
#include <iostream>
#include <ratio>

int main()
{
    constexpr bool equ = std::ratio_equal_v<std::ratio<2,3>,
                                            std::ratio<6,9>>;
    static_assert(equ);
    std::cout << "2/3 " << (equ ? "==" : "!=") << " 6/9\n";
}
```


**Output:**
```
2/3 == 6/9
```


## See also


| cpp/numeric/ratio/dsc ratio_not_equal | (see dedicated page) |

