---
title: std::condition_variable::wait_until
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable/wait_until
---


```cpp
dcl|num=1|since=c++11|
template< class Clock, class Duration >
std::cv_status
wait_until( std::unique_lock<std::mutex>& lock,
const std::chrono::time_point<Clock, Duration>& abs_time );
dcl|num=2|since=c++11|
template< class Clock, class Duration, class Predicate >
bool wait_until( std::unique_lock<std::mutex>& lock,
const std::chrono::time_point<Clock, Duration>& abs_time,
Predicate pred );
```

`wait_until` causes the current thread to block until the condition variable is notified, the given time point has been reached, or a spurious wakeup occurs. `pred` can be optionally provided to detect spurious wakeup.
1. Atomically calls `lock.unlock()` and blocks on `*this`.
@@ The thread will be unblocked when `notify_all()` or `notify_one()` is executed, or `abs_time` is reached. It may also be unblocked spuriously.
@@ When unblocked, calls `lock.lock()` (possibly blocking on the lock), then returns.
2. Equivalent to .
@@ This overload may be used to ignore spurious awakenings while waiting for a specific condition to become true.
Right after `wait_until` returns, `lock.owns_lock()` is `true`, and `lock.mutex()` is locked by the calling thread. If these postconditions cannot be satisfied, calls `std::terminate`.
If any of the following conditions is satisfied, the behavior is undefined:
* `lock.owns_lock()` is `false`.
* `lock.mutex()` is not locked by the calling thread.
* If some other threads are also waiting on `*this`, `lock.mutex()` is different from the mutex unlocked by the waiting functions (`wait`, `wait_for` and `wait_until`) called on `*this` by those threads.

## Parameters


### Parameters

- `lock` - an lock which must be locked by the calling thread
- `abs_time` - the time point where waiting expires
- `pred` - the predicate to check whether the waiting can be completed

**Type requirements:**

- `Predicate`

## Return value

1. `std::cv_status::timeout` if `abs_time` has been reached, otherwise `std::cv_status::no_timeout`.
2. The latest result of `pred()` before returning to the caller.

## Exceptions

1. Timeout-related exceptions.
2. Timeout-related exceptions, and any exception thrown by `pred`.

## Notes


## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2093 | C++11 | timeout-related exceptions were missing in the specification | mentions these exceptions |


## See also


| cpp/thread/condition_variable/dsc wait|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_for|condition_variable | (see dedicated page) |

