---
title: std::counting_semaphore::release
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/counting_semaphore/release
---


```cpp
dcl|since=c++20|1=
void release( std::ptrdiff_t update = 1 );
```

Atomically increments the internal counter by the value of `update`. Any thread(s) waiting for the counter to be greater than `0`, such as due to being blocked in `acquire`, will subsequently be unblocked.
This operation strongly happens before invocations of `try_acquire` that observe the result of the effects.

## Preconditions

Both `1=update >= 0` and `1=update <= max() - counter` are `true`, where `counter` is the value of the internal counter.

## Parameters


### Parameters

- `update` - the amount to increment the internal counter by

## Exceptions

May throw `std::system_error`.

## See also


| cpp/thread/counting_semaphore/dsc acquire | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire_for | (see dedicated page) |
| cpp/thread/counting_semaphore/dsc try_acquire_until | (see dedicated page) |

