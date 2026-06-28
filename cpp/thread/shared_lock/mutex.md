---
title: std::shared_lock::mutex
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/mutex
---


```cpp
dcl|since=c++14|1=
mutex_type* mutex() const noexcept;
```

Returns a pointer to the associated mutex, or a null pointer if there is no associated mutex.

## Parameters

(none)

## Return value

Pointer to the associated mutex or a null pointer if there is no associated mutex.

## Example

