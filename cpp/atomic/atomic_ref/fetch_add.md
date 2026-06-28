---
title: std::atomic_ref::fetch_add
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/fetch_add
---


```cpp
dcla|constexpr=c++26|1=
value_type fetch_add( difference_type arg,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
```

Atomically replaces the current value referenced by  with the result of arithmetic addition of the value and `arg`. This operation is a read-modify-write operation. Memory is affected according to the value of `order`.
* For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
* For floating-point types, the floating-point environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding `std::numeric_limits` traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior.
* For pointer types, the result may be an undefined address, but the operation otherwise has no undefined behavior.
** If `std::remove_pointer_t<T>` is not a complete object type, the program is ill-formed.
.

## Parameters


### Parameters

- `arg` - the other argument of arithmetic addition
- `order` - memory order constraints to enforce

## Return value

The value referenced by , immediately preceding the effects of this function.

## Example

