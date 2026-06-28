---
title: std::coroutine_handle::operator coroutine_handle<>
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/operator_coroutine_handle_void
---

ddcl|since=c++20|
constexpr operator coroutine_handle<>() const noexcept;
This conversion function converts a `std::coroutine_handle<Promise>` value to a `std::coroutine_handle<>` holding the same underlying address. It effectively erases the promise type.

## Parameters

(none)

## Return value

`std::coroutine_handle<>::from_address(address())`

## See also


| cpp/coroutine/coroutine_handle/dsc operator cmp | (see dedicated page) |

