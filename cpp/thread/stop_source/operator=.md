---
title: std::stop_source::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/operator=
---


```cpp
dcl|num=1|since=c++20|1=
std::stop_source& operator=( const std::stop_source& other ) noexcept;
dcl|num=2|since=c++20|1=
std::stop_source& operator=( std::stop_source&& other ) noexcept;
```

Replaces the stop-state with that of `other`.
1. Copy-assigns the stop-state of `other` to that of `*this`. Equivalent to `stop_source(other).swap(*this)`.
2. Move-assigns the stop-state of `other` to that of `*this`. After the assignment, `*this` contains the previous stop-state of `other`, and `other` has no stop-state. Equivalent to `stop_source(std::move(other)).swap(*this)`.

## Parameters


### Parameters

- `other` - another `stop_source` object to share the stop-state with to or acquire the stop-state from
