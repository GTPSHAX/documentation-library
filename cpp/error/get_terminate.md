---
title: std::get_terminate
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/get_terminate
---

ddcl|header=exception|since=c++11|
std::terminate_handler get_terminate() noexcept;
Returns the currently installed `std::terminate_handler`, which may be a null pointer.
This function is thread-safe. Prior call to `std::set_terminate` ''synchronizes-with'' (see `std::memory_order`) this function.

## Parameters

(none)

## Return value

The currently installed `std::terminate_handler`.

## Example

