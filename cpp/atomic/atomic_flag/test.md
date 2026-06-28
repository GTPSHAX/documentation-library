---
title: std::atomic_flag::test
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag/test
---


```cpp
dcl|num=1|since=c++20|1=
bool test( std::memory_order order =
std::memory_order_seq_cst ) const volatile noexcept;
dcl|num=2|since=c++20|1=
bool test( std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
```

Atomically reads the value of the `*this` and returns the value.
If `order` is one of `std::memory_order_release` and `std::memory_order_acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `order` - the memory synchronization ordering

## Return value

The value atomically read.

## Example

