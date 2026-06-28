---
title: std::atomic_ref::fetch_xor
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/fetch_xor
---


```cpp
dcl|since=c++20|1=
value_type fetch_xor( value_type arg,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
```

Atomically replaces the current value of the referenced object with the result of bitwise XOR of the value and `arg`. This operation is a read-modify-write operation. Memory is affected according to the value of `order`.
.

## Parameters


### Parameters

- `arg` - the other argument of bitwise XOR
- `order` - memory order constraints to enforce

## Return value

The value of the referenced object, immediately preceding the effects of this function.

## Defect reports

