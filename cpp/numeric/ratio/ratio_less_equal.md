---
title: std::ratio_less_equal
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio_less_equal
---

ddcl|header=ratio|since=c++11|1=
template< class R1, class R2 >
struct ratio_less_equal : std::integral_constant<bool, /* see below */> { };
If the ratio `R1` is less than or equal to the ratio `R2`, provides the member constant `value` equal `true`. Otherwise, `value` is `false`.

## Helper variable template

ddcl|since=c++17|1=
template< class R1, class R2 >
constexpr bool ratio_less_equal_v = ratio_less_equal<R1, R2>::value;

## Example


### Example

```cpp
#include <iostream>
#include <ratio>

int main()
{
    static_assert(std::ratio_less_equal<std::ratio<1, 2>, std::ratio<3, 4>>::value,
                  "1/2 <= 3/4");

    if (std::ratio_less_equal<std::ratio<10,11>, std::ratio<11,12>>::value)
        std::cout << "10/11 <= 11/12" "\n";

    static_assert(std::ratio_less_equal_v<std::ratio<10, 11>, std::ratio<11, 12>>);

    if constexpr (std::ratio_less_equal_v<std::ratio<10, 11>, std::ratio<11, 12>>)
        std::cout << "11/12 <= 12/13" "\n";
}
```


**Output:**
```
10/11 <= 11/12
11/12 <= 12/13
```


## See also


| cpp/numeric/ratio/dsc ratio_equal | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_not_equal | (see dedicated page) |

