---
title: std::promise::promise
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/promise/promise
---


```cpp
dcl|num=1|since=c++11|
promise();
dcl|num=2|since=c++11|
template< class Alloc >
promise( std::allocator_arg_t, const Alloc& alloc );
dcl|num=3|since=c++11|
promise( promise&& other ) noexcept;
dcl|num=4|since=c++11|1=
promise( const promise& other ) = delete;
```

Constructs a `promise` object.
1. Default constructor. Constructs the promise with an empty shared state.
2. Constructs the promise with an empty shared state. The shared state is allocated using `alloc`. `Alloc` must meet the requirements of *Allocator*.
3. Move constructor. Constructs the promise with the shared state of `other` using move semantics. After construction, `other` has no shared state.
4. `promise` is not copyable.

## Parameters


### Parameters

- `alloc` - allocator to use to allocate the shared state
- `other` - another `promise` to acquire the state from

## Exceptions

@1,2@

## Example

