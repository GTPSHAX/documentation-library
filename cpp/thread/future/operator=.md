---
title: std::future::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future/operator=
---


```cpp
dcl|num=1|since=c++11|1=
future& operator=( future&& other ) noexcept;
dcl|num=2|since=c++11|1=
future& operator=( const future& other ) = delete;
```

Assigns the contents of another future object.
1. Releases any shared state and move-assigns the contents of `other` to `*this`. After the assignment, `other.valid()  and `this->valid()` will yield the same value as `other.valid()` before the assignment.
2. `std::future` is not *CopyAssignable*.

## Parameters


### Parameters

- `other` - a `std::future` that will transfer state to `*this`

## Return value

`*this`
