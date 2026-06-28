---
title: std::atomic_notify_all
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_notify_all
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++20|
template< class T >
void atomic_notify_all( std::atomic<T>* object );
dcl|num=2|since=c++20|
template< class T >
void atomic_notify_all( volatile std::atomic<T>* object );
```

Performs atomic notifying operations.
Unblocks all threads blocked in atomic waiting operations (i.e. `std::atomic_wait()`, `std::atomic_wait_explicit()`, or ) on `*object`, if there are any; otherwise does nothing.
Equivalent to `object->notify_all()`.

## Parameters


### Parameters

- `object` - pointer to the atomic object to notify

## Return value

(none)

## Notes

This form of change-detection is often more efficient than simple polling or pure spinlocks.

## Example

