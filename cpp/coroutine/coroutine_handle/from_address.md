---
title: std::coroutine_handle::from_address
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/from_address
---

ddcl|since=c++20|
static constexpr coroutine_handle from_address( void *addr );
Creates a `coroutine_handle` from a null pointer value or an underlying address of another `coroutine_handle`. The underlying address of return value is `addr`.
The behavior is undefined if `addr` is neither a null pointer value nor an underlying address of a `coroutine_handle`. The behavior is also undefined if the `addr` is an underlying address of a `std::coroutine_handle<P1>`, where both `Promise` and `P1` are not `void`, and `P1` is different from `Promise`.
This function is not declared for specialization `std::coroutine_handle<std::noop_coroutine_promise>`.

## Parameters


### Parameters

- `addr` - underlying address to import

## Return value

A `std::coroutine_handle<Promise>` whose underlying address is `addr`.

## Notes

If `addr` is not a null pointer value, it must be obtained from a prior call to `address()` on a `coroutine_handle` referring to some coroutine.

## Example

