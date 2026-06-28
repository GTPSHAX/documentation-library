---
title: std::swap(std::promise)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/promise/swap2
---

ddcl|header=future|since=c++11|
template< class R >
void swap( promise<R>& lhs, promise<R>& rhs ) noexcept;
Specializes the `std::swap` algorithm for `std::promise`. Exchanges the shared state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - promises whose states to swap

## Return value

(none)

## Example


## See also


| cpp/thread/promise/dsc swap | (see dedicated page) |

