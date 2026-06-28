---
title: std::shared_future::get
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_future/get
---


```cpp
dcl|num=1|since=c++11|
const T& get() const;
dcl|num=2|since=c++11|
T& get() const;
dcl|num=3|since=c++11|
void get() const;
```

The `get` member function waits (by calling `wait()`) until the shared state is ready, then retrieves the value stored in the shared state (if any).
If `valid()` is `false` before the call to this function, the behavior is undefined.

## Return value

1. A const reference to the value stored in the shared state. The behavior of accessing the value through this reference after the shared state has been destroyed is undefined.
2. The reference stored as value in the shared state.
3. (none)

## Exceptions

If an exception was stored in the shared state referenced by the future (e.g. via a call to ) then that exception will be thrown.

## Notes

The C++ standard recommends the implementations to detect the case when `valid()` is `false` before the call and throw a `std::future_error` with an error condition of `std::future_errc::no_state`.

## Example

