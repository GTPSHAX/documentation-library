---
title: std::uniform_int_distribution::uniform_int_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/uniform_int_distribution/uniform_int_distribution
---


```cpp
dcl|num=1|since=c++11|1=
uniform_int_distribution() : uniform_int_distribution(0) { }
dcl|num=2|since=c++11|1=
explicit uniform_int_distribution( IntType a,
IntType b = std::numeric_limits<IntType>::max() );
dcl|num=3|since=c++11|1=
explicit uniform_int_distribution( const param_type& params );
```

Constructs new distribution object.
2. Uses `a` and `b` as the distribution parameters.
3. Uses `params` as the distribution parameters.
The behavior is undefined if `a > b`.

## Parameters


### Parameters

- `a` - the ''a'' distribution parameter (minimum value)
- `b` - the ''b'' distribution parameter (maximum value)
- `params` - the distribution parameter set

## Defect reports

