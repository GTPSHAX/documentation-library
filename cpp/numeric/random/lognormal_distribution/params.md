---
title: std::lognormal_distribution::m
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/lognormal_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
RealType m() const;
dcl | since=c++11 | num=2 |
RealType s() const;
```

Returns the parameters the distribution was constructed with.
1. Returns the log-mean $m$ distribution parameter. It defines the location of the peak. The default value is `0.0`.
2. Returns the log-deviation $s$ distribution parameter. The default value is `1.0`.

## Parameters

(none)

## Return value

1. The log-mean $m$ distribution parameter.
2. The log-deviation $s$ distribution parameter.

## See also

