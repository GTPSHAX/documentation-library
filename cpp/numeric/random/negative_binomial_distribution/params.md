---
title: std::negative_binomial_distribution::p
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/negative_binomial_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
double p() const;
dcl | since=c++11 | num=2 |
IntType k() const;
```

Returns the parameters the distribution was constructed with.
1. Returns the $p$ distribution parameter. It defines the probability of a trial generating `true`. The default value is `0.5`.
2. Returns the $k$ distribution parameter. It defines the number of desired outcomes. The default value is `1`.

## Parameters

(none)

## Return value

1. The $p$ distribution parameter.
2. The $k$ distribution parameter.

## See also

