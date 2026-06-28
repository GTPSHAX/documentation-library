---
title: std::generator::generator
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/generator/generator
---


```cpp
dcl|num=1|since=c++23|1=
generator( const generator& ) = delete;
dcl|num=2|since=c++23|
generator( generator&& other ) noexcept;
```

Constructs a `generator`.
1. The copy-constructor is deleted.
2. The move-constructor that initializes the underlying `''coroutine_''` with }, and the underlying stack of coroutine handles (`''active_''`) with `std::exchange(other.active_, nullptr)`.
Note, that the iterators, previously obtained from `other`, are not invalidated, but become iterators into `*this`.

## Parameters


### Parameters

- `other` - a generator object to be moved in

## Example

