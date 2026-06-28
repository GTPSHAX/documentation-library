---
title: std::error_code::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/operator=
---


```cpp
dcl|num=1|since=c++11|1=
template< class ErrorCodeEnum >
error_code& operator=( ErrorCodeEnum e ) noexcept;
|1=
error_code& operator=( const error_code& other ) = default;
|1=
error_code& operator=( error_code&& other ) = default;
```

1. Replaces the error code and corresponding category with those representing error code enum `e`.
Equivalent to `1=*this = make_error_code(e)`, where `make_error_code` is only found by argument-dependent lookup.
.
@2,3@ Implicitly defined copy-assignment operator and move-assignment operator assign the contents of `other` to `*this`.

## Parameters


### Parameters

- `e` - error code enum to construct
- `other` - another error code to assign with

## Return value

`*this`

## Defect reports


## See also


| cpp/error/error_code/dsc assign | (see dedicated page) |

