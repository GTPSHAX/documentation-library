---
title: std::pmr::synchronized_pool_resource::~synchronized_pool_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/synchronized_pool_resource/~synchronized_pool_resource
---


```cpp
dcl|since=c++17 | 1=
virtual ~synchronized_pool_resource();
```

Destroys a `synchronized_pool_resource`.
Deallocates all memory owned by this resource by calling `this->release()`.

## See also


| cpp/memory/synchronized_pool_resource/dsc release | (see dedicated page) |

