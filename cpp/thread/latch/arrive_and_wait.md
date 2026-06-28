---
title: std::latch::arrive_and_wait
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/latch/arrive_and_wait
---


```cpp
dcl|since=c++20|1=
void arrive_and_wait( std::ptrdiff_t n = 1 );
```

Atomically decrements the internal counter by `n` and (if necessary) blocks the calling
thread until the counter reaches zero. Equivalent to `count_down(n); wait();`.
If `n` is greater than the value of the internal counter or is negative, the behavior is undefined.

## Parameters


### Parameters

- `n` - the value by which the internal counter is decreased

## Return value

(none)

## Exceptions

Throws `std::system_error` with an error code allowed for mutex types on error.
