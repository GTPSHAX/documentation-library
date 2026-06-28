---
title: std::scoped_lock::~scoped_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/scoped_lock/~scoped_lock
---

ddcl | since=c++17 |
~scoped_lock();
Releases the ownership of the owned mutexes.
Effectively calls `unlock()` on every mutex from the pack of mutexes passed to the `scoped_lock`'s constructor.
