---
title: std::future_category
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_category
---

ddcl | header=future | since=c++11 |
const std::error_category& future_category() noexcept;
Obtains a reference to the static error category object for the errors related to futures and promises. The object is required to override the virtual function `error_category::name()` to return a pointer to the string `"future"`. It is used to identify error codes provided in the exceptions of type `std::future_error`.

## Parameters

(none)

## Return value

A reference to the static object of unspecified runtime type, derived from `std::error_category`.

## Example


## See also

