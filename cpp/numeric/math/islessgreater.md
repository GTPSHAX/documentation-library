---
title: std::islessgreater
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/islessgreater
---

cpp/numeric/math/binary_is|islessgreater
|description=Determines if the floating point number `x` is less than or greater than the floating-point number `y`, without setting floating-point exceptions.
|condition=`x < y
|note=
The built-in `operator<` and `operator>` for floating-point numbers may raise `FE_INVALID` if one or both of the arguments is NaN. This function is a "quiet" version of the expression `x < y .

## See also


| cpp/numeric/math/dsc isless | (see dedicated page) |
| cpp/numeric/math/dsc isgreater | (see dedicated page) |

