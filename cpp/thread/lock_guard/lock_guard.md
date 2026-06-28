---
title: std::lock_guard::lock_guard
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/lock_guard/lock_guard
---


```cpp
dcl|num=1|since=c++11|
explicit lock_guard( mutex_type& m );
dcl|num=2|since=c++11|
lock_guard( mutex_type& m, std::adopt_lock_t t );
dcl|num=3|since=c++11|1=
lock_guard( const lock_guard& ) = delete;
```

Acquires ownership of the given mutex `m`.
1. Effectively calls `m.lock()`.
2. Acquires ownership of the mutex `m` without attempting to lock it. The behavior is undefined if the current thread does not hold a non-shared lock (i.e., a lock acquired by `lock`, `try_lock`, `try_lock_for`, or `try_lock_until`) on `m`.
3. Copy constructor is deleted.
The behavior is undefined if `m` is destroyed before the `lock_guard` object is.

## Parameters


### Parameters

- `m` - mutex to acquire ownership of
- `t` - tag parameter used to select non-locking version of the constructor

## Exceptions

1. Throws any exceptions thrown by `m.lock()`.
2. Throws nothing.
