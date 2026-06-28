---
title: std::unique_lock::operator bool
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/operator_bool
---


```cpp
dcl|since=c++11|1=
explicit operator bool() const noexcept;
```

Checks whether `*this` owns a locked mutex or not. Effectively calls `owns_lock()`.

## Parameters

(none)

## Return value

`true` if `*this` has an associated mutex and has acquired ownership of it, `false` otherwise.

## See also


| cpp/thread/unique_lock/dsc owns_lock | (see dedicated page) |

