---
title: std::isgreater
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isgreater
---

cpp/numeric/math/binary_is|isgreater
|description= Determines if the floating point number `x` is greater than the floating-point number `y`, without setting floating-point exceptions.
|condition=`x > y`
|note=The built-in `operator>` for floating-point numbers may set `FE_INVALID` if one or both of the arguments is NaN. This function is a "quiet" version of `operator>`.

## See also


| cpp/utility/functional/dsc greater | (see dedicated page) |
| cpp/numeric/math/dsc isless | (see dedicated page) |

