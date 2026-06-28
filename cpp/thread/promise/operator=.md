---
title: std::promise::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/promise/operator=
---


```cpp
dcl|num=1|since=c++11|1=
promise& operator=( promise&& other ) noexcept;
dcl|num=2|since=c++11|1=
promise& operator=( const promise& rhs ) = delete;
```

Assigns the contents.
1. Move assignment operator. First, abandons the shared state (as in `~promise()`), then assigns the shared state of `other` as if by executing `std::promise(std::move(other)).swap(*this)`.
2. `promise` is not copy-assignable.

## Parameters


### Parameters

- `other` - another `promise` to acquire the state from

## Return value

`*this`
