---
title: std::shared_lock::release
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/release
---


```cpp
dcl|since=c++14|1=
mutex_type* release() noexcept;
```

Breaks the association of the associated mutex, if any, and `*this`.
No locks are unlocked. If the `*this` held ownership of the associated mutex prior to the call, the caller is now responsible to unlock the mutex.

## Parameters

(none)

## Return value

Pointer to the associated mutex or a null pointer if there was no associated mutex.

## Example

