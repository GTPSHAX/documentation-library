---
title: std::isless
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isless
---

cpp/numeric/math/binary_is|isless
|description= Determines if the floating point number `x` is less than the floating-point number `y`, without setting floating-point exceptions.
|condition=`x < y`
|note=The built-in `operator<` for floating-point numbers may raise `FE_INVALID` if one or both of the arguments is NaN. This function is a "quiet" version of `operator<`.

## See also


| cpp/utility/functional/dsc less | (see dedicated page) |
| cpp/numeric/math/dsc isgreater | (see dedicated page) |

