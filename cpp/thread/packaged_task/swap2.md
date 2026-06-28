---
title: std::swap(std::packaged_task)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/swap2
---


```cpp
dcl|since=c++11|
template< class Function, class... Args >
void swap( packaged_task<Function(Args...)> &lhs,
packaged_task<Function(Args...)> &rhs ) noexcept;
```

Specializes the `std::swap` algorithm for `std::packaged_task`. Exchanges the state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - packaged tasks whose states to swap

## Return value

(none)

## Example


## See also


| cpp/thread/packaged_task/dsc swap | (see dedicated page) |

