---
title: std::counting_semaphore::try_acquire
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/counting_semaphore/try_acquire
---


```cpp
dcl|since=c++20|
bool try_acquire() noexcept;
```

Tries to atomically decrement the internal counter by `1` if it is greater than `0`; no blocking occurs regardless.

## Return value

`true` if it decremented the internal counter, otherwise `false`.

## Notes

Implementations are allowed to fail to decrement the counter even if it was greater than `0` - i.e., they are allowed to spuriously fail and return `false`.

## See also


| cpp/thread/counting_semaphore/dsc release | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc acquire | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire_for | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire_until | (see dedicated page) |

