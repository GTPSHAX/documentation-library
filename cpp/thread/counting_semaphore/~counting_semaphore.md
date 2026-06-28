---
title: std::counting_semaphore::~counting_semaphore
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/counting_semaphore/~counting_semaphore
---


```cpp
dcl|since=c++20|
~counting_semaphore();
```

Destroys the `counting_semaphore` object.

## Notes

It is only safe to invoke the destructor if all threads have been notified. The programmer must ensure that no threads attempt to wait on `*this` once the destructor has been started. The destructor does not notify and release any waiting threads.
