---
title: std::shared_lock::~shared_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/~shared_lock
---


```cpp
dcl|since=c++14|1=
~shared_lock();
```

Destroys the lock.
If `*this` has an associated mutex ((`mutex()` returns a non-null pointer) and has acquired ownership of it (`owns()` returns `true`), the mutex is unlocked by calling `std::shared_mutex::unlock_shared|unlock_shared()`.
