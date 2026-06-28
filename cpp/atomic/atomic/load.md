---
title: std::atomic::load
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/load
---


```cpp
dcl|num=1|since=c++11|1=
T load( std::memory_order order
= std::memory_order_seq_cst ) const noexcept;
dcl|num=2|since=c++11|1=
T load( std::memory_order order
= std::memory_order_seq_cst ) const volatile noexcept;
```

Atomically loads and returns the current value of the atomic variable. Memory is affected according to the value of `order`.
If `order` is one of `std::memory_order_release` and `std::memory_order_acq_rel`, the behavior is undefined.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and overload  participates in overload resolution.

## Parameters


### Parameters

- `order` - memory order constraints to enforce

## Return value

The current value of the atomic variable.

## See also


| cpp/atomic/atomic/dsc operator T | (see dedicated page) |
| cpp/atomic/dsc atomic_load | (see dedicated page) |

