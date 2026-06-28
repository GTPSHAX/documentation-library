---
title: std::atomic_ref::operators
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/operator_arith2
---


```cpp
dcla|num=1|constexpr=c++26|1=
value_type operator+=( difference_type arg ) const noexcept;
dcla|num=2|constexpr=c++26|1=
value_type operator-=( difference_type arg ) const noexcept;
```

Atomically replaces the current value referenced by  with the result of computation involving the previous value and `arg`. These operations are read-modify-write operations.
1. `1=operator+=` performs atomic addition. Equivalent to `return fetch_add(arg) + arg;`.
2. `1=operator-=` performs atomic subtraction. Equivalent to `return fetch_sub(arg) - arg;`.
* For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
* For floating-point types, the floating-point environment in effect may be different from the calling thread's floating-point environment. The operation need not be conform to the corresponding `std::numeric_limits` traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior.
* For pointer types, the result may be an undefined address, but the operation otherwise has no undefined behavior.
** If `std::remove_pointer_t<T>` is not a complete object type, the program is ill-formed.
.

## Parameters


### Parameters

- `arg` - the argument for the arithmetic operation

## Return value

The resulting value (that is, the result of applying the corresponding binary operator to the value referenced by  immediately preceding the effects of the corresponding member function).

## Notes

Unlike most compound assignment operators, the compound assignment operators for `atomic_ref` return a copy of the stored value instead of a reference to `arg`.

## Example


## See also


| cpp/atomic/atomic_ref/dsc fetch_add | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc fetch_sub | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith3 | (see dedicated page) |

