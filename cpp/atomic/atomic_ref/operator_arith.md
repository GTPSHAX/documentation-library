---
title: std::atomic_ref::operators (int)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/operator_arith
---


```cpp
dcl|num=1|since=c++20|1=
value_type operator++() const noexcept;
dcl|num=2|since=c++20|1=
value_type operator++( int ) const noexcept;
dcl|num=3|since=c++20|1=
value_type operator--() const noexcept;
dcl|num=4|since=c++20|1=
value_type operator--( int ) const noexcept;
```

Atomically increments or decrements the current value of the referenced object. These operations are read-modify-write operations.
1. Performs atomic pre-increment. Equivalent to `return fetch_add(1) + 1;`.
2. Performs atomic post-increment. Equivalent to `return fetch_add(1);`.
3. Performs atomic pre-decrement. Equivalent to `return fetch_sub(1) - 1;`
4. Performs atomic post-decrement. Equivalent to `return fetch_sub(1);`.
* For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
* For pointer-to-object types, the result may be an undefined address, but the operations otherwise have no undefined behavior. The program is ill-formed if `std::remove_pointer_t<T>` is not a complete object type.
.

## Return value

@1,3@ The value of the referenced object after the modification.
@2,4@ The value of the referenced object before the modification.

## Notes

Unlike most pre-increment and pre-decrement operators, the pre-increment and pre-decrement operators for `atomic_ref` do not return a reference to the modified object. They return a copy of the stored value instead.

## Defect reports


## See also


| cpp/atomic/atomic_ref/dsc fetch_add | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc fetch_sub | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith2 | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith3 | (see dedicated page) |

