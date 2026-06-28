---
title: std::atomic_ref::store
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/store
---

ddcla|constexpr=c++26|1=
void store( value_type desired,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
Atomically replaces the current value of the referenced object with `desired`. Memory is affected according to the value of `order`.
.
If `order` is not `std::memory_order_relaxed`, `std::memory_order_release` or `std::memory_order_seq_cst`, the behavior is undefined.

## Parameters


### Parameters

- `desired` - the value to store into the referenced object
- `order` - memory order constraints to enforce

## Defect reports


## See also


| cpp/atomic/atomic_ref/dsc operator{{= | (see dedicated page) |

