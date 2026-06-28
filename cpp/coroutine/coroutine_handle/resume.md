---
title: std::coroutine_handle::resume
type: Utilities
source: https://en.cppreference.com/w/cpp/coroutine/coroutine_handle/resume
---


```cpp
dcl|num=1|since=c++20|
void operator()() const;
void resume() const;
dcl|num=2|since=c++20|
constexpr void operator()() const noexcept;
constexpr void resume() const noexcept;
```

1. Resumes the execution of the coroutine to which `*this` refers, or does nothing if the coroutine is a no-op coroutine.
2. Does nothing.
The behavior is undefined if `*this` does not refer to suspended coroutine, or the coroutine is not a no-op coroutine and suspended at its final suspend point. A concurrent resumption of the coroutine may result in a data race.
Resumption of a coroutine on an execution agent other than the one on which it was suspended has implementation-defined behavior unless each execution agent either is a thread represented by `std::thread` or `std::jthread`, or is the thread executing `main`.

## Parameters

(none)

## Return value

(none)

## Exceptions

If an exception is thrown from the execution of the coroutine, the exception is caught and `unhandled_exception` is called on the coroutine's promise object. If the call to `unhandled_exception` throws or rethrows an exception, that exception is propagated.

## Notes

A coroutine that is resumed on a different execution agent should avoid relying on consistent thread identity throughout, such as holding a mutex object across a suspend point.

## Example

