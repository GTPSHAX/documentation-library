---
title: std::atomic_ref::fetch_and
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/fetch_and
---


```cpp
dcl|since=c++20|1=
value_type fetch_and( value_type arg,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
```

Atomically replaces the current value of the referenced object with the result of bitwise AND of the value and `arg`. This operation is a read-modify-write operation. Memory is affected according to the value of `order`.
.

## Parameters


### Parameters

- `arg` - the other argument of bitwise AND
- `order` - memory order constraints to enforce

## Return value

The value of the referenced object, immediately preceding the effects of this function.

## Example

