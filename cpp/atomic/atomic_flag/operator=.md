---
title: std::atomic_flag::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag/operator=
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|1=
atomic_flag& operator=( const atomic_flag& ) = delete;
dcl|num=2|since=c++11|1=
atomic_flag& operator=( const atomic_flag& ) volatile = delete;
```

`std::atomic_flag` is not assignable, its assignment operators are deleted.
