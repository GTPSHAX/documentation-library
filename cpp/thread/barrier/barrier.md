---
title: std::barrier::barrier
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/barrier/barrier
---


```cpp
dcl|num=1|since=c++20|1=
constexpr explicit barrier( std::ptrdiff_t expected,
CompletionFunction f = CompletionFunction());
dcl|num=2|since=c++20|1=
barrier( const barrier& ) = delete;
```

1. Sets the both initial expected count for each phase and the current expected count for the first phase to `expected`, initializes the completion function object with `std::move(f)`, and then starts the first phase. The behavior is undefined if `expected` is negative or greater than .
2. Copy constructor is deleted. `barrier` is neither copyable nor movable.

## Parameters


### Parameters

- `expected` - initial value of the expected count
- `f` - completion function object to be called on phase completion step

## Exceptions

1. Any exception thrown by `CompletionFunction`'s move constructor.

## Notes

`expected` is permitted to be zero. However, calling any non-static member function other than the destructor on such `barrier` results in undefined behavior. In other words, such `barrier` can only be destroyed.
