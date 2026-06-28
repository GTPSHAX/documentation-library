---
title: std::shared_lock::owns_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/owns_lock
---


```cpp
dcl|since=c++14|1=
bool owns_lock() const noexcept;
```

Checks whether `*this` owns a locked mutex or not.

## Parameters

(none)

## Return value

`true` if `*this` has an associated mutex and has acquired shared ownership of it, `false` otherwise.

## See also


| cpp/thread/shared_lock/dsc operator_bool | (see dedicated page) |

