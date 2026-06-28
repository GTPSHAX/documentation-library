---
title: std::get_unexpected
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/get_unexpected
---

ddcl|header=exception|deprecated=c++11|until=c++17|
std::unexpected_handler get_unexpected() noexcept;
Returns the currently installed `std::unexpected_handler`, which may be a null pointer.
rrev|since=c++11|
This function is thread-safe. Prior call to `std::set_unexpected` ''synchronizes-with'' (see `std::memory_order`) the subsequent calls to this function.

## Parameters

(none)

## Return value

The currently installed `std::unexpected_handler`.

## See also


| cpp/error/dsc unexpected_handler | (see dedicated page) |
| cpp/error/dsc set_unexpected | (see dedicated page) |

