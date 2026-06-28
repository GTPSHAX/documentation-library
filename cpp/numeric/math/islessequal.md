---
title: std::islessequal
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/islessequal
---

cpp/numeric/math/binary_is|islessequal
|description= Determines if the floating point number `x` is less than or equal to the floating-point number `y`, without setting floating-point exceptions.
|condition=`1=x <= y`
|note=
The built-in `1=operator<=` for floating-point numbers may raise `FE_INVALID` if one or both of the arguments is NaN. This function is a "quiet" version of `1=operator<=`.

## See also


| cpp/utility/functional/dsc less_equal | (see dedicated page) |
| cpp/numeric/math/dsc isgreaterequal | (see dedicated page) |

