---
title: std::gamma_distribution::gamma_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/gamma_distribution/gamma_distribution
---


```cpp
dcl|num=1|since=c++11|1=
gamma_distribution() : gamma_distribution(1.0) {}
dcl|num=2|since=c++11|1=
explicit gamma_distribution( RealType alpha, RealType beta = 1.0 );
dcl|num=3|since=c++11|1=
explicit gamma_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `alpha` and `beta` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `alpha` - the ''α'' distribution parameter (shape)
- `beta` - the ''β'' distribution parameter (scale)
- `params` - the distribution parameter set

## Defect reports

