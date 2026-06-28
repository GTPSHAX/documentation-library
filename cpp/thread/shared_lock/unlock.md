---
title: std::shared_lock::unlock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/unlock
---


```cpp
dcl|since=c++14|1=
void unlock();
```

Unlocks the associated mutex from shared mode. Effectively calls `mutex()->unlock_shared()`.
`std::system_error` is thrown if there is no associated mutex or if the mutex is not locked.

## Parameters

(none)

## Return value

(none)

## Exceptions

* Any exceptions thrown by `mutex()->unlock_shared()`.
* If there is no associated mutex, `std::system_error` with an error code of `std::errc::operation_not_permitted`.

## Example

