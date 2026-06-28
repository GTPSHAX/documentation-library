---
title: std::swap(std::shared_lock)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/swap2
---


```cpp
dcl|since=c++14|
template< class Mutex >
void swap( shared_lock<Mutex>& lhs,
shared_lock<Mutex>& rhs ) noexcept;
```

Specializes the `std::swap` algorithm for `std::shared_lock`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - lock wrappers whose states to swap

## Return value

(none)

## Example


## See also


| cpp/thread/shared_lock/dsc swap | (see dedicated page) |

