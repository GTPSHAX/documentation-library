---
title: std::uniform_int_distribution::a
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/uniform_int_distribution/params
---


```cpp
dcl|since=c++11|num=1|
result_type a() const;
dcl|since=c++11|num=2|
result_type b() const;
```

Returns the parameters the distribution has been constructed with.
1. Returns the ''a'' distribution parameter. It defines the minimum possibly generated value. The default value is `0`.
2. Returns the ''b'' distribution parameter. It defines the maximum possibly generated value. The default value is `std::numeric_limits<IntType>::max()`.

## Parameters

(none)

## Return value

1. The ''a'' distribution parameter.
2. The ''b'' distribution parameter.

## See also


| cpp/numeric/random/distribution/dsc param|uniform_int_distribution | (see dedicated page) |

