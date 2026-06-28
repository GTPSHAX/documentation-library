---
title: std::atomic_flag_clear_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag_clear
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
void atomic_flag_clear( volatile std::atomic_flag* obj ) noexcept;
dcl|num=2|since=c++11|
void atomic_flag_clear( std::atomic_flag* obj ) noexcept;
dcl|num=3|since=c++11|
void atomic_flag_clear_explicit( volatile std::atomic_flag* obj,
std::memory_order order ) noexcept;
dcl|num=4|since=c++11|
void atomic_flag_clear_explicit( std::atomic_flag* obj,
std::memory_order order ) noexcept;
```

Atomically changes the state of the `std::atomic_flag` pointed to by `obj` to clear (`false`).
@1,2@ The memory synchronization ordering is `std::memory_order_seq_cst`.
@3,4@ The memory synchronization ordering is `order`.
@@ If `order` is one of `std::memory_order_consume`, `std::memory_order_acquire` and `std::memory_order_acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `obj` - pointer to `std::atomic_flag` to access
- `order` - the memory synchronization ordering

## Notes

`std::atomic_flag_clear` and `std::atomic_flag_clear_explicit` can be implemented as `obj->clear()` and `obj->clear(order)` respectively.

## Defect reports


## See also


| cpp/atomic/dsc atomic_flag | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_test_and_set | (see dedicated page) |
| cpp/atomic/dsc memory_order | (see dedicated page) |

