---
title: std::atomic_signal_fence
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_signal_fence
---


```cpp
dcl | since=c++11 | 1=
extern "C" void atomic_signal_fence( std::memory_order order ) noexcept;
```

Establishes memory synchronization ordering of non-atomic and relaxed atomic accesses, as instructed by `order`, between a thread and a signal handler executed on the same thread. This is equivalent to `std::atomic_thread_fence`, except no CPU instructions for memory ordering are issued. Only reordering of the instructions by the compiler is suppressed as `order` instructs. For example, a fence with release semantics prevents reads or writes from being moved past subsequent writes and a fence with acquire semantics prevents reads or writes from being moved ahead of preceding reads.

## Parameters


### Parameters


## Return value

(none)

## Example

