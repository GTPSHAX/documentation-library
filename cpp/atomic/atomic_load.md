---
title: std::atomic_load_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_load
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
T atomic_load( const std::atomic<T>* obj ) noexcept;
dcl|num=2|since=c++11|
template< class T >
T atomic_load( const volatile std::atomic<T>* obj ) noexcept;
dcl|num=3|since=c++11|
template< class T >
T atomic_load_explicit( const std::atomic<T>* obj,
std::memory_order order ) noexcept;
dcl|num=4|since=c++11|
template< class T >
T atomic_load_explicit( const volatile std::atomic<T>* obj,
std::memory_order order ) noexcept;
```

@1,2@ Atomically obtains the value pointed to by `obj` as if by `obj->load()`.
@3,4@ Atomically obtains the value pointed to by `obj` as if by `obj->load(order)`.
@@ If order is one of `std::memory_order_release` and `std::memory_order_acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to modify
- `order` - the memory synchronization ordering for this operation

## Return value

The value that is held by the atomic object pointed to by `obj`.

## See also


| cpp/atomic/atomic/dsc load|mem=std::atomic<T> | (see dedicated page) |
| cpp/atomic/dsc atomic_store | (see dedicated page) |
| cpp/atomic/dsc memory_order | (see dedicated page) |
| cpp/memory/shared_ptr/atomic|title=std::atomic_loaddsc small|(std::shared_ptr) | |
| <br>std::atomic_load_explicit(std::shared_ptr)|specializes atomic operations for `std::shared_ptr`|notes= | |

