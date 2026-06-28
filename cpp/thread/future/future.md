---
title: std::future::future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future/future
---


```cpp
dcl|num=1|since=c++11|
future() noexcept;
dcl|num=2|since=c++11|
future( future&& other ) noexcept;
dcl|num=3|since=c++11|
future( const future& other )  delete;
```

Constructs a `std::future` object.
1. Default constructor. Constructs a `std::future` with no shared state. After construction, `valid()` `.
2. Move constructor. Constructs a `std::future` with the shared state of `other` using move semantics. After construction, `other.valid() .
3. `std::future` is not *CopyConstructible*.

## Parameters


### Parameters

- `other` - another `std::future` to acquire shared state from
