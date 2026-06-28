---
title: std::atomic::store
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/store
---


```cpp
dcl|num=1|since=c++11|1=
void store( T desired, std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=2|since=c++11|1=
void store( T desired, std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
```

Atomically replaces the current value with `desired`. Memory is affected according to the value of `order`.
If `order` is one of `std::memory_order_consume`, `std::memory_order_acquire` and `std::memory_order_acq_rel`, the behavior is undefined.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and overload  participates in overload resolution.

## Parameters


### Parameters

- `desired` - the value to store into the atomic variable
- `order` - memory order constraints to enforce

## Return value

(none)

## See also


| cpp/atomic/atomic/dsc operator{{= | (see dedicated page) |
| cpp/atomic/dsc atomic_store | (see dedicated page) |

