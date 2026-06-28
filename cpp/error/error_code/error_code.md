---
title: std::error_code::error_code
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/error_code
---


```cpp
dcl|num=1|since=c++11|1=
error_code() noexcept;
dcl|num=2|since=c++11|1=
error_code( int ec, const error_category& ecat ) noexcept;
dcl|num=3|since=c++11|1=
template< class ErrorCodeEnum >
error_code( ErrorCodeEnum e ) noexcept;
|1=
error_code( const error_code& other ) = default;
|1=
error_code( error_code&& other ) = default;
```

Constructs new error code.
1. Constructs error code with default value. Equivalent to `error_code(0, std::system_category())`.
2. Constructs error code with `ec` as the platform-dependent error code and `ecat` as the corresponding error category.
3. Constructs error code from an error code enum `e`. Equivalent to `make_error_code(e)`, where `make_error_code` is only found by argument-dependent lookup. .
@4,5@ Implicitly defined copy constructor and move constructor. Initializes the error code with the contents of the `other`.

## Parameters


### Parameters

- `other` - another error code to initialize with
- `ec` - platform dependent error code to construct with
- `ecat` - error category corresponding to `ec`
- `e` - error code enum to construct with

## Defect reports


## See also


| cpp/error/errc/dsc make_error_code | (see dedicated page) |
| cpp/io/io_errc/dsc make_error_code | (see dedicated page) |
| cpp/thread/future_errc/dsc make_error_code | (see dedicated page) |

