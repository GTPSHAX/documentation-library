---
title: std::counting_semaphore::counting_semaphore
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/counting_semaphore/counting_semaphore
---


```cpp
dcl|num=1|since=c++20|
constexpr explicit counting_semaphore( std::ptrdiff_t desired );
dcl|num=2|since=c++20|1=
counting_semaphore( const counting_semaphore& ) = delete;
```

1. Constructs an object of type `std::counting_semaphore` with the internal counter initialized to `desired`.
2. Copy constructor is deleted.

## Preconditions

1. Both `1=desired >= 0` and `1=desired <= max()` are `true`.

## Parameters


### Parameters

- `desired` - the value to initialize `counting_semaphore`'s counter with

## Exceptions

Throws nothing.
