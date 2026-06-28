---
title: std::atomic_wait_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_wait
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++20|
template< class T >
void atomic_wait( const std::atomic<T>* object,
typename std::atomic<T>::value_type old );
dcl|num=2|since=c++20|
template< class T >
void atomic_wait( const volatile std::atomic<T>* object,
typename std::atomic<T>::value_type old );
dcl|num=3|since=c++20|
template< class T >
void atomic_wait_explicit( const std::atomic<T>* object,
typename std::atomic<T>::value_type old,
std::memory_order order );
dcl|num=4|since=c++20|
template< class T >
void atomic_wait_explicit( const volatile std::atomic<T>* object,
typename std::atomic<T>::value_type old,
std::memory_order order );
```

Performs atomic waiting operations. Behaves as if it repeatedly performs the following steps:
* Compare the value representation of `object->load()` (for overloads ) or `object->load(order)` (for overloads ) with that of `old`.
** If those are bitwise equal, then blocks until `*object` is notified by `std::atomic::notify_one()` or `std::atomic::notify_all()`, or the thread is unblocked spuriously.
** Otherwise, returns.
These functions are guaranteed to return only if value has changed, even if the underlying implementation unblocks spuriously.
@1,2@ Equivalent to `object->wait(old)`.
@3,4@ Equivalent to `object->wait(old, order)`.
@@ If `order` is one of `std::memory_order::release` and `std::memory_order::acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `object` - pointer to the atomic object to check and wait on
- `old` - the value to check the atomic object no longer contains
- `order` - the memory synchronization ordering

## Return value

(none)

## Notes

This form of change-detection is often more efficient than simple polling or pure spinlocks.
Due to the [ABA problem](https://en.wikipedia.org/wiki/ABA problem), transient changes from `old` to another value and back to `old` might be missed, and not unblock.
The comparison is bitwise (similar to `std::memcmp`); no comparison operator is used. Padding bits that never participate in an object's value representation are ignored.

## Example

