---
title: std::pmr::unsynchronized_pool_resource::upstream_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/unsynchronized_pool_resource/upstream_resource
---


```cpp
dcl|since=c++17|1=
std::pmr::memory_resource* upstream_resource() const;
```

Returns a pointer to the upstream memory resource. This is the same value as the `upstream` argument passed to the constructor of this object.

## See also


| cpp/memory/unsynchronized_pool_resource/dsc constructor | (see dedicated page) |

