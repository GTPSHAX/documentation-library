---
title: std::lock_guard::~lock_guard
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/lock_guard/~lock_guard
---

ddcl | since=c++11 |
~lock_guard();
Releases the ownership of the owned mutex.
Effectively calls `m.unlock()` where `m` is the mutex passed to the `lock_guard`'s constructor.
