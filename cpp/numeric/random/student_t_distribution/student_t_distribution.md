---
title: std::student_t_distribution::student_t_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/student_t_distribution/student_t_distribution
---


```cpp
dcl|num=1|since=c++11|1=
student_t_distribution() : student_t_distribution(1) {}
dcl|num=2|since=c++11|1=
explicit student_t_distribution( RealType n );
dcl|num=3|since=c++11|1=
explicit student_t_distribution( const param_type& params );
```

Constructs a new distribution object.
2. Uses `n` as the distribution parameter.
3. Uses `params` as the distribution parameter.

## Parameters


### Parameters

- `n` - the ''n'' distribution parameter (degrees of freedom)
- `params` - the distribution parameter set

## Defect reports

