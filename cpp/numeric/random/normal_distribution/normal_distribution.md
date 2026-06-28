---
title: std::normal_distribution::normal_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/normal_distribution/normal_distribution
---


```cpp
dcl|num=1|since=c++11|1=
normal_distribution() : normal_distribution(0.0) {}
dcl|num=2|since=c++11|1=
explicit normal_distribution( RealType mean, RealType stddev = 1.0 );
dcl|num=3|since=c++11|1=
explicit normal_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `mean` and `stddev` as the distribution parameters.
3. Uses `params` as the distribution parameters.
The behavior is undefined if `stddev` is not greater than zero.

## Parameters


### Parameters

- `mean` - the ''μ'' distribution parameter (mean)
- `stddev` - the ''σ'' distribution parameter (standard deviation)
- `params` - the distribution parameter set

## Defect reports

