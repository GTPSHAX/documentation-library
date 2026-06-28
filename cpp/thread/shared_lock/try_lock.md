---
title: std::shared_lock::try_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/try_lock
---


```cpp
dcl|since=c++14|1=
bool try_lock();
```

Tries to lock the associated mutex in shared mode without blocking. Effectively calls `mutex()->try_lock_shared()`.
`std::system_error` is thrown if there is no associated mutex or if the mutex is already locked.

## Parameters

(none)

## Return value

`true` if the ownership of the mutex has been acquired successfully, `false` otherwise.

## Exceptions

* Any exceptions thrown by `mutex()->try_lock_shared()`.
* If there is no associated mutex, `std::system_error` with an error code of `std::errc::operation_not_permitted`.
* If the mutex is already locked, `std::system_error` with an error code of `std::errc::resource_deadlock_would_occur`.

## Example

