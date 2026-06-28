---
title: beta
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/gamma_distribution/params
---


```cpp
dcl|since=c++11|num=1|1=
RealType alpha() const;
dcl|since=c++11|num=2|1=
RealType beta() const;
```

Returns the distribution parameters the distribution has been constructed with.
1. Returns the $α$ distribution parameter. It is also known as the shape parameter. The default value is `1.0`.
2. Returns the $β$ distribution parameter. It is also known as the scale parameter. The default value is `1.0`.

## Parameters

(none)

## Return value

1. Floating point value identifying the $α$ parameter.
2. Floating point value identifying the $β$ parameter.

## See also


| cpp/numeric/random/distribution/dsc param|gamma_distribution | (see dedicated page) |

