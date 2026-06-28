---
title: std::binomial_distribution::p
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/binomial_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
double p() const;
dcl | since=c++11 | num=2 |
IntType t() const;
```

Returns the parameters the distribution was constructed with.
1. Returns the $p$ distribution parameter. It defines the probability of a trial generating `true`. The default value is `0.5`.
2. Returns the $t$ distribution parameter. It identifies the number of trials. The default value is `1`.

## Parameters

(none)

## Return value

1. The $p$ distribution parameter.
2. The $t$ distribution parameter.

## See also

