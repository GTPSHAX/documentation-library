---
title: std::discrete_distribution::discrete_distribution
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/discrete_distribution/discrete_distribution
---


```cpp
dcl|num=1|since=c++11|1=
discrete_distribution();
dcl|num=2|since=c++11|1=
template< class InputIt >
discrete_distribution( InputIt first, InputIt last );
dcl|num=3|since=c++11|1=
discrete_distribution( std::initializer_list<double> weights );
dcl|num=4|since=c++11|1=
template< class UnaryOperation >
discrete_distribution( std::size_t count, double xmin, double xmax,
UnaryOperation unary_op );
dcl|num=5|since=c++11|1=
explicit discrete_distribution( const param_type& params );
```

Constructs a new distribution object.
1. Default constructor. Constructs the distribution with a single weight $p }. This distribution will always generate `0`.
2. Constructs the distribution with weights in the range [first, last). If `first , the effects are the same as of the default constructor.
3. Constructs the distribution with weights in `weights`. Effectively calls `discrete_distribution(weights.begin(), weights.end())`.
4. Constructs the distribution with `count` weights that are generated using function `unary_op`. Each of the weights is equal to $w, where $δ  and $i ∈ {0, ..., count − 1$}. `xmin` and `xmax` must be such that $δ > 0$. If `count  the effects are the same as of the default constructor.
5. Constructs the distribution with `params` as the distribution parameters.

## Parameters


### Parameters

- `first, last` - the range of elements defining the numbers to use as weights. The type of the elements referred by `InputIterator` must be convertible to `double`
- `weights` - initializer list containing the weights
- `params` - the distribution parameter set

**Type requirements:**

- `InputIt`
