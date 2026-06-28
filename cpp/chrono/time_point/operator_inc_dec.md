---
title: std::chrono::time_point::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/operator_inc_dec
---


```cpp
dcl|since=c++20|num=1|
constexpr time_point& operator++();
dcl|since=c++20|num=2|
constexpr time_point operator++( int );
dcl|since=c++20|num=3|
constexpr time_point& operator--();
dcl|since=c++20|num=4|
constexpr time_point operator--( int );
```

Modifies the point in time `*this` represents by one tick of the `duration`.
If `d_` is a member variable holding the duration (i.e., time since epoch) of this `time_point` object,
1. Equivalent to `++d_; return *this;`.
2. Equivalent to `return time_point(d_++)`.
3. Equivalent to `--d_; return *this;`.
4. Equivalent to `return time_point(d_--);`.

## Parameters

(none)

## Return value

@1,3@ A reference to this `time_point` after modification.
@2,4@ A copy of the `time_point` made before modification.

## Example

