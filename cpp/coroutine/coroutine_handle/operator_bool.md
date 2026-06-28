---
title: std::coroutine_handle::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/operator_bool
---

ddcl|since=c++20|
constexpr explicit operator bool() const noexcept;
Checks whether `*this` is non-null, i.e. the value of `*this` is obtained from the promise object of some coroutine. Equivalent to `return bool(address());`.
If `Promise` is `std::noop_coroutine_promise`, this conversion function always returns `true`.

## Parameters

(none)

## Return value

`bool(address())`, or `true` if `Promise` is `std::noop_coroutine_promise`.

## See also


| cpp/coroutine/coroutine_handle/dsc address | (see dedicated page) |

