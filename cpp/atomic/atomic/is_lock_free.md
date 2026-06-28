---
title: std::atomic::is_lock_free
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/is_lock_free
---


```cpp
dcl|num=1|since=c++11|
bool is_lock_free() const noexcept;
dcl|num=2|since=c++11|
bool is_lock_free() const volatile noexcept;
```

Checks whether the atomic operations on all objects of this type are lock-free.

## Parameters

(none)

## Return value

`true` if the atomic operations on the objects of this type are lock-free, `false` otherwise.

## Notes

All atomic types except for `std::atomic_flag` may be implemented using mutexes or other locking operations, rather than using the lock-free atomic CPU instructions. Atomic types are also allowed to be ''sometimes'' lock-free, e.g. if only aligned memory accesses are naturally atomic on a given architecture, misaligned objects of the same type have to use locks.
The C++ standard recommends (but does not require) that lock-free atomic operations are also address-free, that is, suitable for communication between processes using shared memory.

## Example


### Example


**Output:**
```
std::atomic<A> is lock free? false
std::atomic<B> is lock free? true
```


## See also


| cpp/atomic/dsc atomic_is_lock_free | (see dedicated page) |
| cpp/memory/shared_ptr/atomic|title=atomic_is_lock_free | |
| cpp/atomic/atomic/dsc is_always_lock_free | (see dedicated page) |

