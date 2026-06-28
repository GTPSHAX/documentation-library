---
title: std::atomic::fetch_sub
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/fetch_sub
---


```cpp
dcl|num=1|since=c++11|1=
T fetch_sub( T arg, std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=2|since=c++11|1=
T fetch_sub( T arg, std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
dcl|num=3|since=c++11|1=
T* fetch_sub( std::ptrdiff_t arg,
std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=4|since=c++11|1=
T* fetch_sub( std::ptrdiff_t arg,
std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
```

Atomically replaces the current value with the result of arithmetic subtraction of the value and `arg`. That is, it performs atomic post-decrement. The operation is read-modify-write operation. Memory is affected according to the value of `order`.
@1,2@ For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
rrev|since=c++20|
For floating-point types, the floating-point environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding `std::numeric_limits` traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior.
@3,4@ The result may be an undefined address, but the operation otherwise has no undefined behavior.
@@ If `T` is not a complete object type, the program is ill-formed.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and overload  or  participates in overload resolution.

## Parameters


### Parameters

- `arg` - the other argument of arithmetic subtraction
- `order` - memory order constraints to enforce

## Return value

The value immediately preceding the effects of this function in the  of `*this`.

## Defect reports


## See also


| cpp/atomic/dsc atomic_fetch_sub | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith | (see dedicated page) |

