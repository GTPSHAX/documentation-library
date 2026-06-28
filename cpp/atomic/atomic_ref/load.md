---
title: std::atomic_ref::load
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/load
---

ddcla|constexpr=c++26|1=
value_type load( std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
Atomically loads and returns the current value of the referenced object. Memory is affected according to the value of `order`.
If `order` is not `std::memory_order_relaxed`, `std::memory_order_consume`, `std::memory_order_acquire` or `std::memory_order_seq_cst`, the behavior is undefined.

## Parameters


### Parameters

- `order` - memory order constraints to enforce

## Return value

The current value of the referenced object.

## See also


| cpp/atomic/atomic_ref/dsc operator T | (see dedicated page) |

