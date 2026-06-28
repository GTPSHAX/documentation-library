---
title: std::swap(std::unique_lock)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/swap2
---


```cpp
dcl|since=c++11|
template< class Mutex >
void swap( unique_lock<Mutex>& lhs,
unique_lock<Mutex>& rhs ) noexcept;
```

Specializes the `std::swap` algorithm for `std::unique_lock`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - lock wrappers whose states to swap

## Return value

(none)

## Example


## See also


| cpp/thread/unique_lock/dsc swap | (see dedicated page) |

