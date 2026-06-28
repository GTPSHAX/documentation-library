---
title: std::fisher_f_distribution::m
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/fisher_f_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
RealType m() const;
dcl | since=c++11 | num=2 |
RealType n() const;
```

Returns the parameters the distribution was constructed with.
1. Returns the $m$ (the first degree of freedom) distribution parameter. The default value is `1.0`.
2. Returns the $n$ (the second degree of freedom) distribution parameter. The default value is `1.0`.

## Parameters

(none)

## Return value

1. The $m$ (the first degree of freedom) distribution parameter.
2. The $n$ (the second degree of freedom) distribution parameter.

## Complexity

Constant.

## See also

