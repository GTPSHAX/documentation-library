---
title: std::condition_variable_any::wait_for
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable_any/wait_for
---


```cpp
dcl|num=1|since=c++11|
template< class Lock, class Rep, class Period >
std::cv_status wait_for( Lock& lock,
const std::chrono::duration<Rep, Period>& rel_time );
dcl|num=2|since=c++11|
template< class Lock, class Rep, class Period, class Predicate >
bool wait_for( Lock& lock, const std::chrono::duration<Rep, Period>& rel_time,
Predicate pred );
dcl|num=3|since=c++20|
template< class Lock, class Rep, class Period, class Predicate >
bool wait_for( Lock& lock, std::stop_token stoken,
const std::chrono::duration<Rep, Period>& rel_time,
Predicate pred );
```

`wait_for` causes the current thread to block until the condition variable is notified, the given duration has been elapsed, or a spurious wakeup occurs. `pred` can be optionally provided to detect spurious wakeup.
1. Equivalent to `return wait_until(lock, std::chrono::steady_clock::now() + rel_time);`.
@2,3@ Waiting for a specific condition to become true, can be used to ignore spurious awakenings.
:@2@ Equivalent to `return wait_until(lock, std::chrono::steady_clock::now() + rel_time, std::move(pred));`.
:@3@ Registers `*this` for the duration of this call, to be notified if a stop request is made on `stoken`'s associated stop-state; it is then equivalent to .
Right after `wait_for` returns, `lock` is locked by the calling thread. If this postcondition cannot be satisfied, calls `std::terminate`.

## Parameters


### Parameters

- `lock` - an lock which must be locked by the calling thread
- `stoken` - a stop token to register interruption for
- `rel_time` - the maximum duration to wait
- `pred` - the predicate to check whether the waiting can be completed

**Type requirements:**

- `Lock`
- `Predicate`

## Return value

1. `std::cv_status::timeout` if `rel_time` has been elapsed since the beginning of this call, otherwise `std::cv_status::no_timeout`.
@2,3@ The latest result of `pred()` before returning to the caller.

## Exceptions

1. Timeout-related exceptions.
@2,3@ Timeout-related exceptions, and any exception thrown by `pred`.

## Notes

Even if notified under lock, overload  makes no guarantees about the state of the associated predicate when returning due to timeout.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2093 | C++11 | timeout-related exceptions were missing in the specification | mentions these exceptions |


## See also


| cpp/thread/condition_variable/dsc wait|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable_any | (see dedicated page) |

