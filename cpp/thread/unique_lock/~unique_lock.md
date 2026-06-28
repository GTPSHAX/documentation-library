---
title: std::unique_lock::~unique_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/~unique_lock
---


```cpp
dcl|since=c++11|1=
~unique_lock();
```

Destroys the lock. If `*this` has an associated mutex and has acquired ownership of it, the mutex is unlocked.
