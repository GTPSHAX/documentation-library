---
title: std::atomic_fetch_xor_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_fetch_xor
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
T atomic_fetch_xor( std::atomic<T>* obj,
typename std::atomic<T>::value_type arg ) noexcept;
dcl|num=2|since=c++11|
template< class T >
T atomic_fetch_xor( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type arg ) noexcept;
dcl|num=3|since=c++11|
template< class T >
T atomic_fetch_xor_explicit( std::atomic<T>* obj,
typename std::atomic<T>::value_type arg,
std::memory_order order) noexcept;
dcl|num=4|since=c++11|
template< class T >
T atomic_fetch_xor_explicit( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type arg,
std::memory_order order) noexcept;
```

Atomically replaces the value pointed by `obj` with the result of bitwise XOR between the old value of `obj` and `arg`. Returns the value `obj` held previously.
The operation is performed as if the following is executed:
@1,2@ `obj->fetch_xor(arg)`
@3,4@ `obj->fetch_xor(arg, order)`
If `std::atomic<T>` has no `fetch_xor` member (this member is only provided for `integral types` except `bool`), the program is ill-formed.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to modify
- `arg` - the value to bitwise XOR to the value stored in the atomic object
- `order` - the memory synchronization ordering

## Return value

The value immediately preceding the effects of this function in the  of `*obj`.

## Example


## See also


| cpp/atomic/atomic/dsc fetch_xor|mem=std::atomic<T> | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_or | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_and | (see dedicated page) |

