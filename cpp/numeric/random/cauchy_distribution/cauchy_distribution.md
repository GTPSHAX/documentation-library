---
title: std::cauchy_distribution::cauchy_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/cauchy_distribution/cauchy_distribution
---


```cpp
dcl|num=1|since=c++11|1=
cauchy_distribution() : cauchy_distribution(0.0) {}
dcl|num=2|since=c++11|1=
explicit cauchy_distribution( RealType a, RealType b = 1.0 );
dcl|num=3|since=c++11|1=
explicit cauchy_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `a` and `b` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `a` - the ''a'' distribution parameter (location)
- `b` - the ''b'' distribution parameter (scale)
- `params` - the distribution parameter set

## Defect reports

