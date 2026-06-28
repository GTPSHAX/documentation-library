---
title: std::coroutine_handle::promise
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/promise
---


```cpp
dcl|since=c++20|
Promise& promise() const;
dcl|since=c++20|
std::noop_coroutine_promise& promise() const noexcept;
```

Obtains a reference to the promise object.
The behavior is undefined if `*this` does not refer to a coroutine whose promise object has not been destroyed.
This function is not provided for the specialization `std::coroutine_handle<>`.

## Parameters

(none)

## Return value

A reference to the promise object.

## Notes

The promise object of a no-op coroutine is not destroyed as long as there is some `std::noop_coroutine_handle` referring to the coroutine.

## See also


| cpp/coroutine/coroutine_handle/dsc from_promise | (see dedicated page) |

