---
title: std::atomic_flag_test_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag_test
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++20|
bool atomic_flag_test( const volatile std::atomic_flag* object ) noexcept;
dcl|num=2|since=c++20|
bool atomic_flag_test( const std::atomic_flag* object ) noexcept;
dcl|num=3|since=c++20|
bool atomic_flag_test_explicit( const volatile std::atomic_flag* object,
std::memory_order order ) noexcept;
dcl|num=4|since=c++20|
bool atomic_flag_test_explicit( const std::atomic_flag* object,
std::memory_order order ) noexcept;
```

Atomically reads the value of the `*object` and returns the value.
@1,2@ The memory synchronization order is `std::memory_order_seq_cst`.
@3,4@ The memory synchronization order is `order`.
@@ If `order` is one of `std::memory_order::release` and `std::memory_order::acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `object` - pointer to the `atomic_flag` object to read
- `order` - the memory synchronization ordering

## Return value

The value atomically read.

## Notes


## Example

