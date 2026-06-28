---
title: std::atomic_ref::compare_exchange_weak
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/compare_exchange
---


```cpp
dcla|num=1|constexpr=c++26|
bool compare_exchange_weak
( value_type& expected, value_type desired,
std::memory_order success,
std::memory_order failure ) const noexcept;
dcla|num=2|constexpr=c++26|1=
bool compare_exchange_weak
( value_type& expected, value_type desired,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
dcla|num=3|constexpr=c++26|1=
bool compare_exchange_strong
( value_type& expected, value_type desired,
std::memory_order success,
std::memory_order failure ) const noexcept;
dcla|num=4|constexpr=c++26|1=
bool compare_exchange_strong
( value_type& expected, value_type desired,
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
```

Atomically compares the value representation of the referenced object with that of `expected`, and if those are bitwise-equal, replaces the former with `desired` (performs a read-modify-write operation). Otherwise, loads the actual value stored in the referenced object into `expected` (performs a load operation).
@1,3@ The memory models for the read-modify-write and load operations are `success` and `failure` respectively.
@2,4@ `order` is used for both read-modify-write and load operations, except that `std::memory_order_acquire` and `std::memory_order_relaxed` are used for the load operation if `order` is `std::memory_order_acq_rel` or `std::memory_order_release` respectively.
.
If `failure` is not `std::memory_order_relaxed`, `std::memory_order_consume`, `std::memory_order_acquire` or `std::memory_order_seq_cst`, the behavior is undefined.

## Parameters


### Parameters

- `expected` - reference to the value expected to be found in the object referenced by the `atomic_ref` object
- `desired` - the value to store in the referenced object if it is as expected
- `success` - the memory synchronization ordering for the read-modify-write operation if the comparison succeeds
- `failure` - the memory synchronization ordering for the load operation if the comparison fails
- `order` - the memory synchronization ordering for both operations

## Return value

`true` if the referenced object was successfully changed, `false` otherwise.

## Notes

The comparison and copying are bitwise (similar to `std::memcmp` and `std::memcpy`); no constructor, assignment operator, or comparison operator are used.
The weak forms  of the functions are allowed to fail spuriously, that is, act as if `1=*this != expected` even if they are equal. When a compare-and-exchange is in a loop, the weak version will yield better performance on some platforms.
When a weak compare-and-exchange would require a loop and a strong one would not, the strong one is preferable unless the object representation of `value_type` may include trap bits, or offers multiple object representations for the same value (e.g. floating-point NaN). In those cases, weak compare-and-exchange typically works because it quickly converges on some stable object representation.
For a union with bits that participate in the value representations of some members but not the others, compare-and-exchange might always fail because such padding bits have indeterminate values when they do not participate in the value representation of the active member.
Padding bits that never participate in an object's value representation are ignored.

## Defect reports


## Example

