---
title: std::condition_variable::wait
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable/wait
---


```cpp
dcl|num=1|since=c++11|
void wait( std::unique_lock<std::mutex>& lock );
dcl|num=2|since=c++11|
template< class Predicate >
void wait( std::unique_lock<std::mutex>& lock, Predicate pred );
```

`wait` causes the current thread to block until the condition variable is notified or a spurious wakeup occurs. `pred` can be optionally provided to detect spurious wakeup.
1. Atomically calls `lock.unlock()` and blocks on `*this`.
@@ The thread will be unblocked when `notify_all()` or `notify_one()` is executed. It may also be unblocked spuriously.
@@ When unblocked, calls `lock.lock()` (possibly blocking on the lock), then returns.
2. Equivalent to
@@ c multi|
while (!pred())|
wait(lock);
.
@@ This overload may be used to ignore spurious awakenings while waiting for a specific condition to become `true`.
Right after `wait` returns, `lock.owns_lock()` is `true`, and `lock.mutex()` is locked by the calling thread. If these postconditions cannot be satisfied, calls `std::terminate`.
If any of the following conditions is satisfied, the behavior is undefined:
* `lock.owns_lock()` is `false`.
* `lock.mutex()` is not locked by the calling thread.
* If some other threads are also waiting on `*this`, `lock.mutex()` is different from the mutex unlocked by the waiting functions (`wait`, `wait_for` and `wait_until`) called on `*this` by those threads.

## Parameters


### Parameters

- `lock` - an lock which must be locked by the calling thread
- `pred` - the predicate to check whether the waiting can be completed

**Type requirements:**

- `Predicate`

## Exceptions

1. Throws nothing.
2. Any exception thrown by `pred`.

## Notes


## Example


## Defect reports


## See also


| cpp/thread/condition_variable/dsc wait_for|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable | (see dedicated page) |


## External links

