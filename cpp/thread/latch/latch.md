---
title: std::latch::latch
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/latch/latch
---


```cpp
dcl|num=1|since=c++20|1=
constexpr explicit latch( std::ptrdiff_t expected );
dcl|num=2|since=c++20|1=
latch( const latch& ) = delete;
```

1. Constructs a `latch` and initializes its internal counter. The behavior is undefined if `expected` is negative or greater than `max()`.
2. Copy constructor is deleted. `latch` is neither copyable nor movable.

## Parameters


### Parameters

- `expected` - the initial value of the internal counter

## Exceptions

Throws nothing.
