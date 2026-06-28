---
title: std::exponential_distribution::exponential_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/exponential_distribution/exponential_distribution
---


```cpp
dcl|num=1|since=c++11|1=
exponential_distribution() : exponential_distribution(1.0) {}
dcl|num=2|since=c++11|1=
explicit exponential_distribution( RealType lambda );
dcl|num=3|since=c++11|1=
explicit exponential_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `lambda` as the distribution parameter.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `lambda` - the ''λ'' distribution parameter (the rate parameter)
- `params` - the distribution parameter set

## Notes

Requires that $0 < lambda$.

## Defect reports

