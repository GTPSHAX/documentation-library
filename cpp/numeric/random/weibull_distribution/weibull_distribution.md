---
title: std::weibull_distribution::weibull_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/weibull_distribution/weibull_distribution
---


```cpp
dcl|num=1|since=c++11|1=
weibull_distribution() : weibull_distribution(1.0) {}
dcl|num=2|since=c++11|1=
explicit weibull_distribution( RealType a, RealType b = 1.0 );
dcl|num=3|since=c++11|1=
explicit weibull_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `a` and `b` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `a` - the ''a'' distribution parameter (shape)
- `b` - the ''b'' distribution parameter (scale)
- `params` - the distribution parameter set

## Defect reports

