---
title: std::barrier::~barrier
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/barrier/~barrier
---

ddcl|since=c++20|
~barrier();
Destroys the `barrier`.

## Notes

It is only safe to invoke the destructor if all threads have been notified. The programmer must ensure that no threads attempt to wait on `*this` once the destructor has been started. The destructor does not notify and release any waiting threads.
