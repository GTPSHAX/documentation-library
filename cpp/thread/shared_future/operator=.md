---
title: std::shared_future::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_future/operator=
---


```cpp
dcl rev multi|num=1|since1=c++11|dcl1=
shared_future& operator=( const shared_future& other );
|since2=c++17|dcl2=
shared_future& operator=( const shared_future& other ) noexcept;
dcl|num=2|since=c++11|1=
shared_future& operator=( shared_future&& other ) noexcept;
```

Assigns the contents of another `shared_future`.
1. Releases any shared state and assigns the contents of `other` to `*this`. After the assignment, `this->valid() .
2. Releases any shared state and move-assigns the contents of `other` to `*this`. After the assignment, `other.valid()  and `valid|this->valid()` will yield the same value as `other.valid()` before the assignment.

## Parameters


### Parameters

- `other` - a `std::shared_future` that will transfer state to `*this`

## Return value

`*this`
