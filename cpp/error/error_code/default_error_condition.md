---
title: std::error_code::default_error_condition
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/default_error_condition
---

ddcl|since=c++11|
std::error_condition default_error_condition() const noexcept;
Returns the default error condition for the current error value.
Equivalent to `category().default_error_condition(value())`.

## Parameters

(none)

## Return value

The default error condition for the current error value.
