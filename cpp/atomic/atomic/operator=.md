---
title: std::atomic::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/operator=
---


```cpp
dcl|num=1|since=c++11|1=
T operator=( T desired ) noexcept;
dcl|num=2|since=c++11|1=
T operator=( T desired ) volatile noexcept;
dcl|num=3|since=c++11|1=
atomic& operator=( const atomic& ) = delete;
dcl|num=4|since=c++11|1=
atomic& operator=( const atomic& ) volatile = delete;
```

@1,2@ Atomically assigns `desired` to the atomic variable. Equivalent to `store(desired)`.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and overload  participates in overload resolution.
@3,4@ Atomic variables are not *CopyAssignable*.

## Parameters


### Parameters

- `desired` - value to assign

## Return value

@1,2@ `desired`

## Notes

Unlike most assignment operators, the assignment operators for atomic types do not return a reference to their left-hand arguments. They return a copy of the stored value instead.

## See also


| cpp/atomic/atomic/dsc constructor | (see dedicated page) |

