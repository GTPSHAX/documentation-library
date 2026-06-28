---
title: std::atomic_flag_notify_all
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag_notify_all
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++20|
void atomic_flag_notify_all( std::atomic_flag* object ) noexcept;
dcl|num=2|since=c++20|
void atomic_flag_notify_all( volatile std::atomic_flag* object ) noexcept;
```

Performs atomic notifying operations.
Unblocks all threads blocked in atomic waiting operations (i.e. `std::atomic_flag_wait()`, `std::atomic_flag_wait_explicit()`, or ) on `*object`, if there are any; otherwise does nothing.
Equivalent to `object->notify_all()`.

## Parameters


### Parameters

- `object` - pointer to the `atomic_flag` object to notify

## Return value

(none)

## Notes

This form of change-detection is often more efficient than simple polling or pure spinlocks.

## Example

