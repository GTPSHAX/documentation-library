---
title: std::atomic::operators
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/operator_arith2
---


```cpp
dcl|num=1|since=c++11|1=
T operator+=( T arg ) noexcept;
dcl|num=2|since=c++11|1=
T operator+=( T arg ) volatile noexcept;
dcl|num=3|since=c++11|1=
T operator-=( T arg ) noexcept;
dcl|num=4|since=c++11|1=
T operator-=( T arg ) volatile noexcept;
dcl|num=5|since=c++11|1=
T* operator+=( std::ptrdiff_t arg ) noexcept;
dcl|num=6|since=c++11|1=
T* operator+=( std::ptrdiff_t arg ) volatile noexcept;
dcl|num=7|since=c++11|1=
T* operator-=( std::ptrdiff_t arg ) noexcept;
dcl|num=8|since=c++11|1=
T* operator-=( std::ptrdiff_t arg ) volatile noexcept;
```

Atomically replaces the current value with the result of computation involving the previous value and `arg`. The operation is read-modify-write operation.
* `1=operator+=` performs atomic addition. Equivalent to `return fetch_add(arg) + arg;`.
* `1=operator-=` performs atomic subtraction. Equivalent to `return fetch_sub(arg) - arg;`.
@1-4@ For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
rrev|since=c++20|
For floating-point types, the floating-point environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding `std::numeric_limits` traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior.
@5-8@ The result may be an undefined address, but the operations otherwise have no undefined behavior.
@@ If `T` is not a complete object type, the program is ill-formed.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and any `volatile` overload participates in overload resolution.

## Parameters


### Parameters

- `arg` - the argument for the arithmetic operation

## Return value

The resulting value (that is, the result of applying the corresponding binary operator to the value immediately preceding the effects of the corresponding member function in the  of `*this`).

## Notes

Unlike most compound assignment operators, the compound assignment operators for atomic types do not return a reference to their left-hand arguments. They return a copy of the stored value instead.

## Defect reports


## See also


| cpp/atomic/atomic/dsc fetch_add | (see dedicated page) |
| cpp/atomic/atomic/dsc fetch_sub | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith3 | (see dedicated page) |

