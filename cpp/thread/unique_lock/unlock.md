---
title: std::unique_lock::unlock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/unlock
---


```cpp
dcl|since=c++11|1=
void unlock();
```

Unlocks (i.e., releases ownership of) the associated mutex.
`std::system_error` is thrown if there is no associated mutex or if the mutex is not locked.

## Parameters

(none)

## Return value

(none)

## Exceptions

If there is no associated mutex or the mutex is not locked, `std::system_error` with an error code of `std::errc::operation_not_permitted`.

## Example

