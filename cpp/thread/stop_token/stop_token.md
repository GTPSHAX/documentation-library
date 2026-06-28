---
title: std::stop_token::stop_token
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_token/stop_token
---


```cpp
dcl|since=c++20|num=1|
stop_token() noexcept;
dcl|since=c++20|num=2|
stop_token( const stop_token& other ) noexcept;
dcl|since=c++20|num=3|
stop_token( stop_token&& other ) noexcept;
```

Constructs a new `stop_token` object.
1. Constructs an empty `stop_token` with no associated stop-state.
2. Copy constructor. Constructs a `stop_token` whose associated stop-state is the same as that of `other`.
3. Move constructor. Constructs a `stop_token` whose associated stop-state is the same as that of `other`; `other` is left empty.

## Parameters


### Parameters

- `other` - another `stop_token` object to construct this `stop_token` object with

## Postconditions

1. `stop_possible()` and `stop_requested()` are both `false`.
2. `*this` and `other` share the same associated stop-state and compare equal.
3. `*this` has `other`'s previously associated stop-state, and `other.stop_possible()` is `false`.
