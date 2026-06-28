---
title: std::uses_allocator<std::promise>
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/promise/uses_allocator
---


# uses_allocatorsmall|<std::promise>

ddcl|since=c++11|
template< class R, class Alloc >
struct uses_allocator<std::promise<R>, Alloc> : std::true_type {};
Provides a specialization of the `std::uses_allocator` type trait for `std::promise`.

## See also


| cpp/memory/dsc uses allocator | (see dedicated page) |

