---
title: std::unique_lock::try_lock_for
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/try_lock_for
---


```cpp
dcl|since=c++11|1=
template< class Rep, class Period >
bool try_lock_for( const std::chrono::duration<Rep, Period>& timeout_duration );
```

Tries to lock (i.e., takes ownership of) the associated mutex. Blocks until specified `timeout_duration` has elapsed or the lock is acquired, whichever comes first. On successful lock acquisition returns `true`, otherwise returns `false`. Effectively calls `mutex()->try_lock_for(timeout_duration)`.
This function may block for longer than `timeout_duration` due to scheduling or resource contention delays.
The standard recommends that a steady clock is used to measure the duration. If an implementation uses a system clock instead, the wait time may also be sensitive to clock adjustments.
`std::system_error` is thrown if there is no associated mutex or if the mutex is already locked by this std::unique_lock.

## Parameters


### Parameters

- `timeout_duration` - maximum duration to block for

## Return value

`true` if the ownership of the mutex has been acquired successfully, `false` otherwise.

## Exceptions

* Any exceptions thrown by `mutex()->try_lock_for(timeout_duration)`.
* If there is no associated mutex, `std::system_error` with an error code of `std::errc::operation_not_permitted`.
* If the mutex is already locked, `std::system_error` with an error code of `std::errc::resource_deadlock_would_occur`.

## Example

