---
title: std::atomic_flag_notify_one
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag_notify_one
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++20|
void atomic_flag_notify_one( std::atomic_flag* object ) noexcept;
dcl|num=2|since=c++20|
void atomic_flag_notify_one( volatile std::atomic_flag* object ) noexcept;
```

Performs atomic notifying operations.
If there is a thread blocked in an atomic waiting operation (i.e. `std::atomic_flag_wait()`, `std::atomic_flag_wait_explicit()`, or ) on `*object`, then unblocks ''at least'' one such thread; otherwise does nothing.
Equivalent to `object->notify_one()`.

## Parameters


### Parameters

- `object` - pointer to the `atomic_flag` object to notify

## Return value

(none)

## Notes

This form of change-detection is often more efficient than simple polling or pure spinlocks.

## Example

