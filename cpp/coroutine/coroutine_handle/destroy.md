---
title: std::coroutine_handle::destroy
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/destroy
---


```cpp
dcl|num=1|since=c++20|
void destroy() const;
dcl|num=2|since=c++20|
constexpr void destroy() const noexcept;
```

1. Destroys the coroutine state of the coroutine to which `*this` refers, or does nothing if the coroutine is a no-op coroutine.
2. Does nothing.
The behavior is undefined if destroying is needed and `*this` does not refer to a suspended coroutine.

## Parameters

(none)

## Return value

(none)

## Example

