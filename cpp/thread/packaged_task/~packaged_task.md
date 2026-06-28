---
title: std::packaged_task::~packaged_task
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/~packaged_task
---


```cpp
dcl |1=
~packaged_task();
```

Abandons the shared state and destroys the stored task object.
As with `std::promise::~promise`, if the shared state is abandoned before it was made ready, an `std::future_error` exception is stored with the error code `std::future_errc::broken_promise`).

## Parameters

(none)

## Example

