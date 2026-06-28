---
title: std::atomic_notify_one
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_notify_one
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++20|
template< class T >
void atomic_notify_one( std::atomic<T>* object );
dcl|num=2|since=c++20|
template< class T >
void atomic_notify_one( volatile std::atomic<T>* object );
```

Performs atomic notifying operations.
If there is a thread blocked in atomic waiting operation (i.e. `std::atomic_wait()`, `std::atomic_wait_explicit()`, or ) on `*object`, then unblocks ''at least'' one such thread; otherwise does nothing.
Equivalent to `object->notify_one()`.

## Parameters


### Parameters

- `object` - pointer to the atomic object to notify

## Return value

(none)

## Notes

This form of change-detection is often more efficient than simple polling or pure spinlocks.

## Example

