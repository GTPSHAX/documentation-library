---
title: std::normal_distribution::mean
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/normal_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
RealType mean() const;
dcl | since=c++11 | num=2 |
RealType stddev() const;
```

Returns the parameters the distribution was constructed with.
1. Returns the mean $μ$ distribution parameter. The mean specifies the location of the peak. The default value is `0.0`.
2. Returns the deviation $σ$ distribution parameter. The default value is `1.0`.

## Parameters

(none)

## Return value

1. The mean $μ$ distribution parameter.
2. The deviation $σ$ distribution parameter.

## See also

