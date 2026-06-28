---
title: std::stop_token::~stop_token
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_token/~stop_token
---

ddcl|since=c++20|
~stop_token();
Destroys the `stop_token` object.
If `*this` has associated stop-state, releases ownership of it.
