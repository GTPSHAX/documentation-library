---
title: std::condition_variable::wait_for
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable/wait_for
---


```cpp
dcl|num=1|since=c++11|
template< class Rep, class Period >
std::cv_status wait_for( std::unique_lock<std::mutex>& lock,
const std::chrono::duration<Rep, Period>& rel_time );
dcl|num=2|since=c++11|
template< class Rep, class Period, class Predicate >
bool wait_for( std::unique_lock<std::mutex>& lock,
const std::chrono::duration<Rep, Period>& rel_time,
Predicate pred );
```

`wait_for` causes the current thread to block until the condition variable is notified, the given duration has been elapsed, or a spurious wakeup occurs. `pred` can be optionally provided to detect spurious wakeup.
1. Equivalent to `return wait_until(lock, std::chrono::steady_clock::now() + rel_time);`.
2. Equivalent to `return wait_until(lock, std::chrono::steady_clock::now() + rel_time, std::move(pred));`.
@@ This overload may be used to ignore spurious awakenings while waiting for a specific condition to become true.
Right after `wait_for` returns, `lock.owns_lock()` is `true`, and `lock.mutex()` is locked by the calling thread. If these postconditions cannot be satisfied, calls `std::terminate`.
If any of the following conditions is satisfied, the behavior is undefined:
* `lock.owns_lock()` is `false`.
* `lock.mutex()` is not locked by the calling thread.
* If some other threads are also waiting on `*this`, `lock.mutex()` is different from the mutex unlocked by the waiting functions (`wait`, `wait_for` and `wait_until`) called on `*this` by those threads.

## Parameters


### Parameters

- `lock` - a lock which must be locked by the calling thread
- `rel_time` - the maximum duration to wait
- `pred` - the predicate to check whether the waiting can be completed

**Type requirements:**

- `Predicate`

## Return value

1. `std::cv_status::timeout` if `rel_time` has been elapsed since the beginning of this call, otherwise `std::cv_status::no_timeout`.
2. The latest result of `pred()` before returning to the caller.

## Exceptions

1. Timeout-related exceptions.
2. Timeout-related exceptions, and any exception thrown by `pred`.

## Notes

Even if notified under lock, overload  makes no guarantees about the state of the associated predicate when returning due to timeout.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2093 | C++11 | timeout-related exceptions were missing in the specification | mentions these exceptions |


## See also


| cpp/thread/condition_variable/dsc wait|condition_variable | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable | (see dedicated page) |

