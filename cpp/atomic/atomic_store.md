---
title: std::atomic_store_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_store
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
void atomic_store( std::atomic<T>* obj,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=2|since=c++11|
template< class T >
void atomic_store( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=3|since=c++11|
template< class T >
void atomic_store_explicit( std::atomic<T>* obj,
typename std::atomic<T>::value_type desired,
std::memory_order order) noexcept;
dcl|num=4|since=c++11|
template< class T >
void atomic_store_explicit( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type desired,
std::memory_order order) noexcept;
```

@1,2@ Atomically replaces the value pointed to by `obj` with the value of `desired` as if by `obj->store(desired)`.
@3,4@ Atomically replaces the value pointed to by `obj` with the value of `desired` as if by `obj->store(desired, order)`.
@@ If `order` is one of `std::memory_order_consume`, `std::memory_order_acquire` and `std::memory_order_acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to modify
- `desired` - the value to store in the atomic object
- `order` - the memory synchronization ordering

## Return value

(none)

## Defect reports


## See also


| cpp/atomic/atomic/dsc store|mem=std::atomic<T> | (see dedicated page) |
| cpp/atomic/dsc atomic_load | (see dedicated page) |
| cpp/atomic/dsc memory_order | (see dedicated page) |
| cpp/memory/shared_ptr/atomic|notes=mark life|deprecated=c++20|removed=c++26|br=yes|title=std::atomic_store(std::shared_ptr) | |
| <br>std::atomic_store_explicit(std::shared_ptr)|specializes atomic operations for `std::shared_ptr` | |

