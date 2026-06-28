---
title: std::latch::try_wait
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/latch/try_wait
---


```cpp
dcl|since=c++20|
bool try_wait() const noexcept;
```

Returns `true` only if the internal counter has reached zero. This function may spuriously return `false` with very low probability even if the internal counter has reached zero.

## Parameters

(none)

## Return value

With very low probability `false`, otherwise `1=cnt == 0`, where `cnt` is the value of the internal counter.

## Notes

The reason why a spurious result is permitted is to allow implementations to use a memory order more relaxed than `std::memory_order_seq_cst`.
