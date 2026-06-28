---
title: std::pmr::monotonic_buffer_resource::release
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/monotonic_buffer_resource/release
---


```cpp
dcl|since=c++17 |
void release();
```

Releases all allocated memory by calling the `deallocate` function on the upstream memory resource as necessary. Resets ''current buffer'' and ''next buffer size'' to their initial values at construction.
Memory is released back to the upstream resource even if `deallocate` has not been called for some of the allocated blocks.

## Defect reports


## See also


| cpp/memory/memory_resource/dsc deallocate | (see dedicated page) |

