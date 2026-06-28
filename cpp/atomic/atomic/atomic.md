---
title: std::atomic::atomic
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/atomic
---


```cpp
dcl|num=1|since=c++11|
constexpr atomic() noexcept(std::is_nothrow_default_constructible_v<T>);
dcl|num=2|since=c++11|
constexpr atomic( T desired ) noexcept;
dcl|num=3|since=c++11|1=
atomic( const atomic& ) = delete;
```

Constructs a new atomic variable.
1. Value-initializes the underlying object (i.e. with `T()`). The initialization is not atomic.
@@ .
2. Initializes the underlying object with `desired`. The initialization is not atomic.
3. Atomic variables are not *CopyConstructible*.

## Parameters


### Parameters

- `desired` - value to initialize with

## Note

In libstdc++, libc++,  was only fixed in C++20 and later. Prior to the fix, the above implementations all initialize the underlying object by default-initialization.

## Defect reports


## See also


| cpp/atomic/dsc atomic_init | (see dedicated page) |

