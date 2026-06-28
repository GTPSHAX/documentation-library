---
title: std::latch::wait
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/latch/wait
---


```cpp
dcl|since=c++20|
void wait() const;
```

Blocks the calling thread until the internal counter reaches `0`. If it is zero already, returns immediately.

## Parameters

(none)

## Return value

(none)

## Exceptions

Throws `std::system_error` with an error code allowed for mutex types on error.
