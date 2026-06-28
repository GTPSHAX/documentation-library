---
title: std::cauchy_distribution::a
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/cauchy_distribution/params
---


```cpp
dcl|since=c++11|num=1|
RealType a() const;
dcl|since=c++11|num=2|
RealType b() const;
```

Returns the distribution parameters with which the distribution was constructed.
1. Returns the ''a'' parameter. It specifies the location of the peak and is also called location parameter. The default value is `0.0`.
2. Returns the ''b'' parameter. It represents the half-width at half-maximum (HWHM) and is also called scale parameter. The default value is `1.0`.

## Parameters

(none)

## Return value

1. The value of the ''a'' parameter.
2. The value of the ''b'' parameter.

## See also


| cpp/numeric/random/distribution/dsc param|cauchy_distribution | (see dedicated page) |


## External links

