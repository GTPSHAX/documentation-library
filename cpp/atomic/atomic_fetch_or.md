---
title: std::atomic_fetch_or_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_fetch_or
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
T atomic_fetch_or( std::atomic<T>* obj,
typename std::atomic<T>::value_type arg ) noexcept;
dcl|num=2|since=c++11|
template< class T >
T atomic_fetch_or( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type arg ) noexcept;
dcl|num=3|since=c++11|
template< class T >
T atomic_fetch_or_explicit( std::atomic<T>* obj,
typename std::atomic<T>::value_type arg,
std::memory_order order ) noexcept;
dcl|num=4|since=c++11|
template< class T >
T atomic_fetch_or_explicit( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type arg,
std::memory_order order ) noexcept;
```

Atomically replaces the value pointed by `obj` with the result of bitwise OR between the old value of `obj` and `arg`. Returns the value `obj` held previously.
The operation is performed as if the following is executed:
@1,2@ `obj->fetch_or(arg)`
@3,4@ `obj->fetch_or(arg, order)`
If `std::atomic<T>` has no `fetch_or` member (this member is only provided for `integral types` except `bool`), the program is ill-formed.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to modify
- `arg` - the value to bitwise OR to the value stored in the atomic object
- `order` - the memory synchronization ordering

## Return value

The value immediately preceding the effects of this function in the lsd|cpp/atomic/memory order#
Modification order of `*obj`.

## Example


## Defect reports


## See also


| cpp/atomic/atomic/dsc fetch_or | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_and | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_xor | (see dedicated page) |

