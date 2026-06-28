---
title: std::shared_future::shared_future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_future/shared_future
---


```cpp
dcl|num=1|since=c++11|
shared_future() noexcept;
dcl rev multi|num=2|since1=c++11|dcl1=
shared_future( const shared_future& other );
|since2=c++17|dcl2=
shared_future( const shared_future& other ) noexcept;
dcl|num=3|since=c++11|
shared_future( std::future<T>&& other ) noexcept;
dcl|num=4|since=c++11|
shared_future( shared_future&& other ) noexcept;
```

Constructs a new `shared_future`.
1. Default constructor. Constructs an empty shared future, that doesn't refer to a shared state, that is `1=valid() == false`.
2. Constructs a shared future that refers to the same shared state, if any, as `other`.
@3,4@ Transfers the shared state held by `other` to `*this`. After the construction, `1=other.valid() == false`, and `this->valid()` returns the same value as `other.valid()` would have returned before the construction.

## Parameters


### Parameters

- `other` - another future object to initialize with
