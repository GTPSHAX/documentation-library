---
title: std::error_condition::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/operator=
---


```cpp
dcl | num=1 | since=c++11 | 1=
template< class ErrorConditionEnum >
error_condition& operator=( ErrorConditionEnum e ) noexcept;
dcl | num=2 | since=c++11 | notes= | 1=
error_condition& operator=( const error_condition& other ) = default;
dcl | num=3 | since=c++11 | notes= | 1=
error_condition& operator=( error_condition&& other ) = default;
```

Assigns contents to an error condition.
1. Assigns error condition for enum `e`. Effectively calls `make_error_condition` that is only found by argument-dependent lookup for `e` and then replaces `*this` with the result. .
@2,3@ Implicitly defined copy-assignment operator and move-assignment operator assign the contents of `other` to `*this`.

## Parameters


### Parameters


## Return value

`*this`.

## Defect reports

