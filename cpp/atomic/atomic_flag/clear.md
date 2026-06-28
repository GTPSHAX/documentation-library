---
title: std::atomic_flag::clear
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag/clear
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|1=
void clear( std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
dcl|num=2|since=c++11|1=
void clear( std::memory_order order =
std::memory_order_seq_cst ) noexcept;
```

Atomically changes the state of a `std::atomic_flag` to clear (`false`). Memory is affected according to the value of `order`.
If `order` is one of `std::memory_order_consume`, `std::memory_order_acquire` and `std::memory_order_acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `order` - the memory synchronization ordering

## Defect reports


## See also


| cpp/atomic/atomic_flag/dsc test_and_set | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_clear | (see dedicated page) |
| cpp/atomic/dsc memory_order | (see dedicated page) |

