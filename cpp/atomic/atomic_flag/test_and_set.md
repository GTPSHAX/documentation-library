---
title: std::atomic_flag::test_and_set
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag/test_and_set
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|1=
bool test_and_set( std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
dcl|num=2|since=c++11|1=
bool test_and_set( std::memory_order order =
std::memory_order_seq_cst ) noexcept;
```

Atomically changes the state of a `std::atomic_flag` to set (`true`) and returns the value it held before. This operation is a read-modify-write operation. Memory is affected according to the value of `order`.

## Parameters


### Parameters

- `order` - the memory synchronization order

## See also


| cpp/atomic/atomic_flag/dsc clear | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_test_and_set | (see dedicated page) |
| cpp/atomic/dsc memory_order | (see dedicated page) |

