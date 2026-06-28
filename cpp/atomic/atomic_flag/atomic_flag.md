---
title: std::atomic_flag::atomic_flag
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag/atomic_flag
---


```cpp
**Header:** `<`atomic`>`
dcl rev multi|num=1
|since1=c++11|dcl1=
atomic_flag() noexcept = default;
|since2=c++20|dcl2=
constexpr atomic_flag() noexcept;
dcl|num=2|since=c++11|1=
atomic_flag( const atomic_flag& ) = delete;
```

Constructs a new `std::atomic_flag`.
rrev multi
|until1=c++20|rev1=
1. Trivial default constructor, initializes `std::atomic_flag` to unspecified state.
|rev2=
1. Initializes `std::atomic_flag` to clear state.
2. The copy constructor is deleted; `std::atomic_flag` is not copyable.
In addition, `std::atomic_flag` can be value-initialized to clear state with the expression `ATOMIC_FLAG_INIT`. For an `atomic_flag` with static storage duration, this guarantees static initialization: the flag can be used in constructors of static objects.

## See also


| cpp/atomic/dsc ATOMIC_FLAG_INIT | (see dedicated page) |

