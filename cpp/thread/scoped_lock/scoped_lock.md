---
title: std::scoped_lock::scoped_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/scoped_lock/scoped_lock
---


```cpp
dcl|num=1|since=c++17|
explicit scoped_lock( MutexTypes&... m );
dcl|num=2|since=c++17|
scoped_lock( std::adopt_lock_t, MutexTypes&... m );
dcl|num=3|since=c++17|1=
scoped_lock( const scoped_lock& ) = delete;
```

Acquires ownership of the given mutexes `m`.
1. If `1=sizeof...(MutexTypes) == 0`, does nothing. Otherwise, if `1=sizeof...(MutexTypes) == 1`, effectively calls `m.lock()`. Otherwise, effectively calls `std::lock(m...)`.
2. Acquires ownership of the mutexes `m...` without attempting to lock any of them. The behavior is undefined unless the current thread holds a non-shared lock (i.e., a lock acquired by `lock`, `try_lock`, `try_lock_for`, or `try_lock_until`) on each object in `m...`.
3. Copy constructor is deleted.
The behavior is undefined if `m` is destroyed before the `scoped_lock` object is.

## Parameters


### Parameters

- `m` - mutexes to acquire ownership of

## Exceptions

1. Throws any exceptions thrown by `m.lock()`.
2. Throws nothing.

## Defect reports

