---
title: std::error_code::message
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/message
---

ddcl|since=c++11|
std::string message() const;
Returns the message corresponding to the current error code value and category.
Equivalent to `category().message(value())`.

## Parameters

(none)

## Return value

The error message corresponding to the current error code value and category.
