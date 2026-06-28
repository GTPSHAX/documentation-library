---
title: std::lognormal_distribution::lognormal_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/lognormal_distribution/lognormal_distribution
---


```cpp
dcl|num=1|since=c++11|1=
lognormal_distribution() : lognormal_distribution(0.0) {}
dcl|num=2|since=c++11|1=
explicit lognormal_distribution( RealType m, RealType s = 1.0 );
dcl|num=3|since=c++11|1=
explicit lognormal_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `m` and `s` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `m` - the ''m'' distribution parameter (log-scale)
- `s` - the ''s'' distribution parameter (shape)
- `params` - the distribution parameter set

## Defect reports

