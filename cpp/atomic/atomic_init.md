---
title: std::atomic_init
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_init
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|deprecated=c++20|
template< class T >
void atomic_init
( std::atomic<T>* obj,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=2|since=c++11|deprecated=c++20|
template< class T >
void atomic_init
( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type desired ) noexcept;
```

Initializes the default-constructed atomic object `obj` with the value `desired`. The function is not atomic: concurrent access from another thread, even through an atomic operation, is a data race.
If `obj` was not default-constructed, or this function is called twice on the same `obj`, the behavior is undefined.

## Parameters


### Parameters

- `obj` - pointer to an atomic object to initialize
- `desired` - the value to initialize atomic object with

## Return value

(none)

## Notes

This function is provided for compatibility with C. If the compatibility is not required, `std::atomic` may be initialized through their non-default constructors.

## Example


## See also


| cpp/atomic/dsc ATOMIC_VAR_INIT | (see dedicated page) |
| cpp/atomic/atomic/dsc constructor | (see dedicated page) |

