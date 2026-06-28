---
title: std::pmr::monotonic_buffer_resource::~monotonic_buffer_resource
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/monotonic_buffer_resource/~monotonic_buffer_resource
---


```cpp
dcl|since=c++17 | 1=
virtual ~monotonic_buffer_resource();
```

Destroys a `monotonic_buffer_resource`.
Deallocates all memory owned by this resource by calling `this->release()`.

## See also


| cpp/memory/monotonic_buffer_resource/dsc release | (see dedicated page) |

