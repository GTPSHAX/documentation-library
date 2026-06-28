---
title: std::atomic_ref::exchange
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/exchange
---

ddcla|constexpr=c++26|1=
value_type exchange( value_type desired,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
Atomically replaces the value of the referenced object with `desired`. The operation is a read-modify-write operation. Memory is affected according to the value of `order`.
.

## Parameters


### Parameters

- `desired` - value to assign
- `order` - memory order constraints to enforce

## Return value

The value of the referenced object before the call.

## Defect reports

