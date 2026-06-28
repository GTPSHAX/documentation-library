---
title: std::shared_lock::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/operator=
---


```cpp
dcl|since=c++14|1=
shared_lock& operator=( shared_lock&& other ) noexcept;
```

Move assignment operator. Equivalent to }.
If `other` is the same object as `*this`, there is no effect.
Otherwise, if prior to this call `*this` has an associated mutex ((`mutex()` returns a non-null pointer) and has acquired ownership of it (`owns()` returns `true`), the mutex is unlocked by calling `std::shared_mutex::unlock_shared|unlock_shared()`. After this call, `other` has no associated mutex.

## Parameters


### Parameters

- `other` - another `shared_lock` to replace the state with

## Return value

`*this`

## Defect reports

