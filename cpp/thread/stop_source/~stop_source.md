---
title: std::stop_source::~stop_source
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/~stop_source
---

ddcl|since=c++20|
~stop_source();
Destroys the `stop_source` object.
If `*this` has associated stop-state, releases ownership of it.
