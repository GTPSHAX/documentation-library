---
title: std::weibull_distribution::a
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/weibull_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
RealType a() const;
dcl | since=c++11 | num=2 |
RealType b() const;
```

Returns the parameters the distribution was constructed with.
1. Returns the $a$ parameter. It defines the shape of the distribution. The default value is `1.0`.
2. Returns the $b$ parameter. It defines the scale of the distribution. The default value is `1.0`.

## Parameters

(none)

## Return value

1. The value of the $a$ parameter.
2. The value of the $b$ parameter.

## Complexity

Constant.

## See also

