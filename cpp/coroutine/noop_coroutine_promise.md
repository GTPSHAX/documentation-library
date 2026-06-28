---
title: std::noop_coroutine_promise
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/noop_coroutine_promise
---

ddcl|header=coroutine|since=c++20|
struct noop_coroutine_promise {};
`noop_coroutine_promise` is the promise type of no-op coroutines.
A no-op coroutine behaves as if it
* does nothing other than the control flow of a coroutine, and
* is suspended immediately after beginning and resumption, and
* has a coroutine state such that destroying the state is no-op, and
* never reaches its final suspended point if there is any `std::coroutine_handle` referring to it.
No-op coroutines can be started by `std::noop_coroutine`, and controlled by the coroutine handle it returns. The returned coroutine handle is of type `std::noop_coroutine_handle`, which is a synonym for `std::coroutine_handle<std::noop_coroutine_promise>`.
Some operations of a no-op coroutines are determined no-op at compile time through the type `std::noop_coroutine_handle`.

## Example

