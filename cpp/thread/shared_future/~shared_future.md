---
title: std::shared_future::~shared_future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_future/~shared_future
---

ddcl|since=c++11|
~shared_future();
If `*this` is the last object referring to the shared state, destroys the shared state. Otherwise does nothing.
