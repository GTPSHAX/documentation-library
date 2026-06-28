---
title: std::packaged_task::get_future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/get_future
---

ddcl | since=c++11 |
std::future<R> get_future();
Returns a `future` which shares the same shared state as `*this`.
`get_future` can be called only once for each `packaged_task`.

## Parameters

(none)

## Return value

A future which shares the same shared state as `*this`.

## Exceptions

`std::future_error` on the following error conditions:
* The shared state has already been retrieved via a call to `get_future`. The error category is set to `cpp/thread/future_errc|future_already_retrieved`.
* `*this` has no shared state. The error category is set to `cpp/thread/future_errc|no_state`.
