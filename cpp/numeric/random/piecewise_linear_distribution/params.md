---
title: densities
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/random/piecewise_linear_distribution/params
---


```cpp
dcl | since=c++11 | num=1 |
std::vector<RealType> intervals() const;
dcl | since=c++11 | num=2 |
std::vector<RealType> densities() const;
```

Returns the distribution parameters.
1. Returns the list of boundaries of the intervals.
2. Returns the list of probability densities at the boundaries of the intervals.

## Parameters

(none)

## Return value

The distribution parameters:
1. The list of boundaries of the intervals.
2. The list of probability densities at the boundaries of the intervals.

## Complexity

Linear in the number of intervals in this object.
