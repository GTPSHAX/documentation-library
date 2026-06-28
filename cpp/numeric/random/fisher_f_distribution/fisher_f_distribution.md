---
title: std::fisher_f_distribution::fisher_f_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/fisher_f_distribution/fisher_f_distribution
---


```cpp
dcl|num=1|since=c++11|1=
fisher_f_distribution() : fisher_f_distribution(1.0) {}
dcl|num=2|since=c++11|1=
explicit fisher_f_distribution( RealType m, RealType n = 1.0 );
dcl|num=3|since=c++11|1=
explicit fisher_f_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `m` and `n` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `m` - the ''m'' distribution parameter (degrees of freedom)
- `n` - the ''n'' distribution parameter (degrees of freedom)
- `params` - the distribution parameter set

## Defect reports

