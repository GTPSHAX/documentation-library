---
title: std::atomic_ref::is_always_lock_free
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref/is_always_lock_free
---


```cpp
dcl|since=c++20|
static constexpr bool is_always_lock_free  /*implementation-defined*/;
```

Equals `true` if the operations on this `atomic_ref` type is always lock-free and `false` if it is never or sometimes lock-free.
The value of this constant is consistent with the result of member function `is_lock_free`.

## See also


| cpp/atomic/atomic_ref/dsc is_lock_free | (see dedicated page) |

