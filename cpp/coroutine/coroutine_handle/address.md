---
title: std::coroutine_handle::address
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/address
---

ddcl|since=c++20|
constexpr void* address() const noexcept;
Returns the underlying address of the `coroutine_handle`. The return value is non-null if and only if the current value of the `coroutine_handle` is obtained from a promise object of a coroutine.

## Parameters

(none)

## Return value

The underlying address.

## Notes

The return value is non-null for specialization `std::noop_coroutine_handle`, because a `std::noop_coroutine_handle` cannot be created without referring to a no-op coroutine.

## See also


| cpp/coroutine/coroutine_handle/dsc from_address | (see dedicated page) |

