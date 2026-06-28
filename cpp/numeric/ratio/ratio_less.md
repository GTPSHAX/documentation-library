---
title: std::ratio_less
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio_less
---

ddcl|header=ratio|since=c++11|1=
template< class R1, class R2 >
struct ratio_less : std::integral_constant<bool, /* see below */> { };
If the ratio `R1` is less than the ratio `R2`, provides the member constant `value` equal `true`. Otherwise, `value` is `false`.

## Helper variable template

ddcl|since=c++17|1=
template< class R1, class R2 >
constexpr bool ratio_less_v = ratio_less<R1, R2>::value;

## Example


### Example

```cpp
#include <iostream>
#include <ratio>

int main()
{
    using x = std::ratio<69, 90>;
    using y = std::ratio<70, 90>;

    if constexpr (std::ratio_less_v<x, y>)
        std::cout << x::num << '/' << x::den << " < "
                  << y::num << '/' << y::den << '\n';
}
```


**Output:**
```
23/30 < 7/9
```


## See also


| cpp/numeric/ratio/dsc ratio_greater | (see dedicated page) |

