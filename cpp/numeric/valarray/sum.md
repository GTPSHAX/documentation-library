---
title: std::valarray::sum
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/sum
---

ddcl |
T sum() const;
Computes the sum of the elements.
The function can be used only if `operator+ is defined for type `T`. If the `std::valarray` is empty, the behavior is undefined. The order in which the elements are processed by this function is unspecified.

## Parameters

(none)

## Return value

The sum of the elements.

## Example


## See also

