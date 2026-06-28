---
title: std::coroutine_handle::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/operator=
---


```cpp
dcl|num=1|since=c++20|1=
coroutine_handle& operator=( std::nullptr_t ) noexcept;
dcl|num=2|since=c++20|1=
coroutine_handle& operator=( const coroutine_handle& other ) = default;
dcl|num=3|since=c++20|1=
coroutine_handle& operator=( coroutine_handle&& other ) = default;
```

Replaces the underlying address.
1. Replaces the underlying address with a null pointer value. After assignment, `*this` does not refer to a coroutine. This assignment operator is not declared for specialization `std::coroutine_handle<std::noop_coroutine_promise>`.
@2,3@ Replaces the underlying address with the one of `other`. Copy and move assignment operators are equivalent to implicitly declared ones.

## Parameters


### Parameters

- `other` - another `coroutine_handle` to assign from

## Return value

`*this`
