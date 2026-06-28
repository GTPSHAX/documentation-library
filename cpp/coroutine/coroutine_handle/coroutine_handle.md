---
title: std::coroutine_handle::coroutine_handle
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/coroutine_handle
---


```cpp
dcl|num=1|since=c++20|
constexpr coroutine_handle() noexcept;
dcl|num=2|since=c++20|
constexpr coroutine_handle( std::nullptr_t ) noexcept;
dcl|num=3|since=c++20|1=
coroutine_handle( const coroutine_handle& other ) = default;
dcl|num=4|since=c++20|1=
coroutine_handle( coroutine_handle&& other ) = default;
```

Creates a `coroutine_handle` that does not refer a coroutine, or copies a `coroutine_handle`.
@1,2@ Initializes the underlying address  to `nullptr`. After construction,  returns `nullptr`, and the `coroutine_handle` does not refer a coroutine. These constructors are not declared for the specialization `std::coroutine_handle<std::noop_coroutine_promise>`.
@3,4@ Copies the underlying address. The copy constructor and move constructor are equivalent to implicitly declared ones.

## Parameters


### Parameters

- `other` - another `coroutine_handle` to copy

## Notes

`std::coroutine_handle<std::noop_coroutine_promise>` is neither default constructible nor constructible from `std::nullptr_t`. `std::noop_coroutine` can be used to create a new `std::coroutine_handle<std::noop_coroutine_promise>`.
Static member functions `from_promise` and `from_address` can also create a `coroutine_handle`.

## See also


| cpp/coroutine/coroutine_handle/dsc from_promise | (see dedicated page) |
| cpp/coroutine/coroutine_handle/dsc from_address | (see dedicated page) |
| cpp/coroutine/dsc noop_coroutine | (see dedicated page) |

