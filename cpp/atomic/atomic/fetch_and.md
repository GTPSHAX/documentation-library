---
title: std::atomic::fetch_and
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/fetch_and
---


```cpp
dcl|num=1|since=c++11|1=
T fetch_and( T arg, std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=2|since=c++11|1=
T fetch_and( T arg, std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
```

Atomically replaces the current value with the result of bitwise AND of the value and `arg`. The operation is read-modify-write operation. Memory is affected according to the value of `order`.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and overload  participates in overload resolution.

## Parameters


### Parameters

- `arg` - the other argument of bitwise AND
- `order` - memory order constraints to enforce

## Return value

The value immediately preceding the effects of this function in the  of `*this`.

## See also


| cpp/atomic/dsc atomic_fetch_and | (see dedicated page) |

