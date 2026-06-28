---
title: std::negative_binomial_distribution::negative_binomial_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/negative_binomial_distribution/negative_binomial_distribution
---


```cpp
dcl|num=1|since=c++11|1=
negative_binomial_distribution() : negative_binomial_distribution(1) {}
dcl|num=2|since=c++11|1=
explicit negative_binomial_distribution( IntType k, double p = 0.5 );
dcl|num=3|since=c++11|1=
explicit negative_binomial_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `k` and `p` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `k` - the ''k'' distribution parameter (number of trial successes)
- `p` - the ''p'' distribution parameter (probability of a trial generating `true`)
- `params` - the distribution parameter set

## Notes

Requires that $0 < p ≤ 1$ and $0 < k$.
If `1=p == 1`, subsequent calls to the `cpp/numeric/random/negative_binomial_distribution/operator()|operator()` overload that does not accept a `param_type` object will cause undefined behavior.
The default-constructed `std::negative_binomial_distribution` is equivalent to the default-constructed `std::geometric_distribution`.

## Defect reports

