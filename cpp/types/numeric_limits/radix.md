---
title: std::numeric_limits::radix
type: Utilities
source: https://en.cppreference.com/w/cpp/types/numeric_limits/radix
---


```cpp
dcl rev multi|until1=c++11
|dcl1=
static const int radix;
|dcl2=
static constexpr int radix;
```

The value of `std::numeric_limits<T>::radix` is the base of the number system used in the representation of the type. It is `2` for all binary numeric types, but it may be, for example, `10` for IEEE 754 [Decimal64 floating-point format|decimal floating-point types](https://en.wikipedia.org/wiki/Decimal64 floating-point format|decimal floating-point types) or for third-party [binary-coded decimal](https://en.wikipedia.org/wiki/binary-coded decimal) integers. This constant is meaningful for all specializations.

## Standard specializations


## See also


| cpp/types/numeric_limits/dsc digits | (see dedicated page) |
| cpp/types/numeric_limits/dsc min_exponent | (see dedicated page) |
| cpp/types/numeric_limits/dsc max_exponent | (see dedicated page) |

