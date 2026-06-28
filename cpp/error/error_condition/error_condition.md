---
title: std::error_condition::error_condition
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/error_condition
---


```cpp
dcl|num=1|since=c++11|
error_condition() noexcept;
dcl|num=2|since=c++11|
error_condition( int val, const error_category& cat ) noexcept;
dcl|num=3|since=c++11|
template< class ErrorConditionEnum >
error_condition( ErrorConditionEnum e ) noexcept;
|1=
error_condition( const error_condition& other ) = default;
|1=
error_condition( error_condition&& other ) = default;
```

Constructs new error condition.
1. Default constructor. Initializes the error condition with generic category and error value `0`.
2. Initializes the error condition with error value `val` and error category `cat`.
3. Initializes the error condition with enum `e`. Effectively calls `make_error_condition` that is only found by argument-dependent lookup for `e`. .
@4,5@ Implicitly defined copy constructor and move constructor. Initializes the error condition with the contents of the `other`.

## Parameters


### Parameters

- `other` - another error condition to initialize with
- `val` - error value
- `cat` - error category
- `e` - error condition enum

## Defect reports


## See also


| cpp/error/errc/dsc make_error_condition | (see dedicated page) |
| cpp/io/io_errc/dsc make_error_condition | (see dedicated page) |
| cpp/thread/future_errc/dsc make_error_condition | (see dedicated page) |

