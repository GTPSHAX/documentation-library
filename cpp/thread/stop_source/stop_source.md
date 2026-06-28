---
title: std::stop_source::stop_source
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/stop_source
---


```cpp
dcl|since=c++20|num=1|
stop_source();
dcl|since=c++20|num=2|
explicit stop_source( std::nostopstate_t nss ) noexcept;
dcl|since=c++20|num=3|
stop_source( const stop_source& other ) noexcept;
dcl|since=c++20|num=4|
stop_source( stop_source&& other ) noexcept;
```

Constructs a new `stop_source` object.
1. Constructs a `stop_source` with new stop-state.
2. Constructs an empty `stop_source` with no associated stop-state.
3. Copy constructor. Constructs a `stop_source` whose associated stop-state is the same as that of `other`.
4. Move constructor. Constructs a `stop_source` whose associated stop-state is the same as that of `other`; `other` is left empty.

## Parameters


### Parameters

- `nss` - an `std::nostopstate_t` placeholder object to construct an empty `stop_source`
- `other` - another `stop_source` object to construct this `stop_source` object with

## Postconditions

1. `stop_possible()` is `true` and `stop_requested()` is `false`.
2. `stop_possible()` and `stop_requested()` are both `false`.
3. `*this` and `other` share the same associated stop-state and compare equal.
4. `*this` has `other`'s previously associated stop-state, and `other.stop_possible()` is `false`.

## Exceptions

1. `std::bad_alloc` if memory could not be allocated for the stop-state.
