---
title: std::bernoulli_distribution::bernoulli_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/bernoulli_distribution/bernoulli_distribution
---


```cpp
dcl|num=1|since=c++11|1=
bernoulli_distribution() : bernoulli_distribution(0.5) { }
dcl|num=2|since=c++11|1=
explicit bernoulli_distribution( double p );
dcl|num=3|since=c++11|1=
explicit bernoulli_distribution( const param_type& params );
```

Constructs new distribution object.
2. Uses `p` as the distribution parameter.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `p` - the ''p'' distribution parameter (probability of generating `true`)
- `params` - the distribution parameter set

## Defect reports

