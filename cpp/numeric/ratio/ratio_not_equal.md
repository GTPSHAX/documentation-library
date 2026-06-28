---
title: std::ratio_not_equal
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio/ratio_not_equal
---

ddcl|header=ratio|since=c++11|1=
template< class R1, class R2 >
struct ratio_not_equal : std::integral_constant<bool, /* see below */> { };
If the ratios `R1` and `R2` are not equal, provides the member constant `value` equal `true`. Otherwise, `value` is `false`.

## Helper variable template

ddcl|since=c++17|1=
template< class R1, class R2 >
constexpr bool ratio_not_equal_v = ratio_not_equal<R1, R2>::value;

## Possible implementation

eq fun
|1=
template< class R1, class R2 >
struct ratio_not_equal : std::integral_constant <
bool,
!std::ratio_equal<R1, R2>
> {};

## Example


### Example

```cpp
#include <ratio>

static_assert(std::ratio_not_equal_v<std::ratio<6, 9>, std::ratio<9, 6>>, "6/9 != 9/6");

int main() {}
```


## See also


| cpp/numeric/ratio/dsc ratio_equal | (see dedicated page) |

