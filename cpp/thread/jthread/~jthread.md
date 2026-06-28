---
title: std::jthread::~jthread
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/jthread/~jthread
---

ddcl|since=c++20|
~jthread();
Destroys the `jthread` object.
If `*this` has an associated thread (`1=joinable() == true`), calls `request_stop()` and then `join()`.

## Notes

The `request_stop()` has no effect if the `jthread` was previously requested to stop.
A `jthread` object does not have an associated thread after
* it was default-constructed.
* it was moved from.
* `join()` has been called.
* `detach()` has been called.
If `join()` throws an exception (e.g. because deadlock is detected), `std::terminate()` may be called.

## Example

