---
title: std::pmr::unsynchronized_pool_resource::~unsynchronized_pool_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/unsynchronized_pool_resource/~unsynchronized_pool_resource
---


```cpp
dcl|since=c++17| 1=
virtual ~unsynchronized_pool_resource();
```

Destroys an `unsynchronized_pool_resource`.
Deallocates all memory owned by this resource by calling `this->release()`.

## See also


| cpp/memory/unsynchronized_pool_resource/dsc release | (see dedicated page) |

