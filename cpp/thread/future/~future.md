---
title: std::future::~future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future/~future
---

ddcl|since=c++11|
~future();
Releases any shared state. This means:
* If the current object holds the last reference to its shared state, the shared state is destroyed.
* The current object gives up its reference to its shared state.
rrev|since=c++14|
* These actions will not block for the shared state to become ready, except that they may block if all following conditions are satisfied:
** The shared state was created by a call to `std::async`.
** The shared state is not yet ready.
** The current object was the last reference to the shared state.
