---
title: std::pmr::synchronized_pool_resource::release
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/synchronized_pool_resource/release
---


```cpp
dcl|since=c++17| 1=
void release();
```

Releases all memory owned by this resource by calling the `deallocate` function of the upstream memory resource as needed.
Memory is released back to the upstream resource even if `deallocate` has not been called for some of the allocated blocks.

## See also


| cpp/memory/memory_resource/dsc deallocate | (see dedicated page) |

