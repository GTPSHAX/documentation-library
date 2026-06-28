---
title: std::condition_variable_any::wait
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/condition_variable_any/wait
---


```cpp
dcl|num=1|since=c++11|
template< class Lock >
void wait( Lock& lock );
dcl|num=2|since=c++11|
template< class Lock, class Predicate >
void wait( Lock& lock, Predicate pred );
dcl|num=3|since=c++20|
template< class Lock, class Predicate >
bool wait( Lock& lock, std::stop_token stoken, Predicate pred );
```

`wait` causes the current thread to block until the condition variable is notified or a spurious wakeup occurs. `pred` can be optionally provided to detect spurious wakeup.
1. Atomically calls `lock.unlock()` and blocks on `*this`.
@@ The thread will be unblocked when `notify_all()` or `notify_one()` is executed. It may also be unblocked spuriously.
@@ When unblocked, calls `lock.lock()` (possibly blocking on the lock), then returns.
@2,3@ Waiting for a specific condition to become true, can be used to ignore spurious awakenings.
:@2@ Equivalent to
:@@ c multi
|while (!pred())
|    wait(lock);
:@3@ Registers `*this` for the duration of this call, to be notified if a stop request is made on `stoken`'s associated stop-state; it is then equivalent to
:@@ c multi
|while (!stoken.stop_requested())
|{
|    if (pred())
|        return true;
|    wait(lock);
|}
|return pred();
Right after `wait` returns, `lock` is locked by the calling thread. If this postcondition cannot be satisfied, calls `std::terminate`.

## Parameters


### Parameters

- `lock` - an lock which must be locked by the calling thread
- `stoken` - a stop token to register interruption for
- `pred` - the predicate to check whether the waiting can be completed

**Type requirements:**

- `Lock`
- `Predicate`

## Return value

@1,2@ (none)
3. The latest result of `pred()` before returning to the caller.

## Exceptions

1. Does not throw.
@2,3@ Any exception thrown by `pred`.

## Notes

The returned value of overload  indicates whether `pred` evaluated to `true`, regardless of whether there was a stop requested or not.

## Example


## Defect reports


## See also


| cpp/thread/condition_variable/dsc wait_for|condition_variable_any | (see dedicated page) |
| cpp/thread/condition_variable/dsc wait_until|condition_variable_any | (see dedicated page) |


## External links

