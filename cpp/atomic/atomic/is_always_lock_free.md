---
title: std::atomic::is_always_lock_free
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/is_always_lock_free
---

ddcl|since=c++17|1=
static constexpr bool is_always_lock_free = /*implementation-defined*/;
Equals `true` if this atomic type is always lock-free and `false` if it is never or sometimes lock-free.
The value of this constant is consistent with both the macro `ATOMIC_xxx_LOCK_FREE`, where defined, with the member function `is_lock_free` and non-member function `std::atomic_is_lock_free`.

## Notes

There is no non-member function equivalent of this static member constant because non-member functions take pointers to atomic types, and therefore aren't as useful in s.

## See also


| cpp/atomic/atomic/dsc is_lock_free|mem=std::atomic<T> | (see dedicated page) |
| cpp/atomic/dsc atomic_is_lock_free | (see dedicated page) |

