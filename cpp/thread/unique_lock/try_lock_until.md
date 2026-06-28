---
title: std::unique_lock::try_lock_until
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/try_lock_until
---


```cpp
dcl|since=c++11|1=
template< class Clock, class Duration >
bool try_lock_until( const std::chrono::time_point<Clock, Duration>& timeout_time );
```

Tries to lock (i.e., takes ownership of) the associated mutex. Blocks until specified `timeout_time` has been reached or the lock is acquired, whichever comes first. On successful lock acquisition returns `true`, otherwise returns `false`. May block for longer than `timeout_time` until has been reached.
Effectively calls `mutex()->try_lock_until(timeout_time)`.
`std::system_error` is thrown if there is no associated mutex or if the mutex is already locked by the same thread.
`Clock` must meet the *Clock* requirements. <sup>(since C++20)</sup> The program is ill-formed if `std::chrono::is_clock_v<Clock>` is `false`.

## Parameters


### Parameters

- `timeout_time` - maximum time point to block until

## Return value

`true` if the ownership of the mutex has been acquired successfully, `false` otherwise.

## Exceptions

* Any exceptions thrown by `mutex()->try_lock_until(timeout_time)`.
* If there is no associated mutex, `std::system_error` with an error code of `std::errc::operation_not_permitted`.
* If the mutex is already locked, `std::system_error` with an error code of `std::errc::resource_deadlock_would_occur`.

## Example

