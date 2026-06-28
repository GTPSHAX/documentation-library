---
title: std::uses_allocator<std::packaged_task>
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/uses_allocator
---


# uses_allocatorsmall|<std::packaged_task>

ddcl|since=c++11|removed=c++17|
template< class R, class Alloc >
struct uses_allocator<std::packaged_task<R>, Alloc> : true_type {};
Provides a specialization of the `std::uses_allocator` type trait for `std::packaged_task`.

## See also


| cpp/memory/dsc uses allocator | (see dedicated page) |

