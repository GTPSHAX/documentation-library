---
title: std::error_category::default_error_condition
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_category/default_error_condition
---

ddcl | since=c++11 | 1=
virtual std::error_condition default_error_condition( int val ) const noexcept;
Returns the error condition for the given error value.
Equivalent to `std::error_condition(val, *this)`.
Classes derived from `error_category` may override this function to map certain error values to a generic category. For example, `std::system_category` overrides this function to map the error values that match POSIX `errno` values to `std::generic_category`.

## Parameters


### Parameters


## Return value

The error condition for the given error code.
