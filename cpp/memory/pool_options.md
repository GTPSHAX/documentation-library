---
title: std::pmr::pool_options
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/pool_options
---


```cpp
dcl | since=c++17 |1=
struct pool_options;
```

`std::pmr::pool_options` is a set of constructor options for pool resources including `std::pmr::synchronized_pool_resource` and `std::pmr::unsynchronized_pool_resource`.

## Data members


| dsc | |The largest allocation size that is required to be fulfilled using the pooling mechanism. Attempts to allocate a single block larger than this threshold will be allocated directly from the upstream `std::pmr::memory_resource`. If `largest_required_pool_block` is zero or is greater than an implementation-defined limit, that limit is used instead. The implementation may choose a pass-through threshold larger than specified in this field. | |


## See also

