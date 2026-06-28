---
title: std::binomial_distribution::binomial_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/binomial_distribution/binomial_distribution
---


```cpp
dcl|num=1|since=c++11|1=
binomial_distribution() : binomial_distribution(1) {}
dcl|num=2|since=c++11|1=
explicit binomial_distribution( IntType t, double p = 0.5 );
dcl|num=3|since=c++11|1=
explicit binomial_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `t` and `p` as the distribution parameters.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `t` - the ''t'' distribution parameter (number of trials)
- `p` - the ''p'' distribution parameter (probability of a trial generating `true`)
- `params` - the distribution parameter set

## Notes

Requires that $0 ≤ p ≤ 1$ and $0 ≤ t$.

## Defect reports

