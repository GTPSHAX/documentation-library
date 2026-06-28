---
title: std::uniform_real_distribution::uniform_real_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/uniform_real_distribution/uniform_real_distribution
---


```cpp
dcl|num=1|since=c++11|1=
uniform_real_distribution() : uniform_real_distribution(0.0) { }
dcl|num=2|since=c++11|1=
explicit uniform_real_distribution( RealType a, RealType b = 1.0 );
dcl|num=3|since=c++11|1=
explicit uniform_real_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `a` and `b` as the distribution parameters.
3. Uses `params` as the distribution parameters.

## Parameters


### Parameters

- `a` - the ''a'' distribution parameter (minimum value)
- `b` - the ''b'' distribution parameter (maximum value)
- `params` - the distribution parameter set

## Notes

Requires that `a ≤ b` and ` b - a ≤ std::numeric_limits<RealType>::max()`.
If `1=a == b`, subsequent calls to the `cpp/numeric/random/uniform_real_distribution/operator()|operator()` overload that does not accept a `param_type` object will cause undefined behavior.
To create a distribution over the closed interval $[a,b]$, `std::nextafter(b, std::numeric_limits<RealType>::max())` may be used as the second parameter.

## Defect reports

