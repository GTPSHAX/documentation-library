---
title: std::chi_squared_distribution::chi_squared_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/chi_squared_distribution/chi_squared_distribution
---


```cpp
dcl|num=1|since=c++11|1=
chi_squared_distribution() : chi_squared_distribution(1.0) {}
dcl|num=2|since=c++11|1=
explicit chi_squared_distribution( RealType n );
dcl|num=3|since=c++11|1=
explicit chi_squared_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `n` as the distribution parameter.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `n` - the ''n'' distribution parameter (degrees of freedom)
- `params` - the distribution parameter set

## Defect reports

