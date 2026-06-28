---
title: std::geometric_distribution::geometric_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/geometric_distribution/geometric_distribution
---


```cpp
dcl|num=1|since=c++11|1=
geometric_distribution() : geometric_distribution(0.5) {}
dcl|num=2|since=c++11|1=
explicit geometric_distribution( double p );
dcl|num=3|since=c++11|1=
explicit geometric_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `p` as the distribution parameter.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `p` - the ''p'' distribution parameter (probability of a trial generating `true`)
- `params` - the distribution parameter set

## Notes

Requires that $0 < p < 1$.

## Defect reports

