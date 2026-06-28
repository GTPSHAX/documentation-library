---
title: std::poisson_distribution::poisson_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/poisson_distribution/poisson_distribution
---


```cpp
dcl|num=1|since=c++11|
poisson_distribution() : poisson_distribution(1.0) {}
dcl|num=2|since=c++11|
explicit poisson_distribution( double mean );
dcl|num=3|since=c++11|
explicit poisson_distribution( const param_type& params );
```

Constructs a new distribution object.
1. Uses `1.0` as the distribution parameter.
2. Uses `mean` as the distribution parameter.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `mean` - the ''μ'' distribution parameter (the mean of the distribution)
- `params` - the distribution parameter set

## Notes

Requires that `0 < mean`.

## Defect reports

