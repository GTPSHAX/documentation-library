---
title: std::unique_lock::mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/mutex
---


```cpp
dcl|since=c++11|1=
mutex_type* mutex() const noexcept;
```

Returns a pointer to the associated mutex, or a null pointer if there is no associated mutex.

## Parameters

(none)

## Return value

Pointer to the associated mutex or a null pointer if there is no associated mutex.

## Example

