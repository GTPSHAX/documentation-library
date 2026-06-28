---
title: std::condition_variable_any::wait_until
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable_any/wait_until
---


```cpp
dcl|num=1|since=c++11|
template< class Lock, class Clock, class Duration >
std::cv_status
wait_until( Lock& lock,
const std::chrono::time_point<Clock, Duration>& abs_time );
dcl|num=2|since=c++11|
template< class Lock, class Clock, class Duration, class Predicate >
bool wait_until( Lock& lock,
const std::chrono::time_point<Clock, Duration>& abs_time,
Predicate pred );
dcl|num=3|since=c++20|
template< class Lock, class Clock, class Duration, class Predicate >
bool wait_until( Lock& lock, std::stop_token stoken,
const std::chrono::time_point<Clock, Duration>& abs_time,
Predicate pred );
```

`wait_until` causes the current thread to block until the condition variable is notified, the given duration has been elapsed, or a spurious wakeup occurs. `pred` can be optionally provided to detect spurious wakeup.
1. Atomically calls `lock.unlock()` and blocks on `*this`.
@@ The thread will be unblocked when `notify_all()` or `notify_one()` is executed, or `abs_time` is reached. It may also be unblocked spuriously.
@@ When unblocked, calls `lock.lock()` (possibly blocking on the lock), then returns.
@2,3@ Waiting for a specific condition to become true, can be used to ignore spurious awakenings.
:@2@ Equivalent to .
:@3@ Registers `*this` for the duration of this call, to be notified if a stop request is made on `stoken`'s associated stop-state; it is then equivalent to c multi|while (!stoken.stop_requested())
|{
|    if (pred())
|        return true;
|    if (wait_until(lock, abs_time)  std::cv_status::timeout)
|        return pred();
|}
|return pred();.
Right after `wait_until` returns, `lock` is locked by the calling thread. If this postcondition cannot be satisfied, calls `std::terminate`.

## Parameters


### Parameters

- `lock` - an lock which must be locked by the calling thread
- `stoken` - a stop token to register interruption for
- `abs_time` - the time point where waiting expires
- `pred` - the predicate to check whether the waiting can be completed

**Type requirements:**

- `Lock`
- `Predicate`

## Return value

1. `std::cv_status::timeout` if `abs_time` has been reached, otherwise `std::cv_status::no_timeout`.
@2,3@ The latest result of `pred()` before returning to the caller.

## Exceptions

1. Timeout-related exceptions.
@2,3@ Timeout-related exceptions, and any exception thrown by `pred`.

## Notes


## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2093 | C++11 | timeout-related exceptions were missing in the specification | mentions these exceptions |


## See also


| cpp/thread/condition_variable/dsc wait|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable_any | (see dedicated page) |

