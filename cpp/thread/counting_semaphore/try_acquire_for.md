---
title: std::counting_semaphore::try_acquire_for
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/counting_semaphore/try_acquire_for
---


```cpp
dcl|since=c++20|
template< class Rep, class Period >
bool try_acquire_for( const std::chrono::duration<Rep, Period>& rel_time );
```

Tries to atomically decrement the internal counter by `1` if it is greater than `0`; otherwise blocks until it is greater than `0` and can successfully decrement the internal counter, or the `rel_time` duration has been exceeded.

## Preconditions

(none)

## Parameters


### Parameters

- `rel_time` - the ''minimum'' duration the function must wait for it to fail

## Return value

`true` if it decremented the internal counter, otherwise `false`.

## Exceptions

May throw `std::system_error` or a timeout-related exception.

## Notes

In practice the function may take longer than `rel_time` to fail.

## See also


| cpp/thread/counting_semaphore/dsc release | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc acquire | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire_until | (see dedicated page) |

