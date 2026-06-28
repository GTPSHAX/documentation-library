---
title: std::stop_token::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_token/operator=
---


```cpp
dcl|num=1|since=c++20|1=
std::stop_token& operator=( const std::stop_token& other ) noexcept;
dcl|num=2|since=c++20|1=
std::stop_token& operator=( std::stop_token&& other ) noexcept;
```

Replaces the associated stop-state with that of `other`.
1. Copy-assigns the associated stop-state of `other` to that of `*this`. Equivalent to `stop_token(other).swap(*this)`.
2. Move-assigns the associated stop-state of `other` to that of `*this`. After the assignment, `*this` contains the previous associated stop-state of `other`, and `other` has no associated stop-state. Equivalent to `stop_token(std::move(other)).swap(*this)`.

## Parameters


### Parameters

- `other` - another `stop_token` object to share the stop-state with to or acquire the stop-state from
